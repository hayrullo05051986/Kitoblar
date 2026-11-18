from comic import *
import numpy as np

# ---------- flowchart primitives ----------
def term(ax, x, y, w, h, t, c=2, fs=11):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={h/2}", fc=LIGHT[c], ec=PAL[c], lw=2))
    text(ax, x, y, t, fs=fs, bold=True)
def proc(ax, x, y, w, h, t, c=0, fs=11, mono=False):
    box(ax, x - w / 2, y - h / 2, w, h, t, fc=LIGHT[c], ec=PAL[c], fs=fs, r=0.05, bold=True, mono=mono)
def io(ax, x, y, w, h, t, c=4, fs=11, mono=False):
    s = 0.25
    ax.add_patch(Polygon([[x - w / 2 + s, y + h / 2], [x + w / 2 + s, y + h / 2], [x + w / 2 - s, y - h / 2], [x - w / 2 - s, y - h / 2]], fc=LIGHT[c], ec=PAL[c], lw=2))
    text(ax, x, y, t, fs=fs, bold=True, mono=mono)
def dec(ax, x, y, w, h, t, c=1, fs=11, mono=False):
    ax.add_patch(Polygon([[x, y + h / 2], [x + w / 2, y], [x, y - h / 2], [x - w / 2, y]], fc=LIGHT[c], ec=PAL[c], lw=2))
    text(ax, x, y, t, fs=fs, bold=True, mono=mono)
def ln(ax, pts, arrowend=True, color="#495057"):
    xs, ys = zip(*pts)
    if len(pts) > 2:
        ax.plot(xs[:-1], ys[:-1], color=color, lw=2)
    arrow(ax, xs[-2], ys[-2], xs[-1], ys[-1], color=color, lw=2, ms=14)
    if len(pts) > 2:
        pass

# legend of shapes
fig, ax = canvas(11, 2.6)
term(ax, 1.2, 1.5, 1.8, 0.7, "Boshlash"); text(ax, 1.2, 0.7, "boshlash / tugatish", fs=10, color="#5A6270")
io(ax, 3.9, 1.5, 1.8, 0.7, "Kiritish"); text(ax, 3.9, 0.7, "kiritish / chiqarish", fs=10, color="#5A6270")
proc(ax, 6.6, 1.5, 1.8, 0.7, "s = a + b"); text(ax, 6.6, 0.7, "amal (jarayon)", fs=10, color="#5A6270")
dec(ax, 9.4, 1.5, 2.0, 1.0, "a > b ?"); text(ax, 9.4, 0.7, "shart (tanlash)", fs=10, color="#5A6270")
save(fig, "a_shapes.png")

# linear: tea
fig, ax = plt.subplots(figsize=(5.2, 7.6), dpi=150); ax.set_xlim(0, 5.2); ax.set_ylim(0, 7.6); ax.axis("off"); ax.set_aspect("equal")
steps = [("t", "Boshlash"), ("p", "Choynakka suv quy"), ("p", "Suvni qaynat"), ("p", "Choynakka choy sol"), ("p", "Qaynoq suv quy"), ("p", "5 daqiqa kut"), ("t", "Tugatish")]
ys = [7.1 - i * 1.08 for i in range(len(steps))]
for (k, t), y in zip(steps, ys):
    (term if k == "t" else proc)(ax, 2.6, y, 3.4 if k == "p" else 2.0, 0.62, t, c=2 if k == "t" else 0, fs=11)
for i in range(len(ys) - 1):
    arrow(ax, 2.6, ys[i] - 0.32, 2.6, ys[i + 1] + 0.32, lw=2, ms=13)
save(fig, "a_tea.png")

# linear: sum
fig, ax = plt.subplots(figsize=(4.4, 5.6), dpi=150); ax.set_xlim(0, 4.4); ax.set_ylim(0, 5.6); ax.axis("off"); ax.set_aspect("equal")
items = [(term, "Boshlash", 2), (io, "a, b ni kirit", 4), (proc, "s = a + b", 0), (io, "s ni chiqar", 4), (term, "Tugatish", 2)]
ys = [5.1 - i * 1.15 for i in range(5)]
for (f, t, c), y in zip(items, ys):
    f(ax, 2.2, y, 2.6 if f is not term else 2.0, 0.62, t, c=c, fs=11)
