from comic import *

def mono(ax, x, y, s, fs=11, color="#1F2328", **kw):
    ax.text(x, y, s, fontsize=fs, family="DejaVu Sans Mono", fontweight="bold", color=color, **kw)

# ---------- props ----------
def p_history(ax, x, y):
    for i, (yr, c) in enumerate([("1972\nC", 3), ("1983\nC++", 0)]):
        box(ax, x + 0.1 + i * 1.05, y + 0.35, 0.9, 0.9, yr, fc=LIGHT[c], ec=PAL[c], fs=10, bold=True)
    arrow(ax, x + 1.0, y + 0.8, x + 1.15, y + 0.8, ms=10)

def p_plus(ax, x, y):
    box(ax, x + 0.15, y + 0.4, 0.8, 0.8, "C", fc=LIGHT[3], ec=PAL[3], fs=20, bold=True)
    mono(ax, x + 1.05, y + 0.65, "++", fs=18, color=PAL[2])
    box(ax, x + 0.15 + 0.0, y + 1.3, 1.6, 0.0, "", fc="white", ec="white")

def p_two_books(ax, x, y):
    box(ax, x + 0.1, y + 0.3, 0.85, 1.1, "C", fc=PAL[3], ec="#1F2328", fs=18, bold=True, color="white", r=0.05)
    box(ax, x + 1.1, y + 0.3, 0.85, 1.25, "C++", fc=PAL[0], ec="#1F2328", fs=14, bold=True, color="white", r=0.05)

def p_translator(ax, x, y):
    box(ax, x + 0.0, y + 0.9, 0.9, 0.55, "cout", fc="#F6F8FA", ec="#ADB5BD", fs=9, mono=True)
    arrow(ax, x + 0.95, y + 1.17, x + 1.2, y + 1.17, ms=10)
    box(ax, x + 1.22, y + 0.9, 0.95, 0.55, "0101", fc="#1E1E1E", ec="#495057", fs=9, mono=True, color="#7CFC00")
    box(ax, x + 0.4, y + 0.2, 1.3, 0.55, "kompilyator", fc=LIGHT[1], ec=PAL[1], fs=8, bold=True)

def p_sticky(ax, x, y):
    box(ax, x + 0.05, y + 0.25, 1.4, 1.3, "", fc="#F6F8FA", ec="#ADB5BD", r=0.05)
    for i in range(4):
        ax.plot([x + 0.15, x + 1.2], [y + 1.3 - i * 0.28, y + 1.3 - i * 0.28], color="#ADB5BD", lw=2)
    ax.add_patch(Polygon([[x + 1.2, y + 0.9], [x + 2.05, y + 0.9], [x + 2.05, y + 1.6], [x + 1.2, y + 1.6]], fc="#FFE066", ec="#C9A000", lw=1.2))
    ax.text(x + 1.62, y + 1.25, "// eslatma", fontsize=7.5, ha="center", family="DejaVu Sans Mono")

def p_toolbox(ax, x, y):
    box(ax, x + 0.2, y + 0.3, 1.7, 0.9, "<cmath>", fc=PAL[1], ec="#1F2328", fs=11, bold=True, color="white", mono=True)
    ax.plot([x + 0.75, x + 0.75, x + 1.35, x + 1.35], [y + 1.2, y + 1.5, y + 1.5, y + 1.2], color="#1F2328", lw=3)

def p_two_ali(ax, x, y):
    for i, (n, c) in enumerate([("1-maktab", 0), ("2-maktab", 2)]):
        box(ax, x + i * 1.08, y + 0.3, 1.0, 1.2, n + "\n\nAli", fc=LIGHT[c], ec=PAL[c], fs=8.5, bold=True)

def p_messy(ax, x, y):
    box(ax, x + 0.0, y + 0.3, 1.0, 1.2, "", fc="#FFE3E3", ec=PAL[3])
    for k in range(6):
        ax.plot([x + 0.1 + (k * 0.13) % 0.8, x + 0.4 + (k * 0.29) % 0.5], [y + 0.45 + k * 0.17, y + 0.6 + (k * 0.23) % 0.8], color=PAL[3], lw=1.5)
    box(ax, x + 1.15, y + 0.3, 1.0, 1.2, "", fc="#E3F7EA", ec=PAL[2])
    for k in range(5):
        ax.plot([x + 1.25 + (0.15 if k in (1, 2, 3) else 0), x + 2.0], [y + 1.3 - k * 0.2] * 2, color=PAL[2], lw=2)

