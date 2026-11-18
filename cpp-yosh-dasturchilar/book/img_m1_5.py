from imglib import *
import math

# 1 timeline
fig, ax = canvas(11, 3.6)
ax.plot([0.4,10.6],[1.6,1.6],color="#ADB5BD",lw=4)
items=[("1960","Algol"),("1967","BCPL"),("1970","B"),("1972","C"),("1979","C with\nClasses"),("1983","C++"),("1998","C++98"),("2011","C++11"),("2020","C++20")]
for i,(y,n) in enumerate(items):
    x=0.7+i*1.22; c=i%8
    ax.add_patch(Circle((x,1.6),0.16,fc=PAL[c],ec="white",lw=2,zorder=3))
    up = i%2==0
    box(ax,x-0.55,2.0 if up else 0.2,1.1,0.95,n,fc=LIGHT[c],ec=PAL[c],fs=10,bold=True)
    text(ax,x,1.15 if up else 2.05,y,fs=11,color=PAL[c],bold=True)
save(fig,"m1_timeline.png")

# 2 C vs C++ venn
fig, ax = canvas(10,4.6)
ax.add_patch(Ellipse((3.6,2.3),5.6,4.0,fc="#E3EDFF",ec=PAL[0],lw=2.5,alpha=.9))
ax.add_patch(Ellipse((6.4,2.3),5.6,4.0,fc="#FFF4D6",ec=PAL[1],lw=2.5,alpha=.7))
text(ax,2.2,3.7,"Faqat C",fs=14,bold=True,color=PAL[0])
text(ax,2.2,2.3,"protsedurali\nmalloc / free\nprintf / scanf\nstruct (oddiy)",fs=11)
text(ax,5.0,3.85,"Umumiy",fs=14,bold=True,color="#2EAD5B")
text(ax,5.0,2.3,"if, for, while\nmassivlar\nko'rsatkichlar\nfunksiyalar",fs=11)
text(ax,7.9,3.7,"Faqat C++",fs=14,bold=True,color="#C78A00")
text(ax,7.9,2.2,"klass va obyekt\nmerosxo'rlik\nnew / delete\ncin / cout\nshablonlar, STL",fs=11)
save(fig,"m1_venn.png")

# 3 compile flow
fig, ax = canvas(11,3.2)
flow(ax,["salom.cpp\n(sen yozgan kod)","Preprotsessor\n(#include)","Kompilyator\n(mashina tili)","Linker\n(bog'lovchi)","salom.exe\n(dastur!)"],1.0,h=1.3,fs=10)
text(ax,5.5,2.85,"Kod qanday qilib dasturga aylanadi?",fs=14,bold=True)
save(fig,"m2_compile.png")

# 4 comments
fig, ax = canvas(10,4)
box(ax,0.3,0.3,6.2,3.4,"",fc="#F6F8FA",ec="#ADB5BD",r=0.1)
lines=[("// Bu dastur ikki sonni qo'shadi","#2E8B57"),("int a = 5;","#1F2328"),("int b = 7;   // ikkinchi son","#1F2328"),("/* natijani","#2E8B57"),("   ekranga chiqaramiz */","#2E8B57"),("cout << a + b;","#1F2328")]
for i,(t,c) in enumerate(lines):
    text(ax,0.55,3.3-i*0.52,t,fs=12,color=c,ha="left",mono=True)
box(ax,7.0,2.2,2.8,1.3,"Yashil satrlar —\nizohlar. Kompyuter\nularni o'qimaydi!",fc="#FFF4D6",ec=PAL[1],fs=11)
robot(ax,8.4,0.1,0.85,mood="happy")
save(fig,"m3_comments.png")

# 5 header files as toolboxes
fig, ax = canvas(11,3.6)
hs=[("<iostream>","kirish/chiqish\ncin, cout"),("<cmath>","matematika\nsqrt, pow"),("<string>","matn bilan\nishlash"),("<vector>","dinamik\nmassiv"),("<algorithm>","sort, find\nmax, min")]
for i,(h,d) in enumerate(hs):
    x=0.3+i*2.15; c=i
    box(ax,x,0.3,1.9,2.0,d,fc=LIGHT[c],ec=PAL[c],fs=10)
    box(ax,x+0.2,2.15,1.5,0.55,h,fc=PAL[c],ec=PAL[c],fs=10,bold=True,color="white",mono=True)
    ax.plot([x+0.65,x+0.65,x+1.25,x+1.25],[2.7,3.0,3.0,2.7],color=PAL[c],lw=3)