for i in range(4):
    arrow(ax, 2.2, ys[i] - 0.32, 2.2, ys[i + 1] + 0.32, lw=2, ms=13)
save(fig, "a_sum.png")

# branching: max of two
fig, ax = plt.subplots(figsize=(7.0, 6.2), dpi=150); ax.set_xlim(0, 7.0); ax.set_ylim(0, 6.2); ax.axis("off"); ax.set_aspect("equal")
term(ax, 3.5, 5.8, 2.0, 0.6, "Boshlash")
io(ax, 3.5, 4.85, 2.6, 0.6, "a, b ni kirit")
dec(ax, 3.5, 3.6, 2.4, 1.2, "a > b ?")
io(ax, 1.3, 2.2, 2.2, 0.6, "a ni chiqar")
io(ax, 5.7, 2.2, 2.2, 0.6, "b ni chiqar")
term(ax, 3.5, 0.6, 2.0, 0.6, "Tugatish")
arrow(ax, 3.5, 5.5, 3.5, 5.17); arrow(ax, 3.5, 4.53, 3.5, 4.22)
ax.plot([2.3, 1.3], [3.6, 3.6], color="#495057", lw=2); arrow(ax, 1.3, 3.6, 1.3, 2.52); text(ax, 1.75, 3.85, "ha", fs=11, bold=True, color=PAL[2])
ax.plot([4.7, 5.7], [3.6, 3.6], color="#495057", lw=2); arrow(ax, 5.7, 3.6, 5.7, 2.52); text(ax, 5.25, 3.85, "yo'q", fs=11, bold=True, color=PAL[3])
ax.plot([1.3, 1.3, 3.5], [1.88, 1.3, 1.3], color="#495057", lw=2); ax.plot([5.7, 5.7, 3.5], [1.88, 1.3, 1.3], color="#495057", lw=2)
arrow(ax, 3.5, 1.3, 3.5, 0.92)
save(fig, "a_branch.png")

# loop: sum 1..n
fig, ax = plt.subplots(figsize=(7.2, 7.4), dpi=150); ax.set_xlim(0, 7.2); ax.set_ylim(0, 7.4); ax.axis("off"); ax.set_aspect("equal")
term(ax, 3.0, 7.0, 2.0, 0.6, "Boshlash")
io(ax, 3.0, 6.1, 2.2, 0.6, "n ni kirit")
proc(ax, 3.0, 5.2, 2.6, 0.6, "s = 0,  i = 1", mono=True)
dec(ax, 3.0, 3.9, 2.4, 1.2, "i <= n ?", mono=True)
proc(ax, 3.0, 2.55, 2.4, 0.6, "s = s + i", mono=True)
proc(ax, 3.0, 1.65, 2.4, 0.6, "i = i + 1", mono=True)
io(ax, 6.0, 3.9, 1.8, 0.6, "s ni\nchiqar", fs=10)
term(ax, 6.0, 2.4, 1.8, 0.6, "Tugatish")
for a, b in [(6.7, 6.42), (5.8, 5.52), (4.9, 4.52), (3.3, 2.87), (2.25, 1.97)]:
    arrow(ax, 3.0, a, 3.0, b)
text(ax, 3.35, 3.1, "ha", fs=11, bold=True, color=PAL[2])
arrow(ax, 4.2, 3.9, 5.05, 3.9); text(ax, 4.6, 4.15, "yo'q", fs=11, bold=True, color=PAL[3])
arrow(ax, 6.0, 3.58, 6.0, 2.72)
ax.plot([3.0, 3.0, 0.8, 0.8], [1.35, 0.8, 0.8, 3.9], color=PAL[4], lw=2)
arrow(ax, 0.8, 3.9, 1.8, 3.9, color=PAL[4])
text(ax, 0.55, 2.3, "takrorlash", fs=10, color=PAL[4], bold=True, rotation=90)
save(fig, "a_loop.png")

