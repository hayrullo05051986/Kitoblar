from comic import *

def p_lockers(ax, x, y):
    for i in range(4):
        box(ax, x + 0.05 + i * 0.52, y + 0.25, 0.46, 1.25, "", fc=LIGHT[i], ec=PAL[i], r=0.04)
        ax.text(x + 0.28 + i * 0.52, y + 1.3, str(i), fontsize=9, ha="center", fontweight="bold", family="DejaVu Sans Mono")
        ax.add_patch(Circle((x + 0.42 + i * 0.52, y + 0.85), 0.04, fc="#1F2328"))

def p_beads(ax, x, y):
    ax.plot([x + 0.05, x + 2.05], [y + 0.9, y + 0.9], color="#868E96", lw=2)
    for i, ch in enumerate("SALOM"):
        ax.add_patch(Circle((x + 0.25 + i * 0.4, y + 0.9), 0.18, fc=LIGHT[i], ec=PAL[i], lw=2))
        ax.text(x + 0.25 + i * 0.4, y + 0.9, ch, fontsize=9, ha="center", va="center", fontweight="bold")

def p_light(ax, x, y):
    box(ax, x + 0.75, y + 0.15, 0.6, 1.4, "", fc="#343A40", ec="#1F2328", r=0.12)
    for k, c in enumerate(["#E5484D", "#F2A900", "#2EAD5B"]):
        ax.add_patch(Circle((x + 1.05, y + 1.3 - k * 0.42), 0.15, fc=c, ec="white"))

def p_hotel(ax, x, y):
    box(ax, x + 0.2, y + 0.2, 1.7, 1.4, "", fc="#FFF4D6", ec=PAL[1], r=0.05)
    for r in range(3):
        for c in range(3):
            fc = "#FFD43B" if (r + c) % 2 == 0 else "#ADB5BD"
            ax.add_patch(Rectangle((x + 0.4 + c * 0.5, y + 0.4 + r * 0.38), 0.3, 0.25, fc=fc, ec="#1F2328", lw=0.8))

C = {
 "c_array": [dict(m="Sinfimizdagi 30 ta o'quvchining bahosini saqlash uchun 30 ta o'zgaruvchi kerakmi?", mm="think"),
             dict(k="Yo'q! Massiv ishlat — raqamlangan shkafchalar qatori kabi. Bitta nom, ichida 30 ta joy. Raqamlash esa 0 dan boshlanadi!", first="k", prop=p_lockers, m="Bitta nom — 30 ta baho!", mm="wow")],
 "c_string": [dict(m="Ismimni saqlamoqchiman, lekin char faqat bitta harf saqlaydi...", mm="think"),
              dict(k="So'zlar uchun string bor! U ipga terilgan munchoqlar kabi — harflar ketma-ket tizilgan qator.", first="k", prop=p_beads, m="Endi ism, gap, hatto ertak ham saqlay olaman!", mm="happy", arm="up")],
 "c_enum": [dict(m="Svetofor ranglarini 0, 1, 2 raqamlari bilan belgilasam, keyin qaysi biri qaysiligi esimdan chiqadi.", mm="think", prop=p_light),
            dict(k="enum ishlat! Raqamlarga QIZIL, SARIQ, YASHIL kabi nomlar berasan. Kod o'qishga juda oson bo'ladi.", first="k", m="Nomlar raqamlardan yaxshiroq ekan!", mm="wow")],
 "c_storage": [dict(m="Funksiya tugaganda uning o'zgaruvchilari qayerga ketadi?", mm="think", prop=p_hotel),
               dict(k="Ular mehmonxona xonasi kabi: funksiya tugasa — xona bo'shatiladi. Lekin 'static' o'zgaruvchilar doimiy yashovchilar kabi — dastur oxirigacha qoladi!", first="k", m="Har bir o'zgaruvchining o'z umri bor ekan!", mm="wow")],
}
if __name__ == "__main__":
    for k, v in C.items():
        comic(k + ".png", v)
    print(len(C))
