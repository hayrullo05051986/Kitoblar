from imglib import *

# m6_func: machine
fig, ax = canvas(10,3.6)
box(ax,0.2,1.2,1.8,1.0,"a = 3\nb = 4",fc=LIGHT[0],ec=PAL[0],fs=12,mono=True,bold=True)
arrow(ax,2.1,1.7,3.0,1.7)
box(ax,3.1,0.6,3.6,2.3,"",fc=LIGHT[1],ec=PAL[1],r=0.3)
text(ax,4.9,2.4,"qoshish(a, b)",fs=13,bold=True,mono=True,color="#C78A00")
text(ax,4.9,1.5,"return a + b;",fs=12,mono=True)
for gx in (3.6,6.2): ax.add_patch(Circle((gx,0.6),0.25,fc="#868E96",ec="#1F2328"))
arrow(ax,6.8,1.7,7.7,1.7)
box(ax,7.8,1.2,1.8,1.0,"7",fc=LIGHT[2],ec=PAL[2],fs=20,mono=True,bold=True)
text(ax,1.1,0.85,"kirish (parametrlar)",fs=10,color="#5A6270"); text(ax,8.7,0.85,"chiqish (natija)",fs=10,color="#5A6270")
save(fig,"m6_func.png")

# m6_lib: bookshelf
fig, ax = canvas(10,3.8)
ax.add_patch(Rectangle((0.3,0.3),9.4,0.15,fc="#8D6E63")); ax.add_patch(Rectangle((0.3,1.95),9.4,0.15,fc="#8D6E63"))
books=[("sqrt",0),("pow",1),("abs",2),("max",3),("min",4),("sort",5),("rand",6),("toupper",7),("strlen",0),("time",1),("swap",2),("round",3)]
x=0.4
for i,(b,c) in enumerate(books):
    row=i//6; xi=0.5+(i%6)*1.53; y=0.45 if row==1 else 2.1
    box(ax,xi,y,1.35,1.45,b,fc=PAL[c],ec="#1F2328",fs=11,bold=True,color="white",mono=True,r=0.05)
save(fig,"m6_lib.png")

# m6_rec: call stack factorial
fig, ax = canvas(10,4.4)
calls=["faktorial(4)","faktorial(3)","faktorial(2)","faktorial(1)"]
rets=["4 * 6 = 24","3 * 2 = 6","2 * 1 = 2","1 (to'xtash!)"]
for i,(c,r) in enumerate(zip(calls,rets)):
    y=3.5-i*0.95
    box(ax,0.4+i*0.5,y,3.2,0.75,c,fc=LIGHT[i],ec=PAL[i],fs=12,mono=True,bold=True)
    box(ax,5.6+i*0.5,y,3.4-i*0.2,0.75,r,fc="white",ec=PAL[i],fs=12,mono=True)
    if i<3: arrow(ax,2.0+i*0.5,y,2.4+i*0.5,y-0.18,color=PAL[i])
    arrow(ax,5.5+i*0.5,y+0.37,3.7+i*0.5,y+0.37,color="#ADB5BD",lw=1.5,ms=12)
text(ax,2.5,4.35,"chaqiruvlar pastga tushadi ↓",fs=11,color="#5A6270")
text(ax,7.5,4.35,"javoblar yuqoriga qaytadi ↑",fs=11,color="#5A6270")
save(fig,"m6_rec.png")

# m6_prep
fig, ax = canvas(10,3.4)
box(ax,0.2,0.3,4.0,2.6,"",fc="#F6F8FA",ec="#ADB5BD",r=0.1)
for i,t in enumerate(["#define PI 3.14","#define KV(x) ((x)*(x))","","y = PI * KV(r);"]):
    text(ax,0.4,2.5-i*0.55,t,fs=11,ha="left",mono=True,color="#C586C0" if t.startswith("#") else "#1F2328")
arrow(ax,4.4,1.6,5.4,1.6); text(ax,4.9,2.0,"preprotsessor",fs=10,color="#5A6270")
box(ax,5.6,0.3,4.2,2.6,"",fc="#F6F8FA",ec="#ADB5BD",r=0.1)
text(ax,5.8,1.6,"y = 3.14 * ((r)*(r));",fs=11,ha="left",mono=True)
save(fig,"m6_prep.png")

