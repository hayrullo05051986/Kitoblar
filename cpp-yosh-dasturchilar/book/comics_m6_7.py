from comic import *

def p_juicer(ax, x, y):
    ax.add_patch(Circle((x + 0.35, y + 1.25), 0.22, fc="#E5484D", ec="#1F2328"))
    ax.plot([x + 0.35, x + 0.38], [y + 1.47, y + 1.6], color="#2EAD5B", lw=2)
    arrow(ax, x + 0.6, y + 1.25, x + 0.8, y + 1.0, ms=10)
    box(ax, x + 0.75, y + 0.45, 0.9, 0.85, "f( )", fc=LIGHT[1], ec=PAL[1], fs=11, bold=True, mono=True)
    ax.add_patch(Polygon([[x + 1.75, y + 0.2], [x + 2.05, y + 0.2], [x + 2.1, y + 0.75], [x + 1.7, y + 0.75]], fc="#FFA94D", ec="#1F2328"))
    arrow(ax, x + 1.6, y + 0.7, x + 1.8, y + 0.65, ms=10)

def p_shelf(ax, x, y):
    ax.add_patch(Rectangle((x + 0.05, y + 0.2), 2.0, 0.08, fc="#8D6E63"))
    for i, (t, c) in enumerate([("sqrt", 0), ("pow", 1), ("sort", 2), ("max", 3)]):
        box(ax, x + 0.1 + i * 0.49, y + 0.28, 0.44, 1.1, "", fc=PAL[c], ec="#1F2328", r=0.03)
        ax.text(x + 0.32 + i * 0.49, y + 0.83, t, rotation=90, fontsize=8, ha="center", va="center", color="white", fontweight="bold", family="DejaVu Sans Mono")

def p_matryoshka(ax, x, y):
    for i, (s, c) in enumerate([(1.0, 3), (0.78, 1), (0.58, 2), (0.4, 0)]):
        cx = x + 0.3 + i * 0.5 + s * 0.1
        ax.add_patch(Ellipse((cx, y + 0.2 + 0.45 * s), 0.55 * s, 0.9 * s, fc=PAL[c], ec="#1F2328", lw=1.2))
        ax.add_patch(Circle((cx, y + 0.2 + 1.0 * s), 0.2 * s, fc=SKIN, ec="#1F2328", lw=1))

def p_chef(ax, x, y):
    box(ax, x + 0.1, y + 0.3, 1.9, 1.2, "#define PI 3.14\n\nPI  →  3.14", fc="#F6F8FA", ec="#ADB5BD", fs=9, mono=True)

def p_shapes(ax, x, y):
    ax.add_patch(Rectangle((x + 0.1, y + 0.4), 0.55, 0.55, fc=LIGHT[0], ec=PAL[0], lw=2))
    ax.add_patch(Rectangle((x + 0.8, y + 0.45), 0.75, 0.45, fc=LIGHT[2], ec=PAL[2], lw=2))
    ax.add_patch(Circle((x + 1.85, y + 0.68), 0.28, fc=LIGHT[4], ec=PAL[4], lw=2))
    ax.text(x + 1.05, y + 1.25, "yuza( )", fontsize=11, ha="center", fontweight="bold", family="DejaVu Sans Mono")

def p_address(ax, x, y):
    ax.add_patch(Polygon([[x + 0.2, y + 0.9], [x + 0.65, y + 1.35], [x + 1.1, y + 0.9]], fc=PAL[3], ec="#1F2328"))
    box(ax, x + 0.3, y + 0.25, 0.7, 0.65, "12", fc="#FFF4D6", ec="#1F2328", fs=11, bold=True, r=0.02)
    box(ax, x + 1.3, y + 0.45, 0.8, 0.6, "uy:\n0x104", fc="white", ec=PAL[4], fs=8, mono=True)
    arrow(ax, x + 1.3, y + 0.75, x + 1.05, y + 0.6, color=PAL[4], ms=10)

def p_nickname(ax, x, y):
    box(ax, x + 0.3, y + 0.3, 1.5, 0.7, "Muhammadali", fc=LIGHT[0], ec=PAL[0], fs=8.5, bold=True)
    box(ax, x + 0.65, y + 1.05, 0.8, 0.45, "Ali", fc=LIGHT[2], ec=PAL[2], fs=10, bold=True)

def p_remote(ax, x, y):
    box(ax, x + 0.2, y + 0.35, 1.2, 1.1, "?", fc="#343A40", ec="#1F2328", fs=24, bold=True, color="#868E96")
    box(ax, x + 1.55, y + 0.4, 0.45, 1.0, "", fc="#495057", ec="#1F2328", r=0.1)
    for k, c in enumerate([2, 3, 0]):
        ax.add_patch(Circle((x + 1.775, y + 1.2 - k * 0.27), 0.08, fc=PAL[c]))

