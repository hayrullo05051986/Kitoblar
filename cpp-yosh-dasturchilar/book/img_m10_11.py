from comic import *

# ================= diagrams =================
# class -> objects (cookie cutter / blueprint)
fig, ax = canvas(10, 4)
box(ax, 0.3, 1.0, 2.8, 2.6, "", fc="#E7F5FF", ec=PAL[0], lw=2.5)
text(ax, 1.7, 3.3, "class Mushuk", fs=12, bold=True, mono=True, color=PAL[0])
for i, t in enumerate(["ism", "rang", "yosh", "miyovla()", "uxla()"]):
    text(ax, 0.55, 2.85 - i * 0.38, ("• " + t), fs=11, ha="left", mono=True)
text(ax, 1.7, 0.6, "CHIZMA (klass)", fs=11, bold=True, color="#5A6270")
for i, (n, r, c) in enumerate([("Mosh", "kulrang", 7), ("Laylak", "oq", 5), ("Qoravoy", "qora", 3)]):
    x = 4.2 + i * 1.95
    box(ax, x, 1.0, 1.75, 2.2, f"{n}\n\n{r}", fc=LIGHT[c], ec=PAL[c], fs=11, bold=True)
    ax.add_patch(Polygon([[x + 0.35, 3.2], [x + 0.55, 3.6], [x + 0.75, 3.2]], fc=PAL[c], ec="#1F2328"))
    ax.add_patch(Polygon([[x + 1.0, 3.2], [x + 1.2, 3.6], [x + 1.4, 3.2]], fc=PAL[c], ec="#1F2328"))
arrow(ax, 3.2, 2.2, 4.1, 2.2, lw=2.5, ms=16)
text(ax, 7.1, 0.6, "OBYEKTLAR (klassdan yasalgan nusxalar)", fs=11, bold=True, color="#5A6270")
save(fig, "m10_class.png")

# procedural vs oop
fig, ax = canvas(10, 3.8)
text(ax, 2.4, 3.5, "Protsedurali", fs=13, bold=True, color=PAL[3])
for i, t in enumerate(["ism, ochlik, rang", "ovqatlantir()", "o'ynat()"]):
    box(ax, 0.4 + (i % 2) * 0.2, 2.4 - i * 0.85, 3.6, 0.65, t, fc=LIGHT[3] if i == 0 else "#F8F9FA", ec=PAL[3], fs=11, mono=True)
text(ax, 2.4, 0.15, "ma'lumot va funksiyalar alohida", fs=10, color="#5A6270")
text(ax, 7.4, 3.5, "Obyektga yo'naltirilgan", fs=13, bold=True, color=PAL[2])
box(ax, 5.4, 0.6, 4.0, 2.6, "", fc=LIGHT[2], ec=PAL[2], lw=2.5)
text(ax, 7.4, 2.85, "Mushuk", fs=12, bold=True, mono=True, color=PAL[2])
for i, t in enumerate(["ism, ochlik, rang", "ovqatlan()", "oyna()"]):
    box(ax, 5.7, 2.15 - i * 0.55, 3.4, 0.45, t, fc="white", ec=PAL[2], fs=10, mono=True)
text(ax, 7.4, 0.15, "hammasi bitta \"quti\"da", fs=10, color="#5A6270")
save(fig, "m10_proc_oop.png")

# constructor / destructor lifecycle
fig, ax = canvas(10, 2.8)
xs, w = flow(ax, ["Konstruktor\n(tug'ilish)", "Obyekt ishlaydi\n(hayot)", "Destruktor\n(xayrlashuv)"], 0.7, h=1.2, colors=[2, 0, 3], fs=12)
text(ax, 5.0, 2.4, "Obyektning hayot yo'li", fs=13, bold=True)
save(fig, "m10_ctor.png")