def p_recipe(ax, x, y):
    box(ax, x + 0.2, y + 0.2, 1.7, 1.4, "1. Suvni qaynat;\n2. Choy sol;\n3. Kut;", fc="#FFF9DB", ec=PAL[1], fs=8.5, mono=True)

def p_jars(ax, x, y):
    for i, (lab, c, h) in enumerate([("int", 0, 1.0), ("double", 2, 1.25), ("char", 1, 0.7), ("bool", 3, 0.6)]):
        ax.add_patch(FancyBboxPatch((x + i * 0.53, y + 0.2), 0.45, h, boxstyle="round,pad=0,rounding_size=0.08", fc=LIGHT[c], ec=PAL[c], lw=2))
        ax.add_patch(Rectangle((x + i * 0.53 + 0.05, y + 0.2 + h), 0.35, 0.1, fc=PAL[c]))
        ax.text(x + i * 0.53 + 0.225, y + 0.35, lab, rotation=90, fontsize=7.5, ha="center", va="bottom", family="DejaVu Sans Mono", fontweight="bold")

def p_sizes(ax, x, y):
    for i, (t, c) in enumerate([("S", 0), ("M", 1), ("L", 2), ("XL", 3)]):
        w = 0.32 + i * 0.1
        box(ax, x + 0.05 + sum(0.42 + k * 0.1 for k in range(i)), y + 0.3, w, 0.5 + i * 0.25, t, fc=LIGHT[c], ec=PAL[c], fs=9, bold=True)

def p_lock(ax, x, y):
    box(ax, x + 0.3, y + 0.25, 1.4, 1.1, "7", fc="#FFF4D6", ec=PAL[1], fs=22, bold=True, mono=True)
    ax.add_patch(FancyBboxPatch((x + 1.45, y + 0.15), 0.5, 0.42, boxstyle="round,pad=0,rounding_size=0.06", fc="#868E96", ec="#1F2328"))
    ax.add_patch(Arc((x + 1.7, y + 0.57), 0.3, 0.4, theta1=0, theta2=180, color="#1F2328", lw=3))

def p_reserved(ax, x, y):
    for i, w in enumerate(["if", "int", "for"]):
        box(ax, x + 0.05 + i * 0.7, y + 0.6, 0.62, 0.5, w, fc="#FFE3E3", ec=PAL[3], fs=9, mono=True, bold=True)
    ax.text(x + 1.05, y + 0.25, "BAND!", fontsize=11, ha="center", fontweight="bold", color=PAL[3])

def p_box(ax, x, y):
    box(ax, x + 0.4, y + 0.2, 1.3, 1.0, "12", fc=LIGHT[0], ec=PAL[0], fs=18, bold=True, mono=True)
    box(ax, x + 0.55, y + 1.1, 1.0, 0.38, "yosh", fc=PAL[0], ec=PAL[0], fs=9, bold=True, color="white", mono=True)

def p_gift(ax, x, y):
    box(ax, x + 0.45, y + 0.2, 1.2, 1.0, "", fc=PAL[7], ec="#1F2328", r=0.05)
    ax.add_patch(Rectangle((x + 0.98, y + 0.2), 0.14, 1.0, fc="#FFD43B"))
    ax.add_patch(Rectangle((x + 0.45, y + 0.65), 1.2, 0.14, fc="#FFD43B"))
    ax.text(x + 1.05, y + 1.35, "auto ?", fontsize=10, ha="center", fontweight="bold", family="DejaVu Sans Mono", color=PAL[4])

def p_letters(ax, x, y):
    for i, (ch, n) in enumerate([("A", "65"), ("B", "66"), ("C", "67")]):
        box(ax, x + 0.1 + i * 0.68, y + 0.75, 0.6, 0.6, ch, fc=LIGHT[i], ec=PAL[i], fs=14, bold=True)
        ax.text(x + 0.4 + i * 0.68, y + 0.45, n, fontsize=9, ha="center", family="DejaVu Sans Mono")

def p_bulbs(ax, x, y):
    for i, b in enumerate([1, 0, 1]):
        ax.add_patch(Circle((x + 0.4 + i * 0.65, y + 1.0), 0.27, fc="#FFD43B" if b else "#DEE2E6", ec="#1F2328", lw=1.5))
        ax.add_patch(Rectangle((x + 0.29 + i * 0.65, y + 0.58), 0.22, 0.15, fc="#868E96"))
        ax.text(x + 0.4 + i * 0.65, y + 0.3, str(b), fontsize=11, ha="center", fontweight="bold")