def p_book_return(ax, x, y):
    box(ax, x + 0.15, y + 0.4, 0.7, 0.9, "", fc=PAL[0], ec="#1F2328", r=0.03)
    ax.text(x + 0.5, y + 0.85, "new", fontsize=9, ha="center", va="center", color="white", fontweight="bold", family="DejaVu Sans Mono")
    arrow(ax, x + 0.9, y + 0.85, x + 1.3, y + 0.85, ms=12)
    box(ax, x + 1.35, y + 0.4, 0.75, 0.9, "", fc="#868E96", ec="#1F2328", r=0.03)
    ax.text(x + 1.72, y + 0.85, "delete", fontsize=7.5, ha="center", va="center", color="white", fontweight="bold", family="DejaVu Sans Mono")

def p_treasure(ax, x, y):
    box(ax, x + 0.05, y + 0.6, 0.6, 0.6, "xat\n1", fc="#FFF9DB", ec=PAL[1], fs=8)
    arrow(ax, x + 0.7, y + 0.9, x + 0.85, y + 0.9, ms=9)
    box(ax, x + 0.85, y + 0.6, 0.6, 0.6, "xat\n2", fc="#FFF9DB", ec=PAL[1], fs=8)
    arrow(ax, x + 1.5, y + 0.9, x + 1.6, y + 0.9, ms=9)
    box(ax, x + 1.6, y + 0.55, 0.5, 0.45, "", fc="#8D6E63", ec="#1F2328", r=0.03)
    ax.add_patch(Rectangle((x + 1.6, y + 0.85), 0.5, 0.18, fc="#FFD43B", ec="#1F2328"))

def p_basket(ax, x, y):
    ax.add_patch(Polygon([[x + 0.3, y + 0.25], [x + 1.8, y + 0.25], [x + 2.0, y + 0.9], [x + 0.1, y + 0.9]], fc="#E9C46A", ec="#8D6E63", lw=2))
    for i, c in enumerate([3, 1, 2, 0, 3]):
        ax.add_patch(Circle((x + 0.4 + i * 0.32, y + 1.0 + 0.1 * (i % 2)), 0.15, fc=PAL[c], ec="#1F2328", lw=0.8))
    ax.text(x + 1.05, y + 0.5, "...", fontsize=14, ha="center", fontweight="bold")

def p_spiral(ax, x, y):
    box(ax, x + 0.05, y + 0.6, 2.0, 0.5, "int* (*f)(int)", fc="#F6F8FA", ec="#ADB5BD", fs=10, mono=True, bold=True)
    ax.add_patch(FancyArrowPatch((x + 1.25, y + 0.5), (x + 0.75, y + 0.5), arrowstyle="-|>", mutation_scale=12, color=PAL[4], lw=2, connectionstyle="arc3,rad=-0.8"))

def p_tvremote(ax, x, y):
    box(ax, x + 0.1, y + 0.3, 0.5, 1.2, "", fc="#343A40", ec="#1F2328", r=0.12)
    for k, c in enumerate([3, 2, 0]):
        ax.add_patch(Circle((x + 0.35, y + 1.25 - k * 0.3), 0.08, fc=PAL[c]))
    box(ax, x + 0.95, y + 0.55, 1.15, 0.85, "TV", fc="#1E1E1E", ec="#495057", fs=12, bold=True, color="#7CFC00")
    arrow(ax, x + 0.62, y + 1.1, x + 0.92, y + 1.0, color=PAL[1], ms=10)