# Al-Khwarizmi scroll + minaret (generic)
fig, ax = canvas(10, 4.2)
ax.add_patch(FancyBboxPatch((0.05, 0.05), 9.9, 4.1, boxstyle="round,pad=0,rounding_size=0.3", fc="#FFF9DB", ec=PAL[1], lw=2))
# minaret
ax.add_patch(Polygon([[1.2, 0.4], [2.2, 0.4], [2.0, 3.0], [1.4, 3.0]], fc="#4DABF7", ec="#1F2328", lw=1.5))
for yy in (1.0, 1.6, 2.2):
    ax.add_patch(Rectangle((1.3 + (yy - 1) * 0.05, yy), 0.8 - (yy - 1) * 0.1, 0.12, fc="#FFD43B", ec="none"))
ax.add_patch(Rectangle((1.3, 3.0), 0.8, 0.25, fc="#1C7ED6", ec="#1F2328"))
ax.add_patch(Wedge((1.7, 3.25), 0.3, 0, 180, fc="#1C7ED6", ec="#1F2328"))
# scroll
box(ax, 3.0, 0.7, 6.4, 2.8, "", fc="#FFF4D6", ec="#8D6E63", lw=2)
ax.add_patch(Ellipse((3.0, 2.1), 0.35, 2.9, fc="#E9C46A", ec="#8D6E63", lw=2))
ax.add_patch(Ellipse((9.4, 2.1), 0.35, 2.9, fc="#E9C46A", ec="#8D6E63", lw=2))
text(ax, 6.2, 2.95, "Muhammad al-Xorazmiy", fs=15, bold=True, color="#8D6E63")
text(ax, 6.2, 2.4, "(taxminan 783 – 850-yillar, Xorazm)", fs=11, color="#5A6270")
text(ax, 6.2, 1.7, "al-Xorazmiy → \"Algorithmi\" → algoritm", fs=13, bold=True, color=PAL[0])
text(ax, 6.2, 1.1, "\"algebra\" so'zi ham uning kitobidan olingan", fs=11, color="#5A6270")
save(fig, "a_khwarizmi.png")

# robot on grid (algorithmic thinking)
fig, ax = canvas(6, 6)
for i in range(6):
    for j in range(6):
        ax.add_patch(Rectangle((i, j), 1, 1, fc="#F8F9FA" if (i + j) % 2 else "white", ec="#CED4DA"))
for (i, j) in [(1, 1), (1, 2), (3, 3), (3, 4), (4, 1)]:
    ax.add_patch(Rectangle((i, j), 1, 1, fc="#868E96", ec="#495057"))
robot(ax, 0.5, 0.08, 0.38)
ax.add_patch(matplotlib.patches.RegularPolygon((5.5, 5.5), 5, radius=0.38, fc="#FFD43B", ec="#C9A000", lw=2))
path = [(0.5, 0.5), (0.5, 3.5), (2.5, 3.5), (2.5, 5.5), (5.5, 5.5)]
xs, ys = zip(*path)
ax.plot(xs, ys, color=PAL[2], lw=4, ls="--", zorder=5)
save(fig, "a_grid.png")

# ---------- algorithms module diagrams ----------
# Big-O growth chart
fig, ax = plt.subplots(figsize=(7.5, 4.2), dpi=150)
n = np.linspace(1, 20, 200)
for f, lab, c in [(np.ones_like(n), "O(1) — doimiy", PAL[2]), (np.log2(n), "O(log n) — logarifmik", PAL[5]), (n, "O(n) — chiziqli", PAL[0]), (n * np.log2(n), "O(n log n)", PAL[1]), (n ** 2, "O(n²) — kvadratik", PAL[3])]:
    ax.plot(n, f, lw=2.5, color=c, label=lab)