# abstraction: car dashboard vs engine
fig, ax = canvas(10, 3.6)
box(ax, 0.3, 0.5, 4.2, 2.7, "", fc=LIGHT[0], ec=PAL[0])
text(ax, 2.4, 2.9, "Foydalanuvchi ko'radi", fs=12, bold=True, color=PAL[0])
for i, t in enumerate(["haydash()", "tormoz()", "signal()"]):
    box(ax, 0.6 + i * 1.3, 1.2, 1.15, 0.8, t, fc="white", ec=PAL[0], fs=9.5, mono=True, bold=True)
box(ax, 5.4, 0.5, 4.2, 2.7, "", fc="#343A40", ec="#1F2328")
text(ax, 7.5, 2.9, "Yashirin (private)", fs=12, bold=True, color="#FFD43B")
for i, t in enumerate(["dvigatel", "yonilg'i nasosi", "uzatmalar qutisi"]):
    text(ax, 7.5, 2.25 - i * 0.55, t, fs=11, color="#CED4DA", mono=True)
save(fig, "m10_abstraction.png")

# generic: one template many types
fig, ax = canvas(10, 3.4)
box(ax, 3.5, 2.2, 3.0, 0.9, "kattasi<T>(a, b)", fc="#FFF4D6", ec=PAL[1], fs=12, bold=True, mono=True)
for i, (t, ex, c) in enumerate([("int", "kattasi(3, 7) → 7", 0), ("double", "kattasi(2.5, 1.5) → 2.5", 2), ("char", "kattasi('a', 'z') → z", 4)]):
    box(ax, 0.2 + i * 3.3, 0.3, 3.1, 0.9, f"T = {t}\n{ex}", fc=LIGHT[c], ec=PAL[c], fs=10, mono=True)
    arrow(ax, 5.0, 2.15, 1.75 + i * 3.3, 1.25, lw=1.5, ms=12)
save(fig, "m10_generic.png")

# this pointer
fig, ax = canvas(10, 3.2)
for i, (n, c) in enumerate([("ali", 0), ("vali", 2)]):
    x = 0.5 + i * 5
    box(ax, x, 0.5, 4.0, 2.0, "", fc=LIGHT[c], ec=PAL[c])
    text(ax, x + 2.0, 2.2, f"obyekt: {n}", fs=12, bold=True, mono=True, color=PAL[c])
    text(ax, x + 2.0, 1.4, f"{n}.salomlash()", fs=11, mono=True)
    text(ax, x + 2.0, 0.85, f"this → &{n}", fs=11, mono=True, color="#C7254E", bold=True)
save(fig, "m10_this.png")

# static member: shared counter
fig, ax = canvas(10, 3.4)
box(ax, 3.6, 2.2, 2.8, 1.0, "static int soni = 3", fc="#FFF4D6", ec=PAL[1], fs=11, bold=True, mono=True)
for i, n in enumerate(["o1", "o2", "o3"]):
    x = 0.6 + i * 3.2
    box(ax, x, 0.3, 2.2, 1.0, f"{n}\n(o'z ismi)", fc=LIGHT[i * 2], ec=PAL[i * 2], fs=11, bold=True)
    arrow(ax, x + 1.1, 1.35, 5.0, 2.15, lw=1.5, ms=12, color="#868E96")
text(ax, 8.6, 2.7, "hamma uchun\nbitta umumiy", fs=10, color="#5A6270")
save(fig, "m10_static.png")

# inheritance tree
fig, ax = canvas(10, 4)
box(ax, 3.7, 2.9, 2.6, 0.85, "Hayvon\nism, yosh, ye()", fc=LIGHT[1], ec=PAL[1], fs=10.5, bold=True)
for i, (n, s, c) in enumerate([("Mushuk", "miyovla()", 0), ("It", "vovulla()", 2), ("Qush", "uch()", 4)]):
    x = 0.4 + i * 3.25
    box(ax, x, 0.6, 2.6, 1.0, f"{n}\n{s}", fc=LIGHT[c], ec=PAL[c], fs=10.5, bold=True)
    arrow(ax, x + 1.3, 1.65, 5.0, 2.85, lw=1.8, ms=14, color="#495057")
