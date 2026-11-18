from imglib import *
fig, ax = canvas(10, 6)
ax.add_patch(FancyBboxPatch((0.1,0.1),9.8,5.8,boxstyle="round,pad=0,rounding_size=0.4",fc="#F1F5FF",ec="none"))
robot(ax, 3.0, 0.6, 2.0, wave=True)
bubble(ax, 4.9, 4.0, 4.9, 1.3, "Salom! Men Kodiman.\nKeling, C++ ni birga o'rganamiz!", fs=14)
# laptop with code
box(ax, 5.4, 0.9, 4.0, 2.6, "", fc="#1E1E1E", ec="#495057", r=0.1)
for i,(t,c) in enumerate([("#include <iostream>","#C586C0"),("int main() {","#569CD6"),('  std::cout << "Salom!";',"#CE9178"),("  return 0;","#569CD6"),("}","#D4D4D4")]):
    text(ax, 5.6, 3.15-i*0.45, t, fs=12, color=c, ha="left", mono=True)
ax.add_patch(Polygon([[5.0,0.5],[9.8,0.5],[9.4,0.9],[5.4,0.9]],fc="#ADB5BD",ec="#495057",lw=1.5))
for (x,y,s,c) in [(0.7,5.2,"{ }",PAL[1]),(1.0,1.2,"++",PAL[3]),(0.6,3.4,";",PAL[2]),(4.6,5.4,"<>",PAL[4])]:
    text(ax,x,y,s,fs=26,color=c,bold=True,mono=True)
save(fig,"cover.png")