save(fig,"m3_headers.png")

# 6 namespace
fig, ax = canvas(10,4)
for i,(sch,c) in enumerate([("maktab1",0),("maktab2",2)]):
    x=0.4+i*5
    box(ax,x,0.3,4.3,3.0,"",fc=LIGHT[c],ec=PAL[c],r=0.2)
    text(ax,x+2.15,3.0,f"namespace {sch}",fs=13,bold=True,color=PAL[c],mono=True)
    for j,n in enumerate(["Ali","Vali","Laylo"]):
        box(ax,x+0.3+j*1.3,1.2,1.1,1.0,n,fc="white",ec=PAL[c],fs=12,bold=(n=="Ali"))
    text(ax,x+2.15,0.65,f"{sch}::Ali",fs=12,mono=True,color="#C7254E")
save(fig,"m3_namespace.png")

# 7 coding standards
fig, ax = canvas(10,3.8)
box(ax,0.2,0.2,4.6,3.3,"",fc="#FFE3E3",ec=PAL[3])
text(ax,2.5,3.15,"Yomon",fs=14,bold=True,color=PAL[3])
for i,t in enumerate(["int x=5;int y=x*3;","if(y>10){cout<<y;}","int a1, a2, a3;"]):
    text(ax,0.45,2.4-i*0.65,t,fs=11,ha="left",mono=True)
box(ax,5.2,0.2,4.6,3.3,"",fc="#E3F7EA",ec=PAL[2])
text(ax,7.5,3.15,"Yaxshi",fs=14,bold=True,color=PAL[2])
for i,t in enumerate(["int narx = 5;","int jami = narx * 3;","if (jami > 10) {","    cout << jami;","}"]):
    text(ax,5.45,2.55-i*0.5,t,fs=11,ha="left",mono=True)
save(fig,"m3_style.png")

# 8 statements tree
fig, ax = canvas(11,4)
box(ax,4.0,3.0,3.0,0.8,"Ko'rsatmalar (statements)",fc=PAL[0],ec=PAL[0],color="white",bold=True,fs=11)
kids=["E'lon qilish","Ifoda","Blok { }","Tanlash\n(if, switch)","Takrorlash\n(for, while)","Sakrash\n(break, return)"]
for i,k in enumerate(kids):
    x=0.2+i*1.8
    box(ax,x,0.6,1.6,1.1,k,fc=LIGHT[(i+1)%8],ec=PAL[(i+1)%8],fs=10,bold=True)
    arrow(ax,5.5,3.0,x+0.8,1.72,lw=1.5,ms=12)
save(fig,"m3_statements.png")

# 9 data types sizes
fig, ax = canvas(11,4.2)
types=[("bool",1,"true/false"),("char",1,"'A'"),("int",4,"25"),("float",4,"3.14"),("double",8,"3.14159265")]
y=3.4
for i,(t,b,ex) in enumerate(types):
    yy=y-i*0.75
    text(ax,0.9,yy+0.27,t,fs=13,bold=True,mono=True,color=PAL[i])
    for k in range(b):
        box(ax,1.8+k*0.75,yy,0.7,0.55,"",fc=LIGHT[i],ec=PAL[i],r=0.05)
    text(ax,1.8+b*0.75+0.2,yy+0.27,f"{b} bayt   masalan: {ex}",fs=11,ha="left")
save(fig,"m4_types.png")

# 10 modifiers ranges
fig, ax = canvas(11,3.6)
rows=[("short","-32 768 ... 32 767",0.35),("int","-2.1 mlrd ... 2.1 mlrd",0.6),("long long","-9.2 kvintillion ... 9.2 kvintillion",1.0),("unsigned int","0 ... 4.2 mlrd",0.6)]
for i,(n,r,f) in enumerate(rows):
    yy=2.9-i*0.8
    text(ax,1.2,yy,n,fs=12,bold=True,mono=True,color=PAL[i])
    off = 2.6 if "unsigned" not in n else 6.0
    w = 7.6*f if "unsigned" not in n else 3.8*f*1.0
    if "unsigned" in n: off=6.4; w=3.6
    else: off=6.4-3.8*f; w=7.6*f
    box(ax,off,yy-0.25,w,0.5,r,fc=LIGHT[i],ec=PAL[i],fs=10)
