"""Kitob manbalaridan (merged/ va merged_new/) ilova uchun content.js yasaydi."""
import json, re, html, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUTDIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, '..', 'app', 'renderer')
ORDER = [l.strip() for l in open(os.path.join(ROOT, 'src', 'ORDER')) if l.strip()]
NOTE = {'eslatma': ('ESLATMA', 'ESLATMA'), 'fakt': ('QIZIQARLI FAKT', 'QIZIQARLI FAKT'),
        'maslahat': ('MASLAHAT', 'MASLAHAT'), 'mashq': ("O'ZING SINAB KO'R", 'ÖZING SINAB KÖR'),
        'diqqat': ('DIQQAT', 'DIQQAT')}


def inline(t):
    parts = re.split(r'(`[^`]*`)', t)
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append('<code>' + html.escape(p[1:-1]) + '</code>')
        else:
            p = html.escape(p, quote=False)
            p = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', p)
            p = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<i>\1</i>', p)
            out.append(p)
    return ''.join(out)


def plain(t):
    t = re.sub(r'`([^`]*)`', r'\1', t)
    t = t.replace('**', '').replace('*', '')
    return t


def speech(t):
    t = plain(t)
    t = re.sub(r'C\+\+', 'Si plyus plyus', t)
    t = t.replace('—', ',').replace('→', ', ').replace('#', '')
    return re.sub(r'\s+', ' ', t).strip()


def code_html(lines, kind):
    esc = []
    for l in lines:
        if kind in ('cpp', 'cppx', 'text', 'python', 'java'):
            ci = -1; inq = False
            for k, ch in enumerate(l):
                if ch == '"' and (k == 0 or l[k - 1] != '\\'): inq = not inq
                if not inq and l.startswith('//', k): ci = k; break
            if ci >= 0:
                esc.append(html.escape(l[:ci]) + '<span class="cm">' + html.escape(l[ci:]) + '</span>')
                continue
        esc.append(html.escape(l))
    label = {'output': 'Natija (ekranda):', 'terminal': 'Terminal:'}.get(kind, '')
    cls = 'out' if kind in ('output', 'terminal') else 'src'
    copy = '' if cls == 'out' else '<button class="copy" title="Nusxa olish">⧉</button>'
    lab = f'<div class="clabel">{label}</div>' if label else ''
    return f'<div class="code {cls}">{lab}{copy}<pre>' + '\n'.join(esc) + '</pre></div>'


def render(src, imgdir, new):
    """Bitta mavzu matnini HTML ga aylantiradi. (html, speech_list)"""
    out, say = [], []
    lines = src.split('\n')
    i = 0
    lst = None

    def close_list():
        nonlocal lst
        if lst: out.append(f'</{lst}>'); lst = None

    def sp(text_html, s, tag, cls=''):
        k = len(say); say.append(s)
        c = f' class="{cls}"' if cls else ''
        out.append(f'<{tag}{c} data-s="{k}">{text_html}</{tag}>')

    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            close_list()
            kind = l[3:].strip(); buf = []; i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                buf.append(lines[i]); i += 1
            out.append(code_html(buf, kind)); i += 1; continue
        if l.startswith('%%sign '):
            close_list(); sp(inline(l[7:]), speech(l[7:]), 'p', 'sign')
        elif l.startswith('### '):
            close_list(); sp(inline(l[4:]), speech(l[4:]), 'h3')
        elif l.startswith('!img '):
            close_list()
            parts = [p.strip() for p in l[5:].split('|')]
            f, cap = parts[0], (parts[1] if len(parts) > 1 else '')
            w = float(parts[2]) if len(parts) > 2 and parts[2] else 6
            pct = min(100, round(w / 6.3 * 100))
            out.append(f'<figure><img src="{imgdir}/{f}" style="width:{pct}%" alt="{html.escape(cap)}" loading="lazy">'
                       + (f'<figcaption>{inline(cap)}</figcaption>' if cap else '') + '</figure>')
        elif re.match(r'^!(\w+)\s', l):
            close_list()
            m = re.match(r'^!(\w+)\s+(.*)$', l)
            kind, txt = m.group(1), m.group(2)
            lab = NOTE.get(kind, (kind.upper(), kind.upper()))[1 if new else 0]
            sp(f'<span class="nlabel">{lab}:</span> ' + inline(txt), speech(NOTE.get(kind, (kind,))[0] + '. ' + txt), 'div', 'note ' + kind)
        elif l.startswith('|'):
            close_list()
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                r = lines[i].strip().replace('\\|', '\u0001').strip('|').split('|')
                r = [c.strip().replace('\u0001', '|') for c in r]
                if not all(re.fullmatch(r':?-+:?', c) for c in r): rows.append(r)
                i += 1
            t = ['<div class="tbl"><table>']
            for ri, r in enumerate(rows):
                tag = 'th' if ri == 0 else 'td'
                t.append('<tr>' + ''.join(f'<{tag}>{inline(c)}</{tag}>' for c in r) + '</tr>')
            t.append('</table></div>'); out.append(''.join(t)); continue
        elif re.match(r'^- ', l):
            if lst != 'ul': close_list(); out.append('<ul>'); lst = 'ul'
            sp(inline(l[2:]), speech(l[2:]), 'li')
        elif re.match(r'^\d+\. ', l):
            if lst != 'ol': close_list(); out.append('<ol>'); lst = 'ol'
            t = re.sub(r'^\d+\. ', '', l); sp(inline(t), speech(t), 'li')
        elif l.strip() == '':
            pass
        else:
            close_list(); sp(inline(l), speech(l), 'p')
        i += 1
    close_list()
    return ''.join(out), say