text(ax, 8.9, 3.3, "ota klass\n(asosiy)", fs=10, color="#5A6270")
text(ax, 5.0, 0.2, "bola klasslar ota klassning hamma narsasini meros oladi + o'zinikini qo'shadi", fs=10, color="#5A6270")
save(fig, "m11_inherit.png")

# polymorphism
fig, ax = canvas(10, 3.4)
box(ax, 0.3, 1.2, 2.6, 1.0, "Hayvon* h", fc="#F6F8FA", ec="#ADB5BD", fs=12, mono=True, bold=True)
text(ax, 1.6, 0.8, "h->ovozChiqar()", fs=11, mono=True, color="#C7254E")
for i, (n, s, c) in enumerate([("Mushuk", "Miyov!", 0), ("It", "Vov!", 2), ("Sigir", "Muu!", 1)]):
    y = 2.5 - i * 1.0
    box(ax, 4.2, y, 2.2, 0.75, n, fc=LIGHT[c], ec=PAL[c], fs=11, bold=True)
    box(ax, 7.2, y, 2.2, 0.75, f'"{s}"', fc="white", ec=PAL[c], fs=12, bold=True)
    arrow(ax, 3.0, 1.7, 4.15, y + 0.37, lw=1.5, ms=12, color="#868E96")
    arrow(ax, 6.45, y + 0.37, 7.15, y + 0.37, lw=1.5, ms=12)
save(fig, "m11_poly.png")

# stack vs heap
fig, ax = canvas(10, 3.8)
box(ax, 0.4, 0.3, 3.6, 3.0, "", fc=LIGHT[0], ec=PAL[0])
text(ax, 2.2, 3.0, "STEK (tez, kichik)", fs=12, bold=True, color=PAL[0])
for i, t in enumerate(["int x = 5", "int* p = 0x9A0", "double d"]):
    box(ax, 0.7, 2.1 - i * 0.65, 3.0, 0.5, t, fc="white", ec=PAL[0], fs=10, mono=True)
box(ax, 5.6, 0.3, 4.0, 3.0, "", fc=LIGHT[1], ec=PAL[1])
text(ax, 7.6, 3.0, "UYUM / heap (katta)", fs=12, bold=True, color="#C78A00")
box(ax, 6.2, 1.3, 2.8, 0.8, "new int(42)\n0x9A0", fc="white", ec=PAL[1], fs=10, mono=True, bold=True)
arrow(ax, 3.75, 1.7, 6.15, 1.7, color=PAL[4], lw=2)
save(fig, "m11_heap.png")

# exception flow
fig, ax = canvas(10, 3.6)
box(ax, 0.3, 0.4, 4.6, 2.8, "", fc=LIGHT[0], ec=PAL[0])
text(ax, 2.6, 2.9, "try { ... }", fs=12, bold=True, mono=True, color=PAL[0])
box(ax, 0.7, 1.6, 3.8, 0.7, "throw \"Xato!\";", fc="#FFE3E3", ec=PAL[3], fs=11, mono=True, bold=True)
text(ax, 2.6, 0.9, "qolgan kod bajarilmaydi", fs=10, color="#ADB5BD")
box(ax, 5.8, 1.2, 3.9, 1.4, "catch (...) {\n  xatoni hal qil\n}", fc=LIGHT[2], ec=PAL[2], fs=11, mono=True, bold=True)
arrow(ax, 4.55, 1.95, 5.75, 1.95, color=PAL[3], lw=2.5, rad=-0.3)
save(fig, "m11_exception.png")