ax.set_ylim(0, 60); ax.set_xlim(1, 20)
ax.set_xlabel("Ma'lumotlar soni (n)", fontsize=11); ax.set_ylabel("Qadamlar soni", fontsize=11)
ax.legend(fontsize=10, frameon=False); ax.spines[["top", "right"]].set_visible(False); ax.grid(alpha=0.25)
fig.savefig(os.path.join(OUT, "a_bigo.png"), bbox_inches="tight", facecolor="white"); plt.close(fig)

# linear search
fig, ax = canvas(10, 2.6)
arr = [7, 3, 9, 4, 8, 1]
for i, v in enumerate(arr):
    c = 2 if v == 4 else (7 if i < 3 else 0)
    box(ax, 0.5 + i * 1.5, 0.9, 1.2, 1.0, str(v), fc=LIGHT[c] if i <= 3 else "#F8F9FA", ec=PAL[c] if i <= 3 else "#CED4DA", fs=18, bold=True, mono=True)
    text(ax, 1.1 + i * 1.5, 0.55, f"{i + 1}-qadam" if i <= 3 else "", fs=9, color="#5A6270")
text(ax, 5.0, 2.3, "4 ni qidiryapmiz: birma-bir tekshiramiz → 4-qadamda topildi!", fs=12, bold=True)
save(fig, "a_linsearch.png")

# binary search
fig, ax = canvas(10, 4.4)
arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
rows = [(0, 9, 4), (5, 9, 7), (5, 6, 5)]
for r, (lo, hi, mid) in enumerate(rows):
    y = 3.4 - r * 1.25
    for i, v in enumerate(arr):
        inside = lo <= i <= hi
        c = 1 if i == mid else (0 if inside else 7)
        fc = LIGHT[c] if inside else "#F1F3F5"; ec = PAL[c] if inside else "#DEE2E6"
        if v == 23 and r == 2: fc, ec = LIGHT[2], PAL[2]
        box(ax, 0.3 + i * 0.94, y, 0.85, 0.75, str(v), fc=fc, ec=ec, fs=12, bold=True, mono=True, color="#1F2328" if inside else "#ADB5BD")
    text(ax, 9.95, y + 0.37, f"{r + 1}-qadam", fs=10, color="#5A6270", ha="left")
text(ax, 5.0, 4.35, "23 ni qidirish: har qadamda yarmini tashlaymiz (o'rtadagisi sariq)", fs=11.5, bold=True)
save(fig, "a_binsearch.png")

# bubble sort passes
fig, ax = canvas(10, 4.2)
passes = [[5, 3, 8, 1], [3, 5, 1, 8], [3, 1, 5, 8], [1, 3, 5, 8]]
for r, p in enumerate(passes):
    y = 3.3 - r * 1.0
    text(ax, 1.0, y + 0.35, "boshida" if r == 0 else f"{r}-o'tish", fs=11, bold=True, color="#5A6270")
    for i, v in enumerate(p):
        done = r > 0 and i >= len(p) - r
        box(ax, 2.3 + i * 1.1, y, 0.9, 0.7, str(v), fc=LIGHT[2] if done else LIGHT[0], ec=PAL[2] if done else PAL[0], fs=14, bold=True, mono=True)
text(ax, 8.2, 2.0, "Har o'tishda eng\nkatta son oxiriga\n\"suzib chiqadi\"", fs=11, color="#5A6270")
save(fig, "a_bubble.png")

# sieve of Eratosthenes
fig, ax = canvas(10, 3.4)
for k in range(2, 41):
    i, j = (k - 2) % 13, (k - 2) // 13
    prime = all(k % d for d in range(2, int(k ** 0.5) + 1))
    box(ax, 0.2 + i * 0.75, 2.3 - j * 0.85, 0.65, 0.65, str(k), fc=LIGHT[2] if prime else "#F1F3F5", ec=PAL[2] if prime else "#DEE2E6", fs=10, bold=prime, color="#1F2328" if prime else "#ADB5BD")
text(ax, 5.0, 0.25, "Yashil — tub sonlar; kulranglar \"elakdan o'tmadi\" (o'chirildi)", fs=11, color="#5A6270")
save(fig, "a_sieve.png")

