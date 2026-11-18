import json,subprocess,sys,re
pdf=sys.argv[1]
n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout).group(1))
txt=subprocess.run(['pdftotext','-layout',pdf,'-'],capture_output=True,text=True).stdout.split('\f')
norm=lambda s:re.sub(r'[^0-9a-z]','',s.lower().replace('ʻ',"'"))
SUF=sys.argv[2] if len(sys.argv)>2 else ''
heads=json.load(open('heads'+SUF+'.json'))
res={}; p=0
toc=[i for i in range(min(25,len(txt))) if 'Mundarija' in txt[i] or '.....' in txt[i]]
p=(max(toc)+1) if toc else 2
print('content starts at page',p+1)
for h in heads:
    key=norm(h['t'])[:25]
    found=None
    for q in range(p,len(txt)):
        full=norm(h['t'])
        for l in txt[q].split('\n'):
            nl=norm(l)
            if nl and nl.startswith(key) and len(nl)<=len(full)+3:
                found=q;break
        if found is not None: break
    if found is None:
        print('NOT FOUND',h['t']); continue
    res[h['id']]=found+1; p=found
json.dump(res,open('tocpages'+SUF+'.json','w'))
print(len(res),'of',len(heads),'pages',n)