# file streams
fig, ax = canvas(10, 3.2)
box(ax, 0.3, 0.8, 2.4, 1.6, "Dastur", fc=LIGHT[0], ec=PAL[0], fs=13, bold=True)
ax.add_patch(Polygon([[7.4, 0.6], [9.2, 0.6], [9.6, 1.0], [9.6, 2.6], [7.4, 2.6]], fc="#FFF9DB", ec="#1F2328", lw=1.5))
text(ax, 8.5, 1.6, "baholar.txt", fs=11, bold=True, mono=True)
arrow(ax, 2.8, 2.0, 7.3, 2.0, color=PAL[2], lw=2.5); text(ax, 5.05, 2.35, "ofstream — yozish", fs=11, bold=True, color=PAL[2])
arrow(ax, 7.3, 1.2, 2.8, 1.2, color=PAL[4], lw=2.5); text(ax, 5.05, 0.8, "ifstream — o'qish", fs=11, bold=True, color=PAL[4])
save(fig, "m11_files.png")

# multiple inheritance (diamond-ish)
fig, ax = canvas(10, 3.6)
box(ax, 0.8, 2.3, 3.0, 0.9, "Uchuvchi\nuch()", fc=LIGHT[0], ec=PAL[0], fs=11, bold=True)
box(ax, 6.2, 2.3, 3.0, 0.9, "Suzuvchi\nsuz()", fc=LIGHT[5], ec=PAL[5], fs=11, bold=True)
box(ax, 3.5, 0.3, 3.0, 0.9, "Ordak\nuch() + suz()", fc=LIGHT[1], ec=PAL[1], fs=11, bold=True)
arrow(ax, 4.2, 1.25, 2.3, 2.25, lw=2, ms=14); arrow(ax, 5.8, 1.25, 7.7, 2.25, lw=2, ms=14)
save(fig, "m11_multi.png")

# operator overloading
fig, ax = canvas(10, 2.8)
box(ax, 0.3, 0.9, 2.2, 1.0, "(1, 2)", fc=LIGHT[0], ec=PAL[0], fs=14, mono=True, bold=True)
text(ax, 2.95, 1.4, "+", fs=24, bold=True)
box(ax, 3.4, 0.9, 2.2, 1.0, "(3, 4)", fc=LIGHT[2], ec=PAL[2], fs=14, mono=True, bold=True)
text(ax, 6.05, 1.4, "=", fs=24, bold=True)
box(ax, 6.5, 0.9, 2.2, 1.0, "(4, 6)", fc=LIGHT[1], ec=PAL[1], fs=14, mono=True, bold=True)
text(ax, 4.5, 2.4, "Vektor + Vektor — o'zimiz o'rgatgan + amali", fs=12, bold=True)
save(fig, "m11_opover.png")

# ================= comics =================
def p_cookie(ax, x, y):
    ax.add_patch(Polygon([[x + 0.2, y + 0.4], [x + 0.6, y + 1.4], [x + 1.0, y + 0.4]], fc="none", ec="#868E96", lw=4))
    for i, c in enumerate([1, 6, 7]):
        ax.add_patch(Polygon([[x + 1.15 + i * 0.32, y + 0.3], [x + 1.3 + i * 0.32, y + 0.7], [x + 1.45 + i * 0.32, y + 0.3]], fc=PAL[c], ec="#1F2328", lw=0.8))

def p_twohouses(ax, x, y):
    for i, c in enumerate([3, 0]):
        bx = x + 0.15 + i * 1.05
        ax.add_patch(Polygon([[bx, y + 0.9], [bx + 0.45, y + 1.4], [bx + 0.9, y + 0.9]], fc=PAL[c], ec="#1F2328"))
        box(ax, bx + 0.1, y + 0.25, 0.7, 0.65, "", fc="#FFF4D6", ec="#1F2328", r=0.02)

def p_baby(ax, x, y):
    ax.add_patch(Circle((x + 0.6, y + 0.9), 0.35, fc="#FFF4D6", ec="#1F2328"))
    ax.text(x + 0.6, y + 0.9, "new", fontsize=8, ha="center", va="center", fontweight="bold", family="DejaVu Sans Mono")
    arrow(ax, x + 1.0, y + 0.9, x + 1.3, y + 0.9, ms=10)
    ax.add_patch(Circle((x + 1.65, y + 0.9), 0.35, fc="#DEE2E6", ec="#1F2328"))
    ax.text(x + 1.65, y + 0.9, "~", fontsize=16, ha="center", va="center", fontweight="bold")