def p_glasses(ax, x, y):
    ax.add_patch(Polygon([[x + 0.2, y + 0.2], [x + 0.8, y + 0.2], [x + 0.9, y + 1.4], [x + 0.1, y + 1.4]], fc="white", ec="#1F2328", lw=1.5))
    ax.add_patch(Polygon([[x + 0.2, y + 0.2], [x + 0.8, y + 0.2], [x + 0.87, y + 1.1], [x + 0.13, y + 1.1]], fc=PAL[0], alpha=.7))
    ax.add_patch(Polygon([[x + 1.3, y + 0.2], [x + 1.7, y + 0.2], [x + 1.75, y + 0.75], [x + 1.25, y + 0.75]], fc=PAL[0], ec="#1F2328", lw=1.5, alpha=.8))
    ax.add_patch(Ellipse((x + 1.9, y + 0.25), 0.35, 0.1, fc=PAL[0], alpha=.6))

def p_calc(ax, x, y):
    box(ax, x + 0.45, y + 0.15, 1.2, 1.45, "", fc="#343A40", ec="#1F2328", r=0.12)
    box(ax, x + 0.55, y + 1.2, 1.0, 0.3, "5+3=8", fc="#C3FAE8", ec="none", fs=8, mono=True)
    for r in range(3):
        for c in range(3):
            ax.add_patch(Circle((x + 0.72 + c * 0.33, y + 0.38 + r * 0.27), 0.1, fc=["#ADB5BD", PAL[1], PAL[0]][c], ec="none"))

def p_tree(ax, x, y):
    for (a, b) in [((1.05, 1.4), (0.55, 0.85)), ((1.05, 1.4), (1.55, 0.85))]:
        ax.plot([x + a[0], x + b[0]], [y + a[1], y + b[1]], color="#868E96", lw=1.5)
    for (px, py, t, c) in [(1.05, 1.4, "*", 3), (0.55, 0.75, "2+3", 1), (1.55, 0.75, "4", 0)]:
        ax.add_patch(Circle((x + px, y + py), 0.25, fc=LIGHT[c], ec=PAL[c], lw=2)); ax.text(x + px, y + py, t, fontsize=8, ha="center", va="center", fontweight="bold")
    ax.text(x + 1.05, y + 0.25, "= 20", fontsize=11, ha="center", fontweight="bold", family="DejaVu Sans Mono")

def p_umbrella(ax, x, y):
    ax.add_patch(Wedge((x + 1.05, y + 0.95), 0.7, 0, 180, fc=PAL[0], ec="#1F2328"))
    ax.plot([x + 1.05, x + 1.05], [y + 0.95, y + 0.25], color="#1F2328", lw=2.5)
    ax.add_patch(Arc((x + 0.95, y + 0.25), 0.2, 0.2, theta1=180, theta2=360, color="#1F2328", lw=2.5))
    for k in range(5):
        ax.plot([x + 0.4 + k * 0.32, x + 0.35 + k * 0.32], [y + 1.75, y + 1.6], color=PAL[5], lw=2)

def p_laps(ax, x, y):
    ax.add_patch(Ellipse((x + 1.05, y + 0.9), 1.9, 1.2, fc="none", ec="#868E96", lw=6))
    ax.add_patch(Ellipse((x + 1.05, y + 0.9), 1.9, 1.2, fc="none", ec="white", lw=1, ls="--"))
    ax.text(x + 1.05, y + 0.9, "1, 2, 3\n...10", fontsize=9, ha="center", va="center", fontweight="bold", color=PAL[2])

def p_stop(ax, x, y):
    ax.add_patch(matplotlib.patches.RegularPolygon((x + 0.6, y + 0.9), 8, radius=0.5, orientation=0.3927, fc=PAL[3], ec="white", lw=2))
    ax.text(x + 0.6, y + 0.9, "break", fontsize=9, ha="center", va="center", fontweight="bold", color="white")
    ax.add_patch(FancyArrowPatch((x + 1.25, y + 0.6), (x + 2.0, y + 1.3), arrowstyle="-|>", mutation_scale=14, color=PAL[1], lw=2, connectionstyle="arc3,rad=-0.5"))
    ax.text(x + 1.6, y + 0.35, "continue", fontsize=8, ha="center", fontweight="bold", color="#C78A00")

