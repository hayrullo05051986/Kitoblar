import sys,glob
from PIL import Image
files=sorted(glob.glob(sys.argv[1])); out=sys.argv[2]
ims=[Image.open(f).convert("RGB") for f in files]
W=1400; tiles=[]
for im in ims:
    r=W/2/im.width; tiles.append(im.resize((int(im.width*r),int(im.height*r))))
rows=[tiles[i:i+2] for i in range(0,len(tiles),2)]
H=sum(max(t.height for t in r)+10 for r in rows)
sheet=Image.new("RGB",(W,H),"white"); y=0
for r in rows:
    x=0
    for t in r: sheet.paste(t,(x,y)); x+=W//2
    y+=max(t.height for t in r)+10
sheet.save(out); print(len(files))