# Euclid steps
fig, ax = canvas(10, 2.6)
steps = [("EKUB(48, 18)", 0), ("EKUB(18, 12)", 1), ("EKUB(12, 6)", 4), ("EKUB(6, 0) = 6", 2)]
xs, w = flow(ax, [s for s, _ in steps], 0.8, h=0.9, colors=[c for _, c in steps], fs=11)
text(ax, 5.0, 2.2, "Evklid algoritmi: (a, b) → (b, a % b)", fs=12, bold=True)
save(fig, "a_euclid.png")

# ---------- comics ----------
def p_recipe2(ax, x, y):
    box(ax, x + 0.25, y + 0.15, 1.6, 1.45, "1. Suv qaynat\n2. Choy sol\n3. Suv quy\n4. Kut", fc="#FFF9DB", ec=PAL[1], fs=8.5)

def p_props(ax, x, y):
    for i, (t, c) in enumerate([("aniq", 0), ("qadamli", 2), ("natijali", 4)]):
        box(ax, x + 0.25, y + 1.15 - i * 0.45, 1.6, 0.38, t, fc=LIGHT[c], ec=PAL[c], fs=9, bold=True)

def p_flowmini(ax, x, y):
    ax.add_patch(FancyBboxPatch((x + 0.6, y + 1.25), 0.9, 0.3, boxstyle="round,pad=0,rounding_size=0.15", fc=LIGHT[2], ec=PAL[2]))
    ax.add_patch(Polygon([[x + 1.05, y + 1.05], [x + 1.45, y + 0.8], [x + 1.05, y + 0.55], [x + 0.65, y + 0.8]], fc=LIGHT[1], ec=PAL[1]))
    box(ax, x + 0.6, y + 0.1, 0.9, 0.3, "", fc=LIGHT[0], ec=PAL[0], r=0.03)
    for a, b in [(1.25, 1.07), (0.53, 0.42)]:
        arrow(ax, x + 1.05, y + a, x + 1.05, y + b, ms=8, lw=1.2)

def p_steps(ax, x, y):
    for i in range(4):
        box(ax, x + 0.15 + i * 0.45, y + 0.25 + i * 0.3, 0.45, 0.3, "", fc=LIGHT[i], ec=PAL[i], r=0.02)

def p_fork(ax, x, y):
    ax.plot([x + 1.05, x + 1.05], [y + 0.2, y + 0.8], color="#868E96", lw=5)
    ax.plot([x + 1.05, x + 0.4], [y + 0.8, y + 1.4], color="#868E96", lw=5)
    ax.plot([x + 1.05, x + 1.7], [y + 0.8, y + 1.4], color="#868E96", lw=5)
    ax.text(x + 0.3, y + 1.5, "ha", fontsize=9, fontweight="bold", color=PAL[2])
    ax.text(x + 1.6, y + 1.5, "yo'q", fontsize=9, fontweight="bold", color=PAL[3])

def p_wheel(ax, x, y):
    ax.add_patch(Circle((x + 1.05, y + 0.85), 0.6, fc="none", ec=PAL[4], lw=4))
    ax.add_patch(FancyArrowPatch((x + 1.6, y + 1.1), (x + 1.45, y + 1.35), arrowstyle="-|>", mutation_scale=16, color=PAL[4], lw=3))
    ax.text(x + 1.05, y + 0.85, "x10", fontsize=12, ha="center", va="center", fontweight="bold")

def p_grid(ax, x, y):
    for i in range(3):
        for j in range(3):
            ax.add_patch(Rectangle((x + 0.5 + i * 0.4, y + 0.25 + j * 0.4), 0.4, 0.4, fc="white", ec="#ADB5BD"))
    ax.add_patch(matplotlib.patches.RegularPolygon((x + 1.5, y + 1.25), 5, radius=0.15, fc="#FFD43B", ec="#C9A000"))