C = {
 "c_history": [dict(m="Kodi, C++ ni kim o'ylab topgan? U doim bormidi?", mm="think"),
               dict(k="Yo'q! Uni 1979-yilda Bjarne Stroustrup degan olim C tilini yaxshilab yaratgan. Hamma narsaning boshlanishi bo'ladi!", m="Demak, C++ — C ning ukasi ekan-da!", first="k", prop=p_history, mm="wow")],
 "c_cvscpp": [dict(m="C va C++ — bir xil tilmi? Nomlari juda o'xshash-ku!", mm="think", prop=p_two_books),
              dict(k="Ular aka-ukaga o'xshaydi. C++ C ning deyarli hamma narsasini biladi, ustiga klasslar va boshqa ko'p yangi imkoniyatlarni qo'shgan.", first="k", m="Unda men C++ ni o'rgansam, C ni ham bilib olaman!", mm="happy", arm="up")],
 "c_setup": [dict(m="Men kompyuterga 'Salom' deb yozdim, lekin u tushunmadi!", mm="sad"),
             dict(k="Kompyuter faqat 0 va 1 ni tushunadi. Unga tarjimon — kompilyator kerak. U sening kodingni mashina tiliga o'giradi.", first="k", m="Xuddi ingliz tilidan o'zbekchaga tarjima qilgandek!", prop=p_translator, mm="wow")],
 "c_comments": [dict(m="Kecha yozgan kodimni bugun tushunmay qoldim...", mm="sad"),
                dict(k="Kodga izoh yozib qo'y! // dan keyingi yozuvni kompyuter o'qimaydi — u faqat odamlar uchun. Xuddi daftardagi stiker kabi.", first="k", prop=p_sticky, m="Zo'r, endi hamma narsani eslab qolaman!")],
 "c_headers": [dict(m="Ildiz chiqaradigan funksiyani o'zim yozishim kerakmi? Bu qiyin-ku!", mm="think"),
               dict(k="Shart emas! Tayyor 'asboblar qutisi' bor. #include <cmath> deb yozsang, sqrt() ishlatishga tayyor bo'ladi.", first="k", prop=p_toolbox, m="Xuddi qalamdonni ochgandek oson ekan!", mm="happy")],
 "c_namespace": [dict(m="Ikkita maktabda ham Ali ismli bola bor. Qaysi biri ekanini qanday bilaman?", mm="think", prop=p_two_ali),
                 dict(k="Maktab nomini qo'shib aytasan: maktab1::Ali yoki maktab2::Ali. C++ da bunga 'namespace' deyiladi.", first="k", m="Endi std::cout dagi std nima ekanini tushundim!", mm="wow")],
 "c_style": [dict(m="Mening kodim ishlayapti-ku, nega chiroyli yozishim kerak?", mm="think", prop=p_messy),
             dict(k="Tartibli xonada narsani topish oson, to'g'rimi? Kod ham shunday — uni sen ham, do'stlaring ham ko'p marta o'qiydi.", first="k", m="Unda kodimni ham xonam kabi yig'ishtiraman!", mm="happy")],
 "c_statements": [dict(m="Nega har qator oxirida nuqtali vergul qo'yiladi?", mm="think"),
                  dict(k="Har bir qator — kompyuterga bitta buyruq, xuddi retseptdagi bitta qadam. Nuqtali vergul 'buyruq tugadi' degani.", first="k", prop=p_recipe, m="Gapdagi nuqta kabi ekan-da!", mm="wow")],
 "c_types": [dict(m="Kodi, nega oshxonada shakar, tuz va sut har xil idishda turadi?", mm="think"),
             dict(k="Har bir narsaga mos idish kerak! Kompyuterda ham har xil ma'lumot uchun har xil 'idish' — ma'lumot turi bor.", m="Voy, ularning nomi nima?", first="k", prop=p_jars, mm="wow")],
 "c_modifiers": [dict(m="Butun son uchun int bor. Lekin juda katta son kerak bo'lsa-chi?", mm="think"),
                 dict(k="Kiyimning S, M, L, XL o'lchamlari bo'lganidek, short, long, long long kabi 'o'lchamlar' bor. Ular modifikatorlar deyiladi.", first="k", prop=p_sizes, m="Unda Yerdagi odamlar sonini ham saqlay olaman!", mm="happy")],
 "c_const": [dict(m="Haftada doim 7 kun bo'ladi. Uni dasturda tasodifan o'zgartirib qo'ymasam edi...", mm="think"),
             dict(k="Uni const qilib qo'y — qulflangan quti kabi. Ichidagini ko'rish mumkin, lekin hech kim o'zgartira olmaydi!", first="k", prop=p_lock, m="Xuddi seyf kabi!", mm="wow")],
 "c_keywords": [dict(m="O'zgaruvchimga 'if' deb nom bermoqchi edim, kompilyator ruxsat bermadi!", mm="sad"),
                dict(k="Chunki 'if', 'int', 'for' kabi so'zlar C++ ning o'z so'zlari — ular band. Xuddi maktabdagi 'direktor' xonasi kabi!", first="k", prop=p_reserved, m="Tushundim, boshqa nom o'ylab topaman.")],
 "c_variables": [dict(m="Dastur mening yoshimni qayerda eslab qoladi?", mm="think"),
                 dict(k="Xotiradagi nomlangan qutida! Bu quti o'zgaruvchi deyiladi. Uning nomi, turi va ichida qiymati bor.", first="k", prop=p_box, m="Keyingi yili qutidagi sonni 13 ga almashtiraman!", mm="happy", arm="up")],
 "c_auto": [dict(m="Har safar int, double deb yozish shartmi?", mm="think", prop=p_gift),
            dict(k="'auto' deb yozsang, kompilyator qiymatga qarab turini o'zi topadi. Sovg'ani ochib, ichidagini ko'rgandek!", first="k", m="Aqlli kompilyator ekan!", mm="wow")],
 "c_ascii": [dict(m="Kompyuter faqat sonlarni bilsa, harflarni qanday saqlaydi?", mm="think"),
             dict(k="Har bir harfning o'z raqami bor! 'A' — 65, 'B' — 66. Xuddi sinf jurnalidagi tartib raqamlari kabi.", first="k", prop=p_letters, m="Unda mening ismim ham sonlar qatori ekan!", mm="wow")],
 "c_binary": [dict(m="Nega kompyuter faqat 0 va 1 dan foydalanadi?", mm="think"),
              dict(k="Uning ichida millionlab kichik 'chiroqlar' bor: yoniq — 1, o'chiq — 0. Ulardan istalgan sonni yasash mumkin!", first="k", prop=p_bulbs, m="101 — bu 5 degani-ku!", mm="wow", arm="up")],
 "c_conversion": [dict(m="7 ni 2 ga bo'ldim, 3 chiqdi! Kompyuter adashdimi?", mm="sad"),
                  dict(k="Yo'q, butun sonlar 'idishi'ga kasr qism sig'madi va to'kilib ketdi. Uni katta idish — double ga quyish kerak!", first="k", prop=p_glasses, m="Endi 3.5 chiqadi!", mm="happy")],
 "c_operators": [dict(m="Matematikadagi +, -, × belgilari C++ da ham bormi?", mm="think", prop=p_calc),
                 dict(k="Albatta! Ular operatorlar deyiladi. Ustiga % (qoldiq), == (tengmi?), && (va) kabi yangilari ham bor.", first="k", m="Kompyuter katta kalkulyator ekan!", mm="wow")],
 "c_expressions": [dict(m="2 + 3 * 4 nechaga teng? 20 mi?", mm="think"),
                   dict(k="Yo'q, 14! Avval ko'paytirish bajariladi. Agar avval qo'shmoqchi bo'lsang, qavs qo'y: (2 + 3) * 4 = 20.", first="k", prop=p_tree, m="Xuddi matematika darsidagi kabi!", mm="happy")],
 "c_if": [dict(m="Ertaga yomg'ir yog'sa, soyabon olaman. Dastur ham shunday o'ylay oladimi?", mm="think", prop=p_umbrella),
          dict(k="Ha! 'if' yordamida: agar shart rost bo'lsa — bir ish, aks holda ('else') — boshqa ish bajaradi.", first="k", m="Dasturim qaror qabul qila oladi!", mm="wow", arm="up")],
 "c_loops": [dict(m="Ekranga 100 marta 'Salom' yozishim kerak. Qo'lim charchaydi!", mm="sad"),
             dict(k="Tsikl ishlat! U yugurish yo'lakchasidagi aylanalar kabi: shart bajarilguncha qayta-qayta aylanaveradi.", first="k", prop=p_laps, m="3 qator kod — 100 ta salom!", mm="happy")],
 "c_jump": [dict(m="Tsikl o'rtasida to'xtatish yoki bir qadamni o'tkazib yuborish mumkinmi?", mm="think"),
            dict(k="'break' — to'xta va chiq! 'continue' — bu qadamni o'tkazib, keyingisiga o't. Xuddi o'yindagi 'stop' va 'skip' kabi.", first="k", prop=p_stop, m="Zo'r, endi tsikllarni boshqaraman!", mm="wow")],
}
if __name__ == "__main__":
    for k, v in C.items():
        comic(k + ".png", v)
    print(len(C), "comics")