def p_car(ax, x, y):
    box(ax, x + 0.1, y + 0.45, 1.9, 0.55, "", fc=PAL[3], ec="#1F2328", r=0.15)
    ax.add_patch(Polygon([[x + 0.5, y + 1.0], [x + 0.75, y + 1.35], [x + 1.4, y + 1.35], [x + 1.65, y + 1.0]], fc=PAL[3], ec="#1F2328"))
    for wx in (0.5, 1.6):
        ax.add_patch(Circle((x + wx, y + 0.42), 0.17, fc="#343A40"))

def p_box_any(ax, x, y):
    box(ax, x + 0.4, y + 0.3, 1.3, 1.0, "<T>", fc="#FFF4D6", ec=PAL[1], fs=14, bold=True, mono=True)
    for i, (t, c) in enumerate([("1", 0), ("'a'", 2), ("2.5", 4)]):
        ax.text(x + 0.3 + i * 0.75, y + 1.5, t, fontsize=9, ha="center", fontweight="bold", color=PAL[c], family="DejaVu Sans Mono")

def p_mirror(ax, x, y):
    ax.add_patch(Ellipse((x + 1.05, y + 0.9), 1.0, 1.3, fc="#D0EBFF", ec="#868E96", lw=3))
    ax.text(x + 1.05, y + 0.9, "this", fontsize=12, ha="center", va="center", fontweight="bold", family="DejaVu Sans Mono", color=PAL[4])

def p_board(ax, x, y):
    box(ax, x + 0.25, y + 0.35, 1.6, 1.15, "Sinf\n28 ta", fc="#2B8A3E", ec="#8D6E63", fs=12, bold=True, color="white", lw=3)

def p_plus_vec(ax, x, y):
    ax.text(x + 1.05, y + 0.85, "(1,2) + (3,4)", fontsize=10, ha="center", va="center", fontweight="bold", family="DejaVu Sans Mono")
    ax.text(x + 1.05, y + 0.4, "= (4,6)", fontsize=11, ha="center", va="center", fontweight="bold", family="DejaVu Sans Mono", color=PAL[2])

def p_key(ax, x, y):
    ax.add_patch(Circle((x + 0.6, y + 0.9), 0.25, fc="none", ec="#F2A900", lw=4))
    ax.plot([x + 0.85, x + 1.7], [y + 0.9, y + 0.9], color="#F2A900", lw=4)
    ax.plot([x + 1.5, x + 1.5], [y + 0.9, y + 0.7], color="#F2A900", lw=4)
    ax.text(x + 1.15, y + 1.3, "friend", fontsize=10, ha="center", fontweight="bold", color=PAL[4], family="DejaVu Sans Mono")

def p_balloon(ax, x, y):
    for i, (c, s) in enumerate([(3, 0.25), (1, 0.32), (2, 0.4)]):
        ax.add_patch(Ellipse((x + 0.45 + i * 0.6, y + 1.2), s * 1.4, s * 1.8, fc=PAL[c], ec="#1F2328", lw=1))
        ax.plot([x + 0.45 + i * 0.6, x + 0.45 + i * 0.6], [y + 1.2 - s * 0.9, y + 0.25], color="#868E96", lw=1)

def p_family(ax, x, y):
    box(ax, x + 0.6, y + 1.05, 0.9, 0.45, "Ota", fc=LIGHT[1], ec=PAL[1], fs=9, bold=True)
    box(ax, x + 0.1, y + 0.25, 0.8, 0.45, "Bola1", fc=LIGHT[0], ec=PAL[0], fs=8, bold=True)
    box(ax, x + 1.2, y + 0.25, 0.8, 0.45, "Bola2", fc=LIGHT[2], ec=PAL[2], fs=8, bold=True)
    arrow(ax, x + 0.5, y + 0.72, x + 0.85, y + 1.02, ms=9); arrow(ax, x + 1.6, y + 0.72, x + 1.25, y + 1.02, ms=9)

