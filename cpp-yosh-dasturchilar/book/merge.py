import re, os
ROOT = os.path.dirname(os.path.abspath(__file__))
order = [l.strip() for l in open(f'{ROOT}/src/ORDER') if l.strip()]
answers = []  # (topic, text)
MARKS = ["### Ichkarida nima bo", "### Ko'p uchraydigan xatolar", "### Boshqa tillarda", "### O'zingni tekshir", "### Xulosa"]


def parse_addon(path):
    d = {}; mod_end = ''; cur = None; sec = None; buf = []

    def flush():
        nonlocal mod_end
        if sec is None:
            return
        txt = '\n'.join(buf).strip('\n')
        if sec == 'module_end':
            mod_end = txt
        else:
            d.setdefault(cur, {})[sec] = txt

    for line in open(path).read().split('\n'):
        m = re.match(r'^@@(topic|start|end|answers|module_end|deep|before_end)\s*(.*)$', line)
        if m:
            flush(); buf = []
            if m.group(1) == 'topic':
                cur = m.group(2).strip(); sec = None
            else:
                sec = m.group(1)
        else:
            buf.append(line)
    flush()
    return d, mod_end


def apply(src, path, fname):
    d, mod_end = parse_addon(path)
    parts = re.split(r'(?m)^(?=## )', src)
    out = []
    for p in parts:
        m = re.match(r'## (.*)', p)
        if m:
            t = m.group(1).strip()
            if t in d:
                a = d.pop(t)
                if 'start' in a:
                    lines = p.split('\n'); lines.insert(1, '\n' + a['start'] + '\n'); p = '\n'.join(lines)
                if 'end' in a:
                    if '### Xulosa' in p:
                        p = p.replace('### Xulosa', a['end'] + '\n\n### Xulosa', 1)
                    else:
                        p = p.rstrip('\n') + '\n\n' + a['end'] + '\n'
                if 'deep' in a:
                    pos = [p.find(mk) for mk in MARKS if p.find(mk) > 0]
                    if pos:
                        q = min(pos); p = p[:q] + a['deep'] + '\n\n' + p[q:]
                    else:
                        p = p.rstrip('\n') + '\n\n' + a['deep'] + '\n'
                if 'answers' in a:
                    answers.append((t, a['answers']))
        out.append(p)
    src = ''.join(out)
    if mod_end:
        src = src.rstrip('\n') + '\n\n' + mod_end + '\n'
    if d:
        print('UNMATCHED topics in', path, list(d))
    return src


for f in order:
    if f == 'javoblar.md':
        continue
    src = open(f'{ROOT}/src/{f}').read()
    for adir in ('addons', 'deep'):
        ap = f'{ROOT}/{adir}/{f}'
        if os.path.exists(ap):
            src = apply(src, ap, f)
    open(f'{ROOT}/merged/{f}', 'w').write(src)

j = ['# Javoblar: "O\'zingni tekshir" savollari', '', 'Bu yerda har bir mavzu oxiridagi savollarning javoblari berilgan. Avval o\'zing javob berib ko\'r, keyin tekshir!', '']
for t, a in answers:
    j.append(f'### {t}'); j.append(a); j.append('')
open(f'{ROOT}/merged/javoblar.md', 'w').write('\n'.join(j))
print('merged', len(order), 'files;', len(answers), 'answer sets')

# muallif so'zlari va mualliflik huquqi sahifasi
import shutil as _sh
_sh.copyfile('src/front.md', 'merged/front.md')