def split(src):
    """Faylni (modul, mavzular) bo'laklariga ajratadi."""
    mods, cur_m, cur_t = [], None, None
    code = False
    for l in src.split('\n'):
        if l.startswith('```'):
            code = not code
        if code or l.startswith('```'):
            if cur_t is not None: cur_t['src'].append(l)
            continue
        if l.startswith('# '):
            cur_m = {'title': l[2:].strip(), 'topics': []}; mods.append(cur_m)
            cur_t = {'title': None, 'src': []}; cur_m['topics'].append(cur_t)
        elif l.startswith('## '):
            if cur_m is None:
                cur_m = {'title': None, 'topics': []}; mods.append(cur_m)
            cur_t = {'title': l[3:].strip().replace('`', ''), 'src': []}; cur_m['topics'].append(cur_t)
        elif cur_t is not None:
            cur_t['src'].append(l)
    for m in mods:
        m['topics'] = [t for t in m['topics'] if t['title'] or any(x.strip() for x in t['src'])]
    return mods


def main():
    data = []
    for f in ORDER:
        old = split(open(os.path.join(ROOT, 'merged', f)).read())
        new = split(open(os.path.join(ROOT, 'merged_new', f)).read())
        for mo, mn in zip(old, new):
            if mo['title'] is None:   # m04a/m04b, m11a/m11b davomi
                mod = data[-1]
            else:
                mod = {'t': [mo['title'], mn['title']], 'topics': []}; data.append(mod)
            for to, tn in zip(mo['topics'], mn['topics']):
                ho, say = render('\n'.join(to['src']), 'img', False)
                hn, _ = render('\n'.join(tn['src']), 'img_new', True)
                tt = [to['title'] or 'Kirish', tn['title'] or 'Kirish']
                if to['title']:
                    say = [speech(to['title'])] + say
                else:
                    say = [speech(mo['title'])] + say
                mod['topics'].append({'t': tt, 'h': [ho, hn], 's': say})
    # Muallif so'zlari — eng boshida
    def front(path):
        ls = open(path).read().split('\n')
        title = ls[0][8:]
        body = ['### ' + l[8:] if l.startswith('%%title ') else l for l in ls[1:]]
        return title, '\n'.join(body)
    t0, b0 = front(os.path.join(ROOT, 'merged', 'front.md'))
    t1, b1 = front(os.path.join(ROOT, 'merged_new', 'front.md'))
    ho, say = render(b0, 'img', False); hn, _ = render(b1, 'img_new', True)
    data.insert(0, {'t': [t0, t1], 'topics': [{'t': [t0, t1], 'h': [ho, hn], 's': [speech(t0)] + say}]})
    n = sum(len(m['topics']) for m in data)
    for m in data:
        for t in m['topics']: t.pop('s', None)   # ovoz olib tashlandi
    os.makedirs(OUTDIR, exist_ok=True)
    with open(os.path.join(OUTDIR, 'content.js'), 'w') as fp:
        fp.write('window.BOOK = ' + json.dumps(data, ensure_ascii=False) + ';\n')
    print(len(data), 'modules', n, 'topics')


main()