def p_animals_sound(ax, x, y):
    for i, (s, c) in enumerate([("Miyov!", 0), ("Vov!", 2), ("Muu!", 1)]):
        box(ax, x + 0.05 + i * 0.7, y + 0.5 + (i % 2) * 0.4, 0.65, 0.45, s, fc=LIGHT[c], ec=PAL[c], fs=8, bold=True)

def p_shape_q(ax, x, y):
    box(ax, x + 0.4, y + 0.3, 1.3, 1.1, "Shakl\n?", fc="#F1F3F5", ec="#868E96", fs=12, bold=True)

def p_duck(ax, x, y):
    ax.add_patch(Ellipse((x + 1.0, y + 0.6), 1.1, 0.6, fc="#FFD43B", ec="#1F2328"))
    ax.add_patch(Circle((x + 1.5, y + 1.05), 0.25, fc="#FFD43B", ec="#1F2328"))
    ax.add_patch(Polygon([[x + 1.72, y + 1.05], [x + 1.95, y + 1.0], [x + 1.72, y + 0.95]], fc="#FF922B"))
    ax.add_patch(Circle((x + 1.55, y + 1.1), 0.04, fc="#1F2328"))
    ax.plot([x + 0.2, x + 2.0], [y + 0.3, y + 0.3], color=PAL[5], lw=3)

def p_stamp(ax, x, y):
    box(ax, x + 0.3, y + 0.35, 1.5, 0.9, "template", fc="#FFF4D6", ec=PAL[1], fs=11, bold=True, mono=True)
    ax.plot([x + 1.05, x + 1.05], [y + 1.25, y + 1.6], color="#8D6E63", lw=6)

def p_net(ax, x, y):
    ax.plot([x + 0.2, x + 1.9], [y + 0.3, y + 0.3], color="#495057", lw=2)
    for k in range(6):
        ax.plot([x + 0.2 + k * 0.34, x + 0.2 + k * 0.34], [y + 0.3, y + 0.9], color="#868E96", lw=1)
    ax.plot([x + 0.2, x + 1.9], [y + 0.9, y + 0.9], color="#868E96", lw=1)
    ax.add_patch(Circle((x + 1.05, y + 1.3), 0.18, fc=PAL[3], ec="#1F2328"))
    ax.text(x + 1.05, y + 1.3, "!", fontsize=10, ha="center", va="center", color="white", fontweight="bold")

def p_diary(ax, x, y):
    box(ax, x + 0.4, y + 0.25, 1.3, 1.3, "Kundalik\n.txt", fc=PAL[7], ec="#1F2328", fs=10, bold=True, color="white", r=0.05)

def p_magnifier(ax, x, y):
    box(ax, x + 0.1, y + 0.4, 1.0, 0.9, "Hayvon*", fc="#F6F8FA", ec="#ADB5BD", fs=8, mono=True)
    ax.add_patch(Circle((x + 1.45, y + 0.95), 0.32, fc="#D0EBFF", ec="#495057", lw=3))
    ax.plot([x + 1.68, x + 1.95], [y + 0.72, y + 0.45], color="#495057", lw=4)
    ax.text(x + 1.45, y + 0.95, "It?", fontsize=9, ha="center", va="center", fontweight="bold")