C = {
 "c_func": [dict(m="Har safar ikki sonni qo'shish uchun bir xil kodni qayta yozaman. Zerikarli!", mm="sad"),
            dict(k="Uni funksiyaga aylantir! Funksiya — sharbat mashinasi kabi: olma solasan, sharbat chiqadi. Bir marta yasaysan, ko'p marta ishlatasan.", first="k", prop=p_juicer, m="O'zimning mashinamni yasayman!", mm="wow", arm="up")],
 "c_libfunc": [dict(m="Saralash funksiyasini yozish uchun bir soat o'tirdim...", mm="sad"),
               dict(k="C++ da minglab tayyor funksiyalar bor — kutubxona javonidagi kitoblar kabi. sort(), sqrt(), max() — olib ishlataver!", first="k", prop=p_shelf, m="Avval javonga qarab olishim kerak ekan!", mm="happy")],
 "c_recursion": [dict(m="Matryoshka ichida yana matryoshka, uning ichida yana... Bu qachon tugaydi?", mm="think", prop=p_matryoshka),
                 dict(k="Eng kichigida! Rekursiya ham shunday: funksiya o'zini kichikroq masala bilan chaqiradi va eng oddiy holatda to'xtaydi.", first="k", m="Demak, to'xtash sharti juda muhim!", mm="wow")],
 "c_preproc": [dict(m="# belgisi bilan boshlanadigan qatorlar nimasi bilan alohida?", mm="think"),
               dict(k="Ularni preprotsessor bajaradi — kompilyatsiyadan oldin! U oshpazning yordamchisi kabi: masalliqlarni tayyorlab, matnni almashtirib qo'yadi.", first="k", prop=p_chef, m="Kompilyatorgacha ham ish bor ekan!", mm="wow")],
 "c_morefunc": [dict(m="Kvadrat, to'rtburchak va doira yuzini hisoblash uchun uch xil nom o'ylab topishim kerakmi?", mm="think", prop=p_shapes),
                dict(k="Yo'q! Uchalasini ham 'yuza' deb nomla. Parametrlar har xil bo'lsa, kompilyator kerakligini o'zi tanlaydi.", first="k", m="Bu juda qulay ekan!", mm="happy", arm="up")],
 "c_pointer": [dict(m="Ko'rsatkich degani nima? Qo'rqinchli eshitiladi...", mm="think"),
               dict(k="Qo'rqma! Bu shunchaki uy manzili yozilgan qog'oz. Qog'ozning o'zida narsa yo'q, lekin u narsa qayerdaligini ko'rsatadi.", first="k", prop=p_address, m="Manzilni bilsam, uyga borib, ichidagini o'zgartira olaman!", mm="wow")],
 "c_ptrref": [dict(m="Havola bilan ko'rsatkichning farqi nima? Ikkalasi ham bir xilga o'xshaydi.", mm="think", prop=p_nickname),
              dict(k="Havola — laqab: Muhammadali va Ali bitta odam. Ko'rsatkich — manzil yozilgan alohida qog'oz, uni boshqa manzilga almashtirsa bo'ladi.", first="k", m="Laqab va manzil! Endi esimdan chiqmaydi.", mm="happy")],
 "c_opaque": [dict(m="Televizor ichida nima borligini bilmayman, lekin pult bilan boshqaraman.", mm="happy", prop=p_remote),
              dict(k="Opaque pointer ham shunday: obyekt ichi yashirin, sen u bilan faqat 'tugmalar' — maxsus funksiyalar orqali ishlaysan.", first="k", m="Ichini buzib qo'yish xavfi ham yo'q ekan!", mm="wow")],
 "c_smart": [dict(m="new bilan xotira oldim, lekin delete qilishni unutibman...", mm="sad"),
             dict(k="Kutubxona kitobini qaytarmaganga o'xshaydi! Aqlli ko'rsatkichlar xotirani o'zi qaytaradi — unutish imkonsiz.", first="k", prop=p_book_return, m="Aqlli ko'rsatkichdan foydalanaman!", mm="happy", arm="up")],
 "c_ptrptr": [dict(m="Ko'rsatkichning ham ko'rsatkichi bo'ladimi?", mm="think"),
              dict(k="Ha! Xazina o'yini kabi: 1-xat 2-xat qayerdaligini, 2-xat esa xazina qayerdaligini ko'rsatadi.", first="k", prop=p_treasure, m="Ikki qadamda xazinaga yetaman!", mm="wow")],
 "c_variadic": [dict(m="Funksiyaga ba'zan 2 ta, ba'zan 10 ta son bermoqchiman. Bo'ladimi?", mm="think", prop=p_basket),
                dict(k="Bo'ladi! Istalgan sondagi argument qabul qiladigan funksiyalar bor — xuddi istalgancha meva sig'adigan savat kabi.", first="k", m="Bitta funksiya — hamma holat uchun!", mm="happy")],
 "c_complex": [dict(m="int* (*f)(int) — bu nima? Sehrli formulami?", mm="think"),
               dict(k="Uni o'qishning siri bor: nomdan boshla, avval o'ngga, keyin chapga qara. Qadam-baqadam hammasi tushunarli bo'ladi!", first="k", prop=p_spiral, m="Topishmoq yechgandek qiziq ekan!", mm="wow")],
 "c_funcptr": [dict(m="Funksiyani o'zgaruvchiga saqlab qo'yish mumkinmi?", mm="think", prop=p_tvremote),
               dict(k="Mumkin! Funksiyaga ko'rsatkich — pult kabi: uni xohlagan 'kanal'ga, ya'ni xohlagan funksiyaga burish mumkin.", first="k", m="Unda kalkulyator tugmalarini shunday yasayman!", mm="happy", arm="up")],
}
if __name__ == "__main__":
    for k, v in C.items():
        comic(k + ".png", v)
    print(len(C), "comics")