# m6_overload
fig, ax = canvas(10,3.6)
text(ax,5,3.3,"Bir xil nom — har xil parametrlar",fs=13,bold=True)
for i,(p,c) in enumerate([("yuza(int a)\nkvadrat",0),("yuza(int a, int b)\nto'rtburchak",2),("yuza(double r)\ndoira",4)]):
    box(ax,0.3+i*3.25,0.5,2.95,2.2,p,fc=LIGHT[c],ec=PAL[c],fs=12,mono=True,bold=True)
save(fig,"m6_overload.png")

# m7_ptr memory
fig, ax = canvas(10,3.8)
addrs=["0x100","0x104","0x108","0x10C","0x110"]
vals=["?","12","?","0x104","?"]
for i,(a,v) in enumerate(zip(addrs,vals)):
    c = 0 if i==1 else (4 if i==3 else 7)
    box(ax,0.5+i*1.85,1.2,1.6,1.0,v,fc=LIGHT[c] if i in (1,3) else "#F8F9FA",ec=PAL[c] if i in (1,3) else "#CED4DA",fs=14,mono=True,bold=True)
    text(ax,1.3+i*1.85,0.9,a,fs=10,mono=True,color="#868E96")
text(ax,3.15,2.55,"int yosh",fs=12,bold=True,mono=True,color=PAL[0])
text(ax,6.85,2.55,"int* p",fs=12,bold=True,mono=True,color=PAL[4])
arrow(ax,6.85,2.25,3.4,2.25,color=PAL[4],rad=0.4)
text(ax,5,0.35,"p o'zida yosh ning manzilini saqlaydi → p yosh ga \"ko'rsatadi\"",fs=11,color="#5A6270")
save(fig,"m7_ptr.png")

# m7_ref
fig, ax = canvas(10,3.6)
box(ax,0.5,0.6,2.8,1.6,"12",fc=LIGHT[0],ec=PAL[0],fs=22,mono=True,bold=True)
box(ax,0.6,2.1,1.2,0.55,"yosh",fc=PAL[0],ec=PAL[0],color="white",fs=11,mono=True,bold=True)
box(ax,2.0,2.1,1.2,0.55,"r",fc=PAL[2],ec=PAL[2],color="white",fs=11,mono=True,bold=True)
text(ax,1.9,0.25,"havola: bitta quti, ikkita nom",fs=11,color="#5A6270")
box(ax,5.0,0.6,2.0,1.6,"12",fc=LIGHT[0],ec=PAL[0],fs=22,mono=True,bold=True)
box(ax,5.4,2.1,1.2,0.55,"yosh",fc=PAL[0],ec=PAL[0],color="white",fs=11,mono=True,bold=True)
box(ax,7.8,0.6,1.8,1.6,"&yosh",fc=LIGHT[4],ec=PAL[4],fs=14,mono=True,bold=True)
box(ax,8.1,2.1,1.2,0.55,"p",fc=PAL[4],ec=PAL[4],color="white",fs=11,mono=True,bold=True)
arrow(ax,7.75,1.4,7.05,1.4,color=PAL[4])
text(ax,7.3,0.25,"ko'rsatkich: alohida quti, ichida manzil",fs=11,color="#5A6270")
save(fig,"m7_ref.png")

# m7_opaque: black box
fig, ax = canvas(10,3.6)
box(ax,3.0,0.5,4.0,2.5,"?",fc="#343A40",ec="#1F2328",fs=48,bold=True,color="#868E96")
for i,(b,c) in enumerate([("yarat()",2),("yoq()",0),("ochir()",3)]):
    box(ax,0.3,2.3-i*0.85,2.2,0.6,b,fc=LIGHT[c],ec=PAL[c],fs=11,mono=True,bold=True)
    arrow(ax,2.55,2.6-i*0.85,2.95,2.6-i*0.85,ms=12)
text(ax,8.5,1.75,"Ichida nima\nborligini\nbilmaymiz —\nfaqat tugmalar\norqali\nishlatamiz",fs=11,color="#5A6270")
save(fig,"m7_opaque.png")

# m7_smart
fig, ax = canvas(10,3.8)
text(ax,2.4,3.5,"unique_ptr — bitta egasi",fs=12,bold=True,color=PAL[0])
box(ax,0.6,0.8,1.4,0.8,"p1",fc=LIGHT[0],ec=PAL[0],fs=13,mono=True,bold=True)
box(ax,2.8,0.6,1.6,1.2,"Robot",fc="#FFF4D6",ec=PAL[1],fs=13,bold=True)
arrow(ax,2.05,1.2,2.75,1.2,color=PAL[0])
text(ax,7.4,3.5,"shared_ptr — bir nechta egasi",fs=12,bold=True,color=PAL[2])
for i,n in enumerate(["p1","p2","p3"]):
    box(ax,5.2,2.3-i*0.85,1.2,0.65,n,fc=LIGHT[2],ec=PAL[2],fs=12,mono=True,bold=True)
    arrow(ax,6.45,2.62-i*0.85,7.55,1.45,color=PAL[2],ms=12)