C = {
 "c_oop": [dict(m="O'yinimda 100 ta mushuk bo'lsa, har birining ismi, rangi, ochligini alohida o'zgaruvchilarda saqlaymanmi?", mm="think", fs=12),
           dict(k="OOP da mushukning hamma ma'lumoti va harakatlari bitta 'quti' — klassda bo'ladi. Keyin undan xohlagancha mushuk yasaysan!", first="k", prop=p_twohouses, m="Tartibli va qulay ekan!", mm="wow")],
 "c_class": [dict(m="Klass va obyektning farqi nima?", mm="think", prop=p_cookie),
             dict(k="Klass — pechenye qolipi, obyekt — shu qolip bilan yasalgan pechenye. Qolip bitta, pechenyelar esa ko'p bo'lishi mumkin!", first="k", m="Endi tushundim! Mmm, pechenye...", mm="happy", arm="up")],
 "c_ctor": [dict(m="Obyekt yaratilganda unga darhol ism berib qo'ysam bo'ladimi?", mm="think"),
            dict(k="Konstruktor aynan shuning uchun! U obyekt 'tug'ilganda' avtomatik ishlaydi. Destruktor esa obyekt yo'q bo'layotganda xayrlashadi.", first="k", prop=p_baby, m="Tug'ilish va xayrlashuv funksiyalari!", mm="wow")],
 "c_abstraction": [dict(m="Dadam mashina haydaydi, lekin dvigatel qanday ishlashini bilmaydi.", mm="happy", prop=p_car),
                   dict(k="Bu abstraksiya! Faqat kerakli tugmalar ko'rsatiladi, murakkab ichki qism esa yashiriladi. Klasslar ham shunday quriladi.", first="k", m="Murakkab narsani oddiy qilib ko'rsatish!", mm="wow")],
 "c_generic": [dict(m="int lar uchun ham, double lar uchun ham bir xil 'kattasi' funksiyasini yozdim...", mm="sad"),
               dict(k="Generic dasturlashda bitta universal funksiya yozasan — u istalgan tur bilan ishlaydi. Xuddi istalgan narsa sig'adigan sehrli quti!", first="k", prop=p_box_any, m="Bir marta yoz — hamma uchun ishlat!", mm="happy")],
 "c_this": [dict(m="Klass ichidagi funksiya qaysi obyekt uchun chaqirilganini qanday biladi?", mm="think", prop=p_mirror),
            dict(k="Har bir obyektda yashirin 'this' ko'rsatkichi bor — u 'men'ni bildiradi. Xuddi ko'zguga qarab 'bu menman' deganingdek!", first="k", m="'this' — bu 'men' degani!", mm="wow")],
 "c_static": [dict(m="Nechta o'quvchi obyekti yaratilganini qanday sanayman?", mm="think"),
              dict(k="static a'zo ishlat! U sinf doskasidagi yozuv kabi — barcha obyektlar uchun bitta umumiy, hamma uni ko'radi va o'zgartiradi.", first="k", prop=p_board, m="Hamma uchun bitta hisoblagich!", mm="happy")],
 "c_opover": [dict(m="Ikkita sonni + bilan qo'shaman. Ikkita vektorni ham + bilan qo'shsa bo'ladimi?", mm="think"),
              dict(k="Bo'ladi! Operatorlarni qayta yuklab, + ga o'z klassing bilan ishlashni o'rgatasan.", first="k", prop=p_plus_vec, m="Operatorlarga yangi narsa o'rgatsa bo'lar ekan!", mm="wow")],
 "c_friend": [dict(m="private ma'lumotlarni hech kim ko'ra olmaydi-ku. Istisno yo'qmi?", mm="think", prop=p_key),
              dict(k="Bor! Klass ishonchli funksiyani 'do'st' (friend) deb e'lon qilsa, unga uy kalitini bergandek bo'ladi — u ichkariga kira oladi.", first="k", m="Faqat eng yaqin do'stlarga kalit beraman!", mm="happy")],
 "c_dynmem": [dict(m="Nechta o'quvchi bo'lishini oldindan bilmasam, massiv o'lchamini qanday tanlayman?", mm="think"),
              dict(k="Dinamik xotira! Dastur ishlayotganda 'new' bilan kerakli joyni olasan, keyin 'delete' bilan qaytarasan — shar puflagandek.", first="k", prop=p_balloon, m="Kerak bo'lganda kattalashtir!", mm="wow")],
 "c_dynmembers": [dict(m="Klass ichida o'lchami o'zgaradigan ro'yxat saqlasa bo'ladimi?", mm="think"),
                  dict(k="Bo'ladi, lekin ehtiyot bo'l: obyekt nusxalanganda va o'chirilganda xotira bilan nima bo'lishini o'zing hal qilishing kerak.", first="k", prop=p_balloon, m="Katta kuch — katta mas'uliyat!", mm="happy")],
 "c_inherit": [dict(m="Mushuk, it, qush — hammasining ismi, yoshi bor va hammasi ovqat yeydi. Uch marta bir xil kod yozamanmi?", mm="think", fs=12),
               dict(k="Merosxo'rlik ishlat! Umumiy narsalarni 'Hayvon' klassiga yoz, qolganlari undan meros oladi — xuddi bolalar ota-onadan meros olgandek.", first="k", prop=p_family, m="Kod bir marta yoziladi!", mm="wow")],
 "c_typeconv": [dict(m="Hayvon ko'rsatkichi aslida it obyektini ko'rsatayotganini qanday bilaman?", mm="think", prop=p_magnifier),
                dict(k="dynamic_cast bilan tekshirasan! U lupa kabi: 'bu haqiqatan itmi?' deb so'raydi va javobga qarab xavfsiz aylantiradi.", first="k", m="Detektivga o'xshayman!", mm="happy")],
 "c_poly": [dict(m="Hamma hayvonga 'ovoz chiqar' desam, har biri o'z ovozini chiqaradimi?", mm="think"),
            dict(k="Ha! Bu polimorfizm — 'ko'p shakllilik'. Buyruq bitta, lekin har bir obyekt uni o'zicha bajaradi.", first="k", prop=p_animals_sound, m="Miyov! Vov! Muu! Zo'r!", mm="wow", arm="up")],
 "c_abstract": [dict(m="'Shakl' ning yuzini qanday hisoblayman? U qanday shakl o'zi?", mm="think", prop=p_shape_q),
                dict(k="To'g'ri savol! 'Shakl' — abstrakt tushuncha, undan obyekt yasab bo'lmaydi. U faqat qoida beradi: 'har bir shakl yuzani hisoblay olishi kerak'.", first="k", m="Qoida bor, lekin aniq shakl yo'q!", mm="wow")],
 "c_multi": [dict(m="O'rdak ham uchadi, ham suzadi. U ikkita klassdan meros ola oladimi?", mm="think", prop=p_duck),
             dict(k="C++ da ola oladi! Bu ko'plik merosxo'rlik. Lekin ehtiyot bo'l — ba'zan chalkashliklar bo'lishi mumkin.", first="k", m="Uchuvchi + suzuvchi = o'rdak!", mm="happy")],
 "c_templates": [dict(m="Butun sonlar uchun ham, satrlar uchun ham bir xil 'Quti' klassini yozmoqchiman.", mm="think"),
                 dict(k="Shablon (template) ishlat — u muhr kabi: bitta muhr bilan xohlagancha turdagi klass yoki funksiya 'bosib chiqarasan'.", first="k", prop=p_stamp, m="Muhr bilan kod yasash!", mm="wow")],
 "c_exceptions": [dict(m="Foydalanuvchi nolga bo'lsa, dasturim qulab tushadi!", mm="sad"),
                  dict(k="Istisnolarni ushla! 'try' ichida xavfli ish qilasan, xato bo'lsa 'throw' tashlaydi, 'catch' esa uni xavfsizlik to'ri kabi ushlab oladi.", first="k", prop=p_net, m="Endi dasturim qulamaydi!", mm="happy", arm="up")],
 "c_files": [dict(m="Dasturni yopsam, kiritgan barcha ma'lumotlarim yo'qolib ketadi...", mm="sad"),
             dict(k="Ularni faylga yoz! Fayl — kompyuterdagi kundalik daftar: dastur yopilsa ham ma'lumot saqlanib qoladi.", first="k", prop=p_diary, m="Endi o'yin rekordlarimni saqlayman!", mm="wow")],
}
for k, v in C.items():
    comic(k + ".png", v)
print("done", len(C))