def p_stopwatch(ax, x, y):
    ax.add_patch(Circle((x + 1.05, y + 0.8), 0.55, fc="white", ec="#1F2328", lw=3))
    ax.plot([x + 1.05, x + 1.05], [y + 0.8, y + 1.2], color=PAL[3], lw=3)
    ax.plot([x + 1.05, x + 1.35], [y + 0.8, y + 0.8], color="#1F2328", lw=3)
    ax.add_patch(Rectangle((x + 0.97, y + 1.35), 0.16, 0.15, fc="#1F2328"))

def p_book(ax, x, y):
    box(ax, x + 0.2, y + 0.3, 1.7, 1.1, "LUG'AT\nA ... Z", fc=PAL[0], ec="#1F2328", fs=10, bold=True, color="white", r=0.05)

def p_bars(ax, x, y):
    for i, h in enumerate([0.4, 0.7, 1.0, 1.3]):
        box(ax, x + 0.3 + i * 0.4, y + 0.2, 0.32, h, "", fc=LIGHT[i], ec=PAL[i], r=0.03)

def p_numbers(ax, x, y):
    ax.text(x + 1.05, y + 0.85, "2 3 5 7\n11 13", fontsize=12, ha="center", va="center", fontweight="bold", color=PAL[2])

C = {
 "c_algo": [dict(m="Kodi, 'algoritm' degani nima? Juda qiyin so'z ekan...", mm="think"),
            dict(k="Bu shunchaki aniq qadamlar ketma-ketligi! Choy damlash retsepti ham algoritm. Bu so'z esa bobomiz al-Xorazmiy nomidan kelib chiqqan!", first="k", prop=p_recipe2, m="Voy, al-Xorazmiy bizning yurtdan-ku!", mm="wow", arm="up")],
 "c_algoprops": [dict(m="Har qanday ko'rsatmalar ro'yxati algoritm bo'la oladimi?", mm="think", prop=p_props),
                 dict(k="Yo'q! Yaxshi algoritm aniq bo'lishi, qadamlarga bo'linishi va albatta natijaga olib kelishi kerak. 'Bir oz shakar sol' — aniq emas!", first="k", m="'2 qoshiq shakar sol' — aniq!", mm="happy")],
 "c_flowchart": [dict(m="Algoritmni chiroyli qilib qanday tasvirlasam bo'ladi?", mm="think"),
                 dict(k="Blok-sxema chiz! Har bir shaklning o'z ma'nosi bor: oval — boshlash, to'rtburchak — amal, romb — savol. Strelkalar esa yo'lni ko'rsatadi.", first="k", prop=p_flowmini, m="Xuddi xazina xaritasi kabi!", mm="wow")],
 "c_linear": [dict(m="Ertalab tishimni yuvaman, yuvinaman, nonushta qilaman — har kuni bir xil tartibda.", mm="happy", prop=p_steps),
              dict(k="Bu chiziqli algoritm! Qadamlar birin-ketin, hech qanday tanlovsiz bajariladi — xuddi zinapoyadan chiqqandek.", first="k", m="Eng oddiy algoritm ekan!", mm="wow")],
 "c_branching": [dict(m="Agar yomg'ir yog'sa — soyabon, yog'masa — ko'zoynak olaman. Bu ham algoritmmi?", mm="think", prop=p_fork),
                 dict(k="Ha, tarmoqlanuvchi algoritm! Shartga qarab yo'l ikkiga ayriladi — xuddi yo'l ayrilishidagi kabi.", first="k", m="Algoritm ham qaror qabul qilar ekan!", mm="happy", arm="up")],
 "c_loopalgo": [dict(m="Bassaynda 10 marta suzib borib-kelishim kerak. Har birini alohida yozamanmi?", mm="think"),
                dict(k="Yo'q! 'Suzib borib kel' qadamini 10 marta takrorla deysan. Bu takrorlanuvchi (tsiklik) algoritm.", first="k", prop=p_wheel, m="Qisqa va aniq!", mm="wow")],
 "c_thinking": [dict(m="Katta masalani yechishni qayerdan boshlashni bilmayman...", mm="sad", prop=p_grid),
                dict(k="Uni kichik bo'laklarga bo'l! Avval nima berilganini va nima topish kerakligini aniqla, keyin qadamlarni birma-bir o'yla.", first="k", m="Bo'lib-bo'lib yechaman!", mm="happy", arm="up")],
 "c_bigo": [dict(m="Ikkala dasturim ham to'g'ri ishlaydi. Qaysi biri yaxshiroq?", mm="think", prop=p_stopwatch),
            dict(k="Ma'lumot ko'payganda qaysi biri tezroq ishlashiga qara! Algoritm tezligini baholash uchun 'Big-O' degan maxsus o'lchov bor.", first="k", m="Tezlik musobaqasi!", mm="wow")],
 "c_search": [dict(m="Lug'atdan so'zni qanday tez topaman? Birinchi sahifadan boshlab varaqlaymanmi?", mm="think", prop=p_book),
              dict(k="Yo'q! O'rtasidan ochasan va so'z oldindami yoki keyindami — shunga qarab yarmini tashlaysan. Bu ikkilik qidiruv!", first="k", m="Har safar yarmi tashlanadi — zo'r!", mm="wow")],
 "c_sort": [dict(m="Sinfdoshlarimni bo'yi bo'yicha qatorga qanday tizaman?", mm="think", prop=p_bars),
            dict(k="Saralash algoritmlari bilan! Masalan, yonma-yon turganlarni solishtirib, kerak bo'lsa joyini almashtirasan — bu 'pufakcha' usuli.", first="k", m="Har kim o'z joyini topadi!", mm="happy")],
 "c_numbers": [dict(m="Tub sonlarni topishning tez usuli bormi?", mm="think", prop=p_numbers),
               dict(k="Bor! Qadimgi yunon olimi Eratosfenning 'elagi' — keraksiz sonlarni elab tashlab, faqat tub sonlarni qoldiradi.", first="k", m="2000 yildan ortiq yashagan algoritm!", mm="wow")],
}
for k, v in C.items():
    comic(k + ".png", v)
