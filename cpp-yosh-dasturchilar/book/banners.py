from imglib import *
B = {
 1: ("1-modul: C++ tarixi", "C++ qanday paydo bo'lganini\nbilib olamiz!"),
 2: ("2-modul: Dastur yaratish", "Kompyuterni C++ ga\ntayyorlaymiz!"),
 3: ("3-modul: Dastur tuzilishi", "Kodni chiroyli va tartibli\nyozishni o'rganamiz!"),
 4: ("4-modul: Ma'lumotlar", "Sonlar, harflar va ular bilan\namallar — eng qiziq qism!"),
 5: ("5-modul: Boshqaruv oqimi", "Dasturga qaror qabul qilish va\ntakrorlashni o'rgatamiz!"),
 6: ("6-modul: Funksiyalar", "Kodni kichik yordamchilarga\nbo'lib yozamiz!"),
 7: ("7-modul: Ko'rsatkichlar", "Xotiradagi manzillar sirini\nochamiz!"),
 8: ("8-modul: Murakkab turlar", "Massivlar, satrlar va\nenumlar bilan tanishamiz!"),
 9: ("9-modul: Xotira sinflari", "O'zgaruvchilar qancha yashashini\nbilib olamiz!"),
 10: ("10-modul: OOP asoslari", "Klass va obyektlar —\nC++ ning yuragi!"),
 11: ("11-modul: OOP chuqurroq", "Merosxo'rlik, polimorfizm va\nboshqa super kuchlar!"),
 12: ("12-modul: STL", "Tayyor konteynerlar —\nvaqtni tejaydigan sehrli quti!"),
 13: ("13-modul: Turli mavzular", "Lambda, rvalue va boshqa\nzamonaviy imkoniyatlar!"),
}
for n,(t,s) in B.items():
    c = (n-1) % 8
    fig, ax = canvas(10, 3.4)
    ax.add_patch(FancyBboxPatch((0.05,0.05),9.9,3.3,boxstyle="round,pad=0,rounding_size=0.35",fc=LIGHT[c],ec=PAL[c],lw=2.5))
    robot(ax, 1.7, 0.35, 1.15, color=PAL[c], wave=True)
    text(ax, 6.2, 2.75, t, fs=20, bold=True, color=PAL[c])
    box(ax, 3.7, 0.55, 5.6, 1.45, "", fc="white", ec="#495057", r=0.25, lw=1.8)
    ax.add_patch(Polygon([[3.72,1.0],[3.72,1.4],[3.05,1.05]], closed=True, fc="white", ec="none", zorder=5))
    ax.plot([3.7,3.05,3.7],[1.0,1.05,1.4], color="#495057", lw=1.8, zorder=6)
    text(ax, 6.5, 1.275, s, fs=15)
    save(fig, f"banner{n:02d}.png")
print("ok")