ax.plot([6.4,6.4],[0.2,3.4],color="#495057",ls="--",lw=1.5); text(ax,6.4,0.05,"0",fs=11,bold=True)
save(fig,"m4_modifiers.png")

# 11 const locked box
fig, ax = canvas(10,3.6)
box(ax,0.8,0.5,3.2,2.0,"3.14159",fc="#FFF4D6",ec=PAL[1],fs=20,bold=True,mono=True)
text(ax,2.4,2.85,"const double PI",fs=13,mono=True,bold=True,color="#C78A00")
ax.add_patch(FancyBboxPatch((3.55,0.25),0.9,0.75,boxstyle="round,pad=0,rounding_size=0.1",fc="#868E96",ec="#1F2328"))
ax.add_patch(matplotlib.patches.Arc((4.0,1.0),0.55,0.7,theta1=0,theta2=180,color="#1F2328",lw=4))
box(ax,5.2,0.6,4.4,1.8,"PI = 3;   // XATO!\nqulflangan qutini\no'zgartirib bo'lmaydi",fc="#FFE3E3",ec=PAL[3],fs=12)
save(fig,"m4_const.png")

# 12 keywords grid
fig, ax = canvas(11,3.4)
kw=["int","char","bool","double","if","else","for","while","do","switch","case","break","return","class","public","private","const","void","true","false","new","delete","auto","namespace"]
for i,k in enumerate(kw):
    r,c=divmod(i,8)
    box(ax,0.2+c*1.35,2.3-r*1.0,1.2,0.7,k,fc=LIGHT[c],ec=PAL[c],fs=11,bold=True,mono=True)
save(fig,"m4_keywords.png")

# 13 variable box
fig, ax = canvas(10,3.8)
for i,(t,n,v,c) in enumerate([("int","yosh","12",0),("double","boy","1.52",2),("char","harf","'K'",4)]):
    x=0.4+i*3.2
    box(ax,x,0.6,2.6,1.8,v,fc=LIGHT[c],ec=PAL[c],fs=22,bold=True,mono=True)
    box(ax,x+0.4,2.2,1.8,0.6,n,fc=PAL[c],ec=PAL[c],fs=13,color="white",bold=True,mono=True)
    text(ax,x+1.3,0.25,f"turi: {t}",fs=12,mono=True,color="#5A6270")
save(fig,"m4_variables.png")

# 14 auto
fig, ax = canvas(10,3.8)
robot(ax,1.3,0.2,1.3,mood="wow")
for i,(code,t) in enumerate([("auto a = 7;","int"),("auto b = 2.5;","double"),('auto c = \'Z\';',"char"),("auto d = true;","bool")]):
    yy=3.0-i*0.8
    box(ax,3.2,yy-0.3,3.3,0.6,code,fc="#F6F8FA",ec="#ADB5BD",fs=12,mono=True)
    arrow(ax,6.6,yy,7.3,yy)
    box(ax,7.4,yy-0.3,2.0,0.6,t,fc=LIGHT[i],ec=PAL[i],fs=12,bold=True,mono=True)
save(fig,"m4_auto.png")

# 15 ascii
fig, ax = canvas(11,3.4)
chars=[("A","65"),("B","66"),("a","97"),("0","48"),("!","33"),("€","8364"),("Ж","1046"),("😀","128512")]
for i,(ch,code) in enumerate(chars):
    x=0.3+i*1.33; c = 0 if i<5 else 4
    box(ax,x,1.4,1.15,1.1,ch if ch!="😀" else ":-)",fc=LIGHT[c],ec=PAL[c],fs=18,bold=True)
    text(ax,x+0.57,1.05,code,fs=11,mono=True)
text(ax,3.4,2.95,"ASCII (128 ta belgi)",fs=13,bold=True,color=PAL[0])
text(ax,8.9,2.95,"Unicode (1 mln dan ortiq)",fs=13,bold=True,color=PAL[4])
text(ax,5.5,0.45,"Har bir belgining o'z raqami bor — kompyuter harflarni raqam sifatida saqlaydi",fs=11,color="#5A6270")
save(fig,"m4_ascii.png")