fig, ax = canvas(10, 3.4)
ax.add_patch(FancyBboxPatch((0.05, 0.05), 9.9, 3.3, boxstyle="round,pad=0,rounding_size=0.35", fc=LIGHT[1], ec=PAL[1], lw=2.5))
robot(ax, 1.7, 0.35, 1.15, color=PAL[1], wave=True)
text(ax, 6.2, 2.75, "0-modul: Algoritmlash asoslari", fs=19, bold=True, color="#C78A00")
box(ax, 3.7, 0.55, 5.6, 1.45, "", fc="white", ec="#495057", r=0.25, lw=1.8)
ax.add_patch(Polygon([[3.72, 1.0], [3.72, 1.4], [3.05, 1.05]], closed=True, fc="white", ec="none", zorder=5))
ax.plot([3.7, 3.05, 3.7], [1.0, 1.05, 1.4], color="#495057", lw=1.8, zorder=6)
text(ax, 6.5, 1.275, "Kod yozishdan oldin —\nqanday o'ylashni o'rganamiz!", fs=15)
save(fig, "banner00.png")
fig, ax = canvas(10, 3.4)
ax.add_patch(FancyBboxPatch((0.05, 0.05), 9.9, 3.3, boxstyle="round,pad=0,rounding_size=0.35", fc=LIGHT[5], ec=PAL[5], lw=2.5))
robot(ax, 1.7, 0.35, 1.15, color=PAL[5], wave=True)
text(ax, 6.2, 2.75, "14-modul: Mashhur algoritmlar", fs=19, bold=True, color="#0C8599")
box(ax, 3.7, 0.55, 5.6, 1.45, "", fc="white", ec="#495057", r=0.25, lw=1.8)
ax.add_patch(Polygon([[3.72, 1.0], [3.72, 1.4], [3.05, 1.05]], closed=True, fc="white", ec="none", zorder=5))
ax.plot([3.7, 3.05, 3.7], [1.0, 1.05, 1.4], color="#495057", lw=1.8, zorder=6)
text(ax, 6.5, 1.275, "Qidirish, saralash va sonlar\nsirlari — C++ da!", fs=15)
save(fig, "banner14.png")
print("ok")
