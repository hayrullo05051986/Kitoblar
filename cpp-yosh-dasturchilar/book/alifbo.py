"""Joriy o'zbek lotin alifbosidan yangi alifboga (O'RQ-1184, 2026) o'giruvchi.
O' -> Ö, G' -> Ğ, Sh -> Ş, Ch -> Ç, tutuq belgisi -> ʼ. Kod (`...`) o'zgarmaydi."""
import re

APOS = "'ʻ‘’`ʼ"
L = "A-Za-zÀ-žʼ"
# s+h / c+h ni o'zgartirmaslik kerak bo'lgan chet so'zlar (kichik harfda)
FOREIGN = {
    'push', 'push_back', 'push_front', 'hash', 'flush', 'switch', 'char', 'shared', 'shell',
    'bash', 'sha', 'chrome', 'cache', 'match', 'catch', 'touch', 'batch', 'patch', 'fetch',
    'search', 'branch', 'english', 'scratch', 'sketch', 'stroustrup', 'mechanic', 'school',
    'bjarne', 'microsoft', 'github', 'hackerrank', 'leetcode', 'codeforces', 'sharp',
    'thread', 'threads', 'chat', 'chatgpt', 'flash', 'dash', 'crash', 'splash', 'smash',
}

def _is_foreign(word):
    w = word.lower().strip("ʼ")
    if w in FOREIGN:
        return True
    # o'zbek tilida bo'lmaydigan harf birikmalari -> chet so'z
    return bool(re.search(r"w|th|ck|ph|q u|c(?!h)|ee|oo", w))

def _word(m):
    w = m.group(0)
    if _is_foreign(w):
        return w
    w = re.sub(r"SH", "Ş", w); w = re.sub(r"CH", "Ç", w)
    w = w.replace("Sh", "Ş").replace("sh", "ş").replace("Ch", "Ç").replace("ch", "ç")
    return w

def convert_plain(t):
    # o' g' (har xil apostroflar bilan)
    t = re.sub(r"O[" + APOS + "]", "Ö", t)
    t = re.sub(r"o[" + APOS + "]", "ö", t)
    t = re.sub(r"G[" + APOS + "]", "Ğ", t)
    t = re.sub(r"g[" + APOS + "]", "ğ", t)
    # tutuq belgisi: ikki harf orasidagi apostrof
    t = re.sub(r"(?<=[A-Za-zÀ-ž])[" + APOS + r"](?=[A-Za-zÀ-ž])", "ʼ", t)
    # sh, ch
    t = re.sub(r"[A-Za-zÀ-žʼ]+", _word, t)
    return t

def convert(text):
    """Markdown satrini o'giradi; `kod` qismlari va !img fayl nomi o'zgarmaydi."""
    if text.startswith('!img '):
        parts = text[5:].split('|')
        if len(parts) >= 2:
            parts[1] = convert(parts[1])
        return '!img ' + '|'.join(parts)
    m = re.match(r"^(!(?:eslatma|fakt|maslahat|mashq|diqqat)\s)(.*)$", text, re.S)
    if m:
        return m.group(1) + convert(m.group(2))
    out = []
    for i, seg in enumerate(re.split(r"(`[^`]*`)", text)):
        out.append(seg if i % 2 else convert_plain(seg))
    return ''.join(out)

def convert_md(src):
    lines, res, code = src.split('\n'), [], False
    for l in lines:
        if l.startswith('```'):
            code = not code; res.append(l); continue
        res.append(l if code else convert(l))
    return '\n'.join(res)

if __name__ == '__main__':
    for s in ["O'zbekiston, o'quvchi, g'alaba, tog'", "Shahar, quyosh, chiroyli, kuch, Fibonachchi",
              "ma'lumot, she'r, Is'hoq", "push_back va switch, `cout << \"o'g'il\"` chiqaradi",
              "'a' belgisi", "Bu \"shaffof bo'lmagan\" ko'rsatkich", "Bjarne Stroustrup va Microsoft"]:
        print(s, '->', convert(s))