# 16 binary bulbs 13 = 1101
fig, ax = canvas(10,3.8)
bits=[1,1,0,1]; vals=[8,4,2,1]
for i,(b,v) in enumerate(zip(bits,vals)):
    x=1.5+i*1.9
    ax.add_patch(Circle((x,2.3),0.6,fc="#FFD43B" if b else "#DEE2E6",ec="#1F2328",lw=2))
    ax.add_patch(Rectangle((x-0.25,1.45),0.5,0.3,fc="#868E96",ec="#1F2328"))
    text(ax,x,2.3,str(b),fs=22,bold=True)
    text(ax,x,1.1,str(v),fs=14,bold=True,color="#5A6270")
text(ax,5.0,0.45,"8 + 4 + 0 + 1 = 13      →      13 = 1101 (ikkilik)",fs=14,bold=True,color=PAL[0])
text(ax,5.0,3.45,"Yonib turgan lampa = 1, o'chgan lampa = 0",fs=12,color="#5A6270")
save(fig,"m4_binary.png")

# 17 type conversion glasses
fig, ax = canvas(10,3.8)
def glass(x,w,h,fill,label,c):
    ax.add_patch(Polygon([[x,0.4],[x+w,0.4],[x+w+0.15,0.4+h],[x-0.15,0.4+h]],fc="white",ec="#1F2328",lw=2))
    ax.add_patch(Polygon([[x,0.4],[x+w,0.4],[x+w+0.15*fill,0.4+h*fill],[x-0.15*fill,0.4+h*fill]],fc=c,ec="none",alpha=.8))
    text(ax,x+w/2,0.1,label,fs=12,mono=True,bold=True)
glass(0.8,1.5,2.2,0.55,"int",PAL[0])
arrow(ax,2.8,1.6,4.0,1.6); text(ax,3.4,2.0,"xavfsiz",fs=11,color=PAL[2],bold=True)
glass(4.4,1.5,2.8,0.43,"double",PAL[0])
glass(7.6,1.0,1.2,1.0,"int",PAL[3])
ax.add_patch(Ellipse((8.1,1.8),0.6,0.25,fc=PAL[3],alpha=.6))
text(ax,8.1,2.6,"3.99 → 3\n(kasr qismi to'kildi!)",fs=11,color=PAL[3],bold=True)
save(fig,"m4_conversion.png")

# 18 operators cards
fig, ax = canvas(11,3.6)
ops=[("Arifmetik","+  -  *  /  %"),("Taqqoslash","==  !=  <  >"),("Mantiqiy","&&  ||  !"),("O'zlashtirish","=  +=  -="),("Oshirish","++  --"),("Bitli","&  |  ^  <<")]
for i,(n,o) in enumerate(ops):
    x=0.2+i*1.8
    box(ax,x,0.4,1.65,2.6,"",fc=LIGHT[i],ec=PAL[i])
    text(ax,x+0.82,2.55,n,fs=10,bold=True,color=PAL[i])
    text(ax,x+0.82,1.5,o.replace("  ","\n"),fs=13,mono=True,bold=True)
save(fig,"m4_operators.png")

# 19 expression tree (2 + 3) * 4
fig, ax = canvas(8,4)
def node(x,y,t,c):
    ax.add_patch(Circle((x,y),0.42,fc=LIGHT[c],ec=PAL[c],lw=2.5)); text(ax,x,y,t,fs=16,bold=True,mono=True)
for (a,b) in [((4,3.3),(2.5,2.0)),((4,3.3),(5.5,2.0)),((2.5,2.0),(1.5,0.7)),((2.5,2.0),(3.5,0.7))]:
    ax.plot([a[0],b[0]],[a[1],b[1]],color="#868E96",lw=2,zorder=0)
node(4,3.3,"*",3); node(2.5,2.0,"+",1); node(5.5,2.0,"4",0); node(1.5,0.7,"2",0); node(3.5,0.7,"3",0)
text(ax,6.7,1.0,"(2 + 3) * 4\n= 5 * 4\n= 20",fs=13,mono=True,ha="left",va="center")
save(fig,"m4_expr.png")