box(ax,7.6,0.8,1.8,1.3,"Robot\nhisob: 3",fc="#FFF4D6",ec=PAL[1],fs=12,bold=True)
save(fig,"m7_smart.png")

# m7_pp
fig, ax = canvas(10,3.0)
for i,(n,v,c) in enumerate([("int** pp","&p",4),("int* p","&x",3),("int x","7",0)]):
    box(ax,0.4+i*3.4,0.6,2.4,1.2,v,fc=LIGHT[c],ec=PAL[c],fs=16,mono=True,bold=True)
    text(ax,1.6+i*3.4,2.15,n,fs=12,mono=True,bold=True,color=PAL[c])
    if i<2: arrow(ax,2.85+i*3.4,1.2,3.75+i*3.4,1.2,color=PAL[c])
text(ax,5,0.2,"**pp  →  *p  →  x  =  7",fs=12,mono=True,color="#5A6270")
save(fig,"m7_pp.png")

# m7_variadic
fig, ax = canvas(10,3.4)
for j,(args,res) in enumerate([("2, 5","7"),("1, 2, 3, 4","10"),("10, 20, 30, 40, 50","150")]):
    y=2.5-j*0.95
    box(ax,0.3,y,5.0,0.7,f"yigindi({args})",fc=LIGHT[j],ec=PAL[j],fs=12,mono=True,bold=True)
    arrow(ax,5.4,y+0.35,6.3,y+0.35)
    box(ax,6.4,y,1.4,0.7,res,fc="white",ec=PAL[j],fs=13,mono=True,bold=True)
text(ax,8.9,1.6,"argumentlar\nsoni har xil!",fs=12,color="#5A6270")
save(fig,"m7_variadic.png")

# m7_spiral
fig, ax = canvas(10,3.4)
toks=["int","*","(","*","f",")","(","int",")"]
x=1.0
pos=[]
for t in toks:
    w=0.55 if len(t)==1 else 0.9
    box(ax,x,1.5,w,0.75,t,fc="#F6F8FA",ec="#ADB5BD",fs=15,mono=True,bold=True)
    pos.append(x+w/2); x+=w+0.12
steps=[(4,"1. f —"),(3,"2. ko'rsatkich"),(7,"3. int oluvchi funksiyaga,"),(1,"4. int* qaytaradigan")]
for k,(i,s) in enumerate(steps):
    ax.add_patch(Circle((pos[i],1.1),0.2,fc=PAL[k],ec="white"))
    text(ax,pos[i],1.1,str(k+1),fs=10,bold=True,color="white")
text(ax,5,0.45,"f — int qabul qilib, int* qaytaradigan funksiyaga ko'rsatkich",fs=12,color="#1F2328")
text(ax,5,2.85,"O'qish tartibi: nomdan boshlab, avval o'ngga, keyin chapga",fs=12,bold=True,color=PAL[4])
save(fig,"m7_spiral.png")

# m7_fptr: remote control
fig, ax = canvas(10,3.8)
box(ax,0.4,0.4,1.8,3.0,"",fc="#343A40",ec="#1F2328",r=0.3)
text(ax,1.3,3.0,"amal",fs=12,bold=True,color="white",mono=True)
for i,c in enumerate([2,3,0]):
    ax.add_patch(Circle((1.3,2.2-i*0.65),0.22,fc=PAL[c],ec="white"))
fs_=[("qoshish(a,b)",2),("ayirish(a,b)",3),("kopaytir(a,b)",0)]
for i,(f,c) in enumerate(fs_):
    box(ax,5.2,2.55-i*1.0,3.6,0.75,f,fc=LIGHT[c],ec=PAL[c],fs=12,mono=True,bold=True)
arrow(ax,2.3,2.2,5.1,2.9,color=PAL[2],lw=2.5)
text(ax,3.6,1.0,"ko'rsatkichni xohlagan\nfunksiyaga burish mumkin",fs=11,color="#5A6270")
save(fig,"m7_fptr.png")

