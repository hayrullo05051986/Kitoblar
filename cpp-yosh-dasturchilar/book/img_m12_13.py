from comic import *

# ============ diagrams ============
# STL family
fig, ax = canvas(11, 4.2)
box(ax, 4.0, 3.3, 3.0, 0.75, "STL konteynerlari", fc=PAL[0], ec=PAL[0], color="white", bold=True, fs=12)
groups = [("Ketma-ket", ["vector", "list", "deque", "array"], 1),
          ("Assotsiativ\n(saralangan)", ["set", "multiset", "map", "multimap"], 2),
          ("Adapterlar", ["stack", "queue", "priority_queue"], 4)]
for gi, (g, items, c) in enumerate(groups):
    x = 0.3 + gi * 3.7
    box(ax, x, 2.15, 3.3, 0.8, g, fc=LIGHT[c], ec=PAL[c], fs=11, bold=True)
    arrow(ax, 5.5, 3.28, x + 1.65, 2.98, lw=1.5, ms=12)
    for k, it in enumerate(items):
        box(ax, x + 0.15 + (k % 2) * 1.55, 1.2 - (k // 2) * 0.62, 1.45, 0.5, it, fc="white", ec=PAL[c], fs=9.5, mono=True, bold=True)
save(fig, "m12_family.png")

# vector: train with wagons
fig, ax = canvas(10, 3.0)
vals = [5, 3, 8, 1, 9]
for i, v in enumerate(vals):
    box(ax, 0.4 + i * 1.5, 1.0, 1.3, 1.0, str(v), fc=LIGHT[i], ec=PAL[i], fs=18, bold=True, mono=True)
    for wx in (0.3, 1.0):
        ax.add_patch(Circle((0.4 + i * 1.5 + wx, 0.9), 0.14, fc="#343A40"))
    text(ax, 1.05 + i * 1.5, 2.25, f"[{i}]", fs=10, mono=True, color="#868E96")
box(ax, 8.0, 1.0, 1.3, 1.0, "+", fc="white", ec="#ADB5BD", fs=22, bold=True, color="#ADB5BD", lw=2)
text(ax, 8.65, 0.45, "push_back()", fs=10, mono=True, color=PAL[2], bold=True)
text(ax, 4.0, 0.3, "vector — kerak bo'lsa yangi vagon qo'shiladigan poyezd", fs=11, color="#5A6270")
save(fig, "m12_vector.png")

# list: chain
fig, ax = canvas(10, 2.6)
for i, v in enumerate(["A", "B", "C", "D"]):
    x = 0.4 + i * 2.4
    box(ax, x, 0.9, 1.2, 0.9, v, fc=LIGHT[i * 2], ec=PAL[i * 2], fs=16, bold=True)
    if i < 3:
        arrow(ax, x + 1.25, 1.5, x + 2.35, 1.5, color=PAL[2], lw=2)
        arrow(ax, x + 2.35, 1.2, x + 1.25, 1.2, color=PAL[4], lw=2)
text(ax, 5.0, 0.35, "list — har bir element qo'shnilarining manzilini biladi (zanjir)", fs=11, color="#5A6270")
save(fig, "m12_list.png")

# deque
fig, ax = canvas(10, 2.6)
for i, v in enumerate([4, 7, 2, 9]):
    box(ax, 2.6 + i * 1.2, 0.9, 1.1, 0.9, str(v), fc=LIGHT[1], ec=PAL[1], fs=16, bold=True, mono=True)
arrow(ax, 0.6, 1.35, 2.5, 1.35, color=PAL[2], lw=2.5); text(ax, 1.5, 1.75, "push_front", fs=10, mono=True, color=PAL[2], bold=True)
arrow(ax, 9.4, 1.35, 7.5, 1.35, color=PAL[2], lw=2.5); text(ax, 8.5, 1.75, "push_back", fs=10, mono=True, color=PAL[2], bold=True)
text(ax, 5.0, 0.35, "deque — ikkala uchidan ham qo'shish va olish mumkin", fs=11, color="#5A6270")
save(fig, "m12_deque.png")

# set: sorted unique balls
fig, ax = canvas(10, 2.8)
text(ax, 2.2, 2.4, "kiritildi: 5 2 8 2 5 1", fs=11, mono=True)
arrow(ax, 4.3, 2.4, 5.0, 2.4)
for i, v in enumerate([1, 2, 5, 8]):
    ax.add_patch(Circle((5.6 + i * 1.05, 1.4), 0.42, fc=LIGHT[i], ec=PAL[i], lw=2.5))
    text(ax, 5.6 + i * 1.05, 1.4, str(v), fs=16, bold=True)
text(ax, 7.2, 0.5, "set: takrorlanmas va saralangan", fs=11, color="#5A6270", bold=True)
save(fig, "m12_set.png")

# map: dictionary
fig, ax = canvas(10, 3.2)
pairs = [("\"olma\"", "8000"), ("\"banan\"", "15000"), ("\"nok\"", "12000")]
text(ax, 2.3, 2.85, "kalit", fs=12, bold=True, color=PAL[0]); text(ax, 6.2, 2.85, "qiymat", fs=12, bold=True, color=PAL[2])
for i, (k, v) in enumerate(sorted(pairs)):
    y = 2.0 - i * 0.75
    box(ax, 1.0, y, 2.6, 0.6, k, fc=LIGHT[0], ec=PAL[0], fs=12, mono=True, bold=True)
    arrow(ax, 3.7, y + 0.3, 4.8, y + 0.3)
    box(ax, 4.9, y, 2.6, 0.6, v, fc=LIGHT[2], ec=PAL[2], fs=12, mono=True, bold=True)
text(ax, 8.7, 1.4, "map —\nlug'at\nkabi", fs=12, color="#5A6270", bold=True)
save(fig, "m12_map.png")

# stack: plates
fig, ax = canvas(10, 3.4)
for i, v in enumerate([10, 20, 30, 40]):
    ax.add_patch(Ellipse((3.0, 0.5 + i * 0.6), 2.6, 0.5, fc=LIGHT[i], ec=PAL[i], lw=2))
    text(ax, 3.0, 0.5 + i * 0.6, str(v), fs=12, bold=True)
arrow(ax, 5.2, 2.3, 4.5, 2.3, color=PAL[2], lw=2.5); text(ax, 6.4, 2.3, "push / pop", fs=12, mono=True, bold=True, color=PAL[2])
text(ax, 6.8, 1.2, "faqat eng ustidagisi\nbilan ishlanadi (LIFO)", fs=11, color="#5A6270")
save(fig, "m12_stack.png")

# queue: line of people
fig, ax = canvas(10, 3.0)
for i in range(5):
    x = 2.0 + i * 1.3
    ax.add_patch(Circle((x, 1.95), 0.25, fc=SKIN, ec="#1F2328"))
    box(ax, x - 0.3, 0.8, 0.6, 0.9, str(i + 1), fc=LIGHT[i], ec=PAL[i], fs=12, bold=True)
box(ax, 0.2, 0.8, 1.2, 1.5, "kassa", fc="#343A40", ec="#1F2328", fs=10, color="white", bold=True)
text(ax, 2.0, 0.4, "front (oldi)", fs=10, color=PAL[3], bold=True)
text(ax, 7.2, 0.4, "back (orqasi)", fs=10, color=PAL[2], bold=True)
text(ax, 5.0, 2.7, "queue — birinchi kelgan birinchi ketadi (FIFO)", fs=11, color="#5A6270", bold=True)
save(fig, "m12_queue.png")

# priority queue: hospital
fig, ax = canvas(10, 3.0)
for i, (n, p, c) in enumerate([("Ali", 9, 3), ("Vali", 5, 1), ("Laylo", 2, 2)]):
    box(ax, 0.5 + i * 2.6, 0.9, 2.3, 1.1, f"{n}\nmuhimlik: {p}", fc=LIGHT[c], ec=PAL[c], fs=11, bold=True)
text(ax, 4.2, 2.5, "priority_queue — eng muhimi har doim oldinda", fs=12, bold=True, color="#5A6270")
box(ax, 8.4, 0.9, 1.3, 1.1, "top()\n= Ali", fc="white", ec=PAL[3], fs=10, mono=True, bold=True)
save(fig, "m12_pq.png")

# pair
fig, ax = canvas(10, 2.4)
box(ax, 2.0, 0.6, 6.0, 1.3, "", fc="#F8F9FA", ec="#495057", lw=2)
box(ax, 2.3, 0.8, 2.6, 0.9, "first: \"Malika\"", fc=LIGHT[0], ec=PAL[0], fs=11, mono=True, bold=True)
box(ax, 5.1, 0.8, 2.6, 0.9, "second: 98", fc=LIGHT[2], ec=PAL[2], fs=11, mono=True, bold=True)
text(ax, 5.0, 2.15, "pair<string, int> — ikki qiymatli quti", fs=12, bold=True)
save(fig, "m12_pair.png")

# lambda anatomy
fig, ax = canvas(10, 2.8)
parts = [("[ ]", "ushlash", 4), ("(int x)", "parametrlar", 0), ("-> int", "qaytish turi", 1), ("{ return x*x; }", "tana", 2)]
x = 0.5
for t, d, c in parts:
    w = 0.6 + len(t) * 0.17
    box(ax, x, 1.2, w, 0.8, t, fc=LIGHT[c], ec=PAL[c], fs=12, mono=True, bold=True)
    text(ax, x + w / 2, 0.8, d, fs=10, color=PAL[c], bold=True)
    x += w + 0.2
text(ax, 5.0, 2.45, "Lambda ifodaning qismlari", fs=13, bold=True)
save(fig, "m13_lambda.png")

# lvalue rvalue
fig, ax = canvas(10, 2.8)
box(ax, 0.6, 0.8, 3.0, 1.2, "x\n(lvalue — nomi va\nmanzili bor)", fc=LIGHT[0], ec=PAL[0], fs=10.5, bold=True)
text(ax, 4.2, 1.4, "=", fs=26, bold=True)
box(ax, 4.9, 0.8, 4.4, 1.2, "5 + 3\n(rvalue — vaqtinchalik,\nnomsiz qiymat)", fc=LIGHT[1], ec=PAL[1], fs=10.5, bold=True)
text(ax, 5.0, 2.45, "Chap tomon — joy, o'ng tomon — qiymat", fs=12, bold=True)
save(fig, "m13_lrvalue.png")

# threads
fig, ax = canvas(10, 3.0)
for i, (n, c) in enumerate([("1-oqim: musiqa", 0), ("2-oqim: grafika", 2), ("3-oqim: tugmalar", 4)]):
    y = 2.2 - i * 0.8
    text(ax, 1.4, y, n, fs=10.5, bold=True, color=PAL[c])
    for k in range(6):
        box(ax, 3.0 + k * 1.1 + (i * 0.25), y - 0.22, 0.85, 0.44, "", fc=LIGHT[c], ec=PAL[c], r=0.06)
text(ax, 6.2, 0.15, "vaqt →    oqimlar bir vaqtda (parallel) ishlaydi", fs=10, color="#5A6270")
save(fig, "m13_threads.png")

# uses of C++
fig, ax = canvas(11, 3.4)
uses = [("O'yinlar", 3), ("Brauzerlar", 0), ("Operatsion\ntizimlar", 2), ("Robotlar", 4), ("Kosmos", 5), ("Moliya", 1), ("Ma'lumotlar\nbazalari", 6), ("Sun'iy\nintellekt", 7)]
for i, (u, c) in enumerate(uses):
    r, col = divmod(i, 4)
    box(ax, 0.3 + col * 2.7, 1.8 - r * 1.5, 2.4, 1.2, u, fc=LIGHT[c], ec=PAL[c], fs=12, bold=True)
save(fig, "m13_uses.png")

# ============ comics ============
def p_toolbelt(ax, x, y):
    for i, (t, c) in enumerate([("vector", 1), ("set", 2), ("map", 0), ("stack", 4)]):
        box(ax, x + 0.05 + (i % 2) * 1.05, y + 0.25 + (i // 2) * 0.65, 0.95, 0.5, t, fc=LIGHT[c], ec=PAL[c], fs=8.5, mono=True, bold=True)

def p_train(ax, x, y):
    for i in range(3):
        box(ax, x + 0.05 + i * 0.7, y + 0.5, 0.6, 0.5, str(i), fc=LIGHT[i], ec=PAL[i], fs=9, bold=True)
        ax.add_patch(Circle((x + 0.2 + i * 0.7, y + 0.45), 0.07, fc="#343A40"))
        ax.add_patch(Circle((x + 0.5 + i * 0.7, y + 0.45), 0.07, fc="#343A40"))

def p_chain(ax, x, y):
    for i in range(4):
        ax.add_patch(Ellipse((x + 0.3 + i * 0.45, y + 0.9), 0.55, 0.32, fc="none", ec="#868E96", lw=3))

def p_twodoors(ax, x, y):
    box(ax, x + 0.5, y + 0.6, 1.1, 0.5, "", fc=LIGHT[1], ec=PAL[1])
    arrow(ax, x + 0.05, y + 0.85, x + 0.45, y + 0.85, ms=10, color=PAL[2])
    arrow(ax, x + 2.05, y + 0.85, x + 1.65, y + 0.85, ms=10, color=PAL[2])

def p_cards(ax, x, y):
    box(ax, x + 0.3, y + 0.4, 0.7, 0.9, "Ism", fc=LIGHT[0], ec=PAL[0], fs=9, bold=True)
    box(ax, x + 1.1, y + 0.4, 0.7, 0.9, "Ball", fc=LIGHT[2], ec=PAL[2], fs=9, bold=True)

def p_stamps(ax, x, y):
    for i, v in enumerate([1, 3, 7]):
        ax.add_patch(Circle((x + 0.45 + i * 0.6, y + 0.9), 0.25, fc=LIGHT[i], ec=PAL[i], lw=2))
        ax.text(x + 0.45 + i * 0.6, y + 0.9, str(v), fontsize=10, ha="center", va="center", fontweight="bold")

def p_dice(ax, x, y):
    for i, v in enumerate([3, 3, 5]):
        box(ax, x + 0.2 + i * 0.6, y + 0.6, 0.5, 0.5, str(v), fc="white", ec="#1F2328", fs=11, bold=True, r=0.08)

def p_dict(ax, x, y):
    box(ax, x + 0.3, y + 0.2, 1.5, 1.3, "LUG'AT\nolma → apple\nkitob → book", fc="#FFF4D6", ec=PAL[1], fs=7.5, bold=True)

def p_phonebook(ax, x, y):
    box(ax, x + 0.3, y + 0.2, 1.5, 1.3, "Ali → 901..\nAli → 933..\nVali → 977..", fc=LIGHT[5], ec=PAL[5], fs=7.5, mono=True)

def p_plates(ax, x, y):
    for i in range(4):
        ax.add_patch(Ellipse((x + 1.05, y + 0.35 + i * 0.25), 1.3, 0.25, fc=LIGHT[i], ec=PAL[i], lw=1.5))

def p_line(ax, x, y):
    for i in range(4):
        ax.add_patch(Circle((x + 0.3 + i * 0.5, y + 1.15), 0.14, fc=SKIN, ec="#1F2328"))
        box(ax, x + 0.15 + i * 0.5, y + 0.4, 0.3, 0.6, "", fc=LIGHT[i], ec=PAL[i], r=0.05)

def p_ambulance(ax, x, y):
    box(ax, x + 0.2, y + 0.45, 1.7, 0.8, "", fc="white", ec="#1F2328", r=0.12)
    ax.add_patch(Rectangle((x + 0.95, y + 0.6), 0.2, 0.5, fc=PAL[3])); ax.add_patch(Rectangle((x + 0.8, y + 0.75), 0.5, 0.2, fc=PAL[3]))
    for wx in (0.55, 1.55):
        ax.add_patch(Circle((x + wx, y + 0.42), 0.15, fc="#343A40"))

def p_lambda(ax, x, y):
    ax.text(x + 1.05, y + 0.9, "[ ](x){...}", fontsize=12, ha="center", va="center", fontweight="bold", family="DejaVu Sans Mono", color=PAL[4])

def p_move(ax, x, y):
    box(ax, x + 0.05, y + 0.5, 0.8, 0.7, "", fc="#E9C46A", ec="#8D6E63", r=0.03)
    arrow(ax, x + 0.9, y + 0.85, x + 1.2, y + 0.85, ms=10)
    box(ax, x + 1.25, y + 0.5, 0.8, 0.7, "", fc="#F1F3F5", ec="#ADB5BD", r=0.03)
    ax.text(x + 1.05, y + 1.4, "move", fontsize=10, ha="center", fontweight="bold", family="DejaVu Sans Mono")

def p_cooks(ax, x, y):
    for i, c in enumerate([0, 2, 4]):
        ax.add_patch(Circle((x + 0.4 + i * 0.65, y + 1.1), 0.18, fc=SKIN, ec="#1F2328"))
        ax.add_patch(Rectangle((x + 0.28 + i * 0.65, y + 1.25), 0.24, 0.18, fc="white", ec="#1F2328"))
        box(ax, x + 0.22 + i * 0.65, y + 0.35, 0.36, 0.55, "", fc=LIGHT[c], ec=PAL[c], r=0.05)

def p_newop(ax, x, y):
    box(ax, x + 0.2, y + 0.4, 1.7, 0.9, "new", fc=PAL[2], ec="#1F2328", fs=14, bold=True, color="white", mono=True)

def p_globe(ax, x, y):
    ax.add_patch(Circle((x + 1.05, y + 0.85), 0.6, fc="#74C0FC", ec="#1F2328"))
    ax.add_patch(Ellipse((x + 0.85, y + 1.0), 0.45, 0.3, fc="#69DB7C", ec="none"))
    ax.add_patch(Ellipse((x + 1.3, y + 0.65), 0.35, 0.25, fc="#69DB7C", ec="none"))
    ax.text(x + 1.05, y + 0.85, "C++", fontsize=10, ha="center", va="center", fontweight="bold")

C = {
 "c_containers": [dict(m="Ro'yxatlar, lug'atlar, navbatlar... Hammasini o'zim yozishim kerakmi?", mm="think", prop=p_toolbelt),
                  dict(k="Yo'q! STL — tayyor konteynerlar to'plami. Har bir vazifa uchun mos 'quti' bor: vector, set, map, stack...", first="k", m="Asboblar qutisi kabi!", mm="wow")],
 "c_vector": [dict(m="Massiv o'lchamini oldindan bilishim shart edi. Bu noqulay!", mm="sad"),
              dict(k="vector ishlat! U poyezd kabi: kerak bo'lsa yangi vagon qo'shiladi. O'lchamini o'zi boshqaradi.", first="k", prop=p_train, m="Cheksiz poyezd!", mm="happy", arm="up")],
 "c_list": [dict(m="vector ning o'rtasiga element qo'shsam, qolganlari surilishi kerak ekan...", mm="think"),
            dict(k="list da unday emas! U zanjir kabi: o'rtaga yangi halqa qo'shish uchun faqat ikki qo'shni halqani ulash kifoya.", first="k", prop=p_chain, m="Zanjirni ochib, yangi halqa qo'shaman!", mm="wow")],
 "c_deque": [dict(m="Ro'yxatning boshiga ham, oxiriga ham tez qo'shadigan narsa bormi?", mm="think", prop=p_twodoors),
             dict(k="deque — ikki eshikli vagon! Oldidan ham, orqasidan ham kirish va chiqish mumkin.", first="k", m="Ikki tomonlama navbat!", mm="happy")],
 "c_pair": [dict(m="O'quvchining ismi va ballini birga saqlamoqchiman. Klass yozishim kerakmi?", mm="think", prop=p_cards),
            dict(k="Oddiy holat uchun pair yetarli! U ikki qiymatni bitta qutiga joylaydi: first va second.", first="k", m="Juft-juft saqlash oson ekan!", mm="happy")],
 "c_set": [dict(m="Kolleksiyamdagi markalarning takrorlanmasligini qanday ta'minlayman?", mm="think", prop=p_stamps),
           dict(k="set ishlat! U bir xil elementni ikki marta saqlamaydi va hammasini o'zi tartib bilan joylaydi.", first="k", m="Takrorlanishsiz va tartibli!", mm="wow")],
 "c_multiset": [dict(m="Zar tashlash natijalarini saqlayman. Bir xil sonlar ham ko'p chiqadi-ku!", mm="think", prop=p_dice),
                dict(k="Unda multiset kerak — u set ga o'xshab saralaydi, lekin takrorlanishlarga ruxsat beradi.", first="k", m="Har bir uchtani ham saqlaydi!", mm="happy")],
 "c_map": [dict(m="So'z yozsam, tarjimasini topadigan dastur qilmoqchiman.", mm="think"),
           dict(k="map — haqiqiy lug'at! Har bir kalitga (so'zga) bitta qiymat (tarjima) mos keladi va qidirish juda tez.", first="k", prop=p_dict, m="O'z lug'atimni yarataman!", mm="wow", arm="up")],
 "c_multimap": [dict(m="Do'stimning ikkita telefon raqami bor. map da faqat bittasini saqlay olaman...", mm="sad"),
                dict(k="multimap da bitta kalitga bir nechta qiymat bog'lash mumkin — xuddi telefon kitobchasidagidek!", first="k", prop=p_phonebook, m="Hamma raqamlar saqlanadi!", mm="happy")],
 "c_stack": [dict(m="Likopchalarni yuvayotganda doim eng ustidagisini olaman.", mm="happy", prop=p_plates),
             dict(k="Bu stek! Oxirgi qo'yilgan birinchi olinadi. Matn muharriridagi 'bekor qilish' (Ctrl+Z) ham shunday ishlaydi.", first="k", m="Ctrl+Z ham stek ekan!", mm="wow")],
 "c_queue": [dict(m="Do'kondagi navbatda birinchi kelgan birinchi xizmat oladi.", mm="happy", prop=p_line),
             dict(k="queue aynan shunday ishlaydi! Printerga yuborilgan hujjatlar ham navbat bilan chop etiladi.", first="k", m="Adolatli navbat!", mm="wow")],
 "c_pq": [dict(m="Shifoxonada nega og'ir bemor navbatsiz kiradi?", mm="think", prop=p_ambulance),
          dict(k="Chunki u yerda navbat muhimlik bo'yicha! priority_queue ham har doim eng muhim elementni birinchi beradi.", first="k", m="Muhimlik navbati!", mm="wow")],
 "c_lambdafx": [dict(m="sort ga bitta kichik taqqoslash funksiyasi berish uchun alohida funksiya yozishim kerakmi?", mm="think"),
                dict(k="Lambda ishlat! Bu nomsiz, kichik funksiya — uni kerakli joyning o'zida yozasan.", first="k", prop=p_lambda, m="Bir qatorlik funksiya!", mm="wow")],
 "c_lrvalue": [dict(m="Katta qutini ko'chirish uchun undagi hamma narsani nusxalash kerakmi?", mm="think", prop=p_move),
               dict(k="Yo'q! Qutining o'zini ko'chirib qo'yish tezroq. rvalue va 'move' aynan shuni qiladi — nusxalash o'rniga ko'chiradi.", first="k", m="Ko'chirish nusxalashdan tez!", mm="happy")],
 "c_concurrency": [dict(m="Uchta oshpaz bir vaqtda ishlasa, ovqat tezroq tayyor bo'ladimi?", mm="think", prop=p_cooks),
                   dict(k="Ha! Dasturlar ham bir vaqtda bir nechta ishni bajara oladi — bu oqimlar (thread). Faqat ular bir-biriga xalaqit bermasligi kerak.", first="k", m="Jamoa bo'lib ishlash!", mm="wow")],
 "c_newop": [dict(m="new operatorini ancha oldin o'rgangan edik-ku. Yana nimasi qoldi?", mm="think"),
             dict(k="Uning ichki sirlari! new aslida ikki ish qiladi: xotira oladi va konstruktorni chaqiradi. Buni bilish juda foydali.", first="k", prop=p_newop, m="Sehrni ochamiz!", mm="wow")],
 "c_uses": [dict(m="C++ ni o'rganib bo'ldim! Endi u bilan nima qila olaman?", mm="happy", arm="up"),
            dict(k="Juda ko'p narsa! O'yinlar, robotlar, brauzerlar, kosmik kemalar... Butun dunyo C++ da ishlaydi!", first="k", prop=p_globe, m="Men kelajakning dasturchisiman!", mm="wow", arm="up")],
}
for k, v in C.items():
    comic(k + ".png", v)
print("ok", len(C))