# 20 if flowchart
fig, ax = canvas(10,4.4)
ax.add_patch(Polygon([[5,4.1],[6.6,3.2],[5,2.3],[3.4,3.2]],fc="#FFF4D6",ec=PAL[1],lw=2.5))
text(ax,5,3.2,"baho >= 5 ?",fs=12,bold=True,mono=True)
box(ax,0.6,0.4,3.0,1.0,"\"A'lo!\"",fc="#E3F7EA",ec=PAL[2],fs=13,bold=True)
box(ax,6.4,0.4,3.0,1.0,"\"Harakat qil!\"",fc="#FFE3E3",ec=PAL[3],fs=13,bold=True)
arrow(ax,3.4,3.2,2.1,1.45); text(ax,2.3,2.7,"ha (true)",fs=11,color=PAL[2],bold=True)
arrow(ax,6.6,3.2,7.9,1.45); text(ax,7.8,2.7,"yo'q (false)",fs=11,color=PAL[3],bold=True)
save(fig,"m5_if.png")

# 21 loop
fig, ax = canvas(10,4.2)
box(ax,0.3,3.0,2.6,0.8,"i = 1",fc=LIGHT[0],ec=PAL[0],fs=13,mono=True,bold=True)
ax.add_patch(Polygon([[4.6,3.9],[6.0,3.4],[4.6,2.9],[3.2,3.4]],fc="#FFF4D6",ec=PAL[1],lw=2))
text(ax,4.6,3.4,"i <= 5 ?",fs=12,mono=True,bold=True)
box(ax,3.3,1.0,2.6,0.9,"cout << i;",fc=LIGHT[2],ec=PAL[2],fs=12,mono=True,bold=True)
box(ax,0.3,1.0,2.4,0.9,"i++",fc=LIGHT[4],ec=PAL[4],fs=13,mono=True,bold=True)
box(ax,7.2,3.0,2.5,0.8,"tugadi",fc=LIGHT[3],ec=PAL[3],fs=13,bold=True)
arrow(ax,2.9,3.4,3.2,3.4); arrow(ax,4.6,2.9,4.6,1.95); text(ax,5.0,2.4,"ha",fs=11,color=PAL[2],bold=True)
arrow(ax,3.3,1.45,2.75,1.45); arrow(ax,1.5,1.95,3.4,3.25,rad=-0.3)
arrow(ax,6.0,3.4,7.15,3.4); text(ax,6.55,3.7,"yo'q",fs=11,color=PAL[3],bold=True)
text(ax,6.5,1.0,"Natija: 1 2 3 4 5",fs=12,mono=True,ha="left",color="#5A6270")
save(fig,"m5_loop.png")

# 22 jump
fig, ax = canvas(11,3.4)
text(ax,2.7,3.0,"continue — bu qadamni o'tkazib yubor",fs=12,bold=True,color=PAL[1])
text(ax,8.3,3.0,"break — tsikldan butunlay chiq",fs=12,bold=True,color=PAL[3])
for i in range(1,6):
    x=0.3+(i-1)*1.0
    skip = i==3
    box(ax,x,1.4,0.85,0.85,str(i),fc="#F1F3F5" if skip else LIGHT[1],ec="#ADB5BD" if skip else PAL[1],fs=16,bold=True,color="#ADB5BD" if skip else "#1F2328")
    if skip: ax.plot([x+0.1,x+0.75],[1.5,2.15],color=PAL[3],lw=3)
for i in range(1,6):
    x=5.9+(i-1)*1.0
    gone = i>=3
    box(ax,x,1.4,0.85,0.85,str(i),fc="#F1F3F5" if gone else LIGHT[3],ec="#ADB5BD" if gone else PAL[3],fs=16,bold=True,color="#ADB5BD" if gone else "#1F2328")
ax.plot([7.85,7.85],[1.2,2.5],color=PAL[3],lw=4)
text(ax,2.7,0.8,"natija: 1 2 4 5",fs=12,mono=True); text(ax,8.3,0.8,"natija: 1 2",fs=12,mono=True)
save(fig,"m5_jump.png")

# module banners: robot + title
for k,(title,c) in enumerate([("1-modul","0")]):
    pass
print("done")