# m8_array lockers
fig, ax = canvas(10,3.8)
vals=[5,4,5,3,5]
for i,v in enumerate(vals):
    box(ax,0.6+i*1.8,0.7,1.5,2.2,"",fc=LIGHT[i],ec=PAL[i],r=0.08)
    ax.add_patch(Circle((1.95+i*1.8,1.5),0.07,fc="#1F2328"))
    text(ax,1.35+i*1.8,1.8,str(v),fs=24,bold=True,mono=True)
    box(ax,0.9+i*1.8,2.45,0.9,0.35,f"[{i}]",fc="white",ec=PAL[i],fs=10,mono=True)
text(ax,5,0.3,"int baholar[5] = {5, 4, 5, 3, 5};    raqamlash 0 dan boshlanadi!",fs=12,mono=True,color="#5A6270")
text(ax,5,3.3,"Massiv — raqamlangan shkafchalar qatori",fs=13,bold=True)
save(fig,"m8_array.png")

# m8_string
fig, ax = canvas(10,3.0)
s=list("Salom")+["\\0"]
for i,ch in enumerate(s):
    c = 3 if ch=="\\0" else 0
    box(ax,1.0+i*1.3,1.0,1.1,1.0,ch,fc=LIGHT[c],ec=PAL[c],fs=18,mono=True,bold=True)
    text(ax,1.55+i*1.3,0.65,str(i),fs=10,mono=True,color="#868E96")
text(ax,7.6,2.35,"satr oxiri belgisi →",fs=11,color=PAL[3],bold=True)
text(ax,3.6,2.45,'"Salom" — xotirada belgilar qatori',fs=12,bold=True)
save(fig,"m8_string.png")

# m8_union_struct
fig, ax = canvas(11,3.6)
text(ax,2.5,3.3,"struct — har biriga alohida joy",fs=12,bold=True,color=PAL[0])
for i,(n,w,c) in enumerate([("int",1.6,0),("double",3.2,2),("char",0.4,4)]):
    pass
x=0.3
for n,w,c in [("int (4)",1.6,0),("double (8)",3.2,2),("char (1)",0.9,4)]:
    box(ax,x,1.8,w,0.9,n,fc=LIGHT[c],ec=PAL[c],fs=10,bold=True); x+=w+0.05
text(ax,8.6,3.3,"union — hammasi bitta joyda",fs=12,bold=True,color=PAL[3])
for j,(n,w,c) in enumerate([("double (8)",3.2,2),("int (4)",1.6,0),("char (1)",0.9,4)]):
    box(ax,7.0,2.2-j*0.8,w,0.65,n,fc=LIGHT[c],ec=PAL[c],fs=10,bold=True)
ax.plot([7.0,7.0],[0.4,3.0],color=PAL[3],lw=2,ls="--")
text(ax,7.0,0.2,"bir xil boshlang'ich manzil",fs=9,color=PAL[3])
save(fig,"m8_union.png")

# m8_enum traffic light
fig, ax = canvas(10,3.8)
box(ax,0.8,0.2,1.6,3.4,"",fc="#343A40",ec="#1F2328",r=0.3)
for i,(c,n,v) in enumerate([("#E5484D","QIZIL","0"),("#F2A900","SARIQ","1"),("#2EAD5B","YASHIL","2")]):
    ax.add_patch(Circle((1.6,3.0-i*1.05),0.4,fc=c,ec="white",lw=2))
    box(ax,3.4,2.65-i*1.05,3.0,0.7,n,fc="white",ec=c,fs=13,mono=True,bold=True)
    text(ax,7.2,3.0-i*1.05,"= "+v,fs=14,mono=True,bold=True)
text(ax,8.6,1.95,"enum\nSvetofor",fs=13,mono=True,bold=True,color=PAL[4])
save(fig,"m8_enum.png")

# m9_storage lifetimes
fig, ax = canvas(11,3.8)
ax.plot([2.4,10.6],[0.3,0.3],color="#495057",lw=2); text(ax,6.5,0.05,"dastur ishlash vaqti →",fs=10,color="#5A6270")
rows=[("auto",3.6,6.6,0,"funksiya ishlayotganda"),("register",3.6,6.6,1,"auto kabi (eskirgan)"),("static",3.0,10.5,2,"dastur oxirigacha"),("extern",2.5,10.5,4,"boshqa faylda ham"),("thread_local",6.0,9.0,5,"oqim ishlayotganda")]
for i,(n,a,b,c,d) in enumerate(rows):
    y=3.2-i*0.6
    text(ax,1.2,y,n,fs=12,bold=True,mono=True,color=PAL[c])
    box(ax,a,y-0.2,b-a,0.4,d,fc=LIGHT[c],ec=PAL[c],fs=9,r=0.08)
save(fig,"m9_storage.png")
print("done")
