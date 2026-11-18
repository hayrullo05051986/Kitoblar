import re,sys,subprocess,os,glob
files=sys.argv[1:] or sorted(glob.glob('merged/*.md'))
os.makedirs('/tmp/cc',exist_ok=True)
bad=0;n=0
for f in files:
    s=open(f).read()
    blocks=[(m.group(1),m.group(2),m.start()) for m in re.finditer(r'```(\w*)\n(.*?)```',s,re.S)]
    for i,(k,code,pos) in enumerate(blocks):
        if k!='cpp' or 'int main' not in code: continue
        n+=1
        line=s[:pos].count('\n')+1
        src=f'/tmp/cc/t.cpp'; open(src,'w').write(code)
        # header-file examples: provide hisob.h
        open('/tmp/cc/hisob.h','w').write('#ifndef HISOB_H\n#define HISOB_H\nint kvadrat(int x){return x*x;}\n#endif\n')
        r=subprocess.run(['g++','-std=c++20','-w','-I/tmp/cc','-o','/tmp/cc/t',src],capture_output=True,text=True)
        if r.returncode:
            bad+=1; print(f'COMPILE FAIL {f}:{line}\n{r.stderr[:600]}'); continue
        nxt=blocks[i+1] if i+1<len(blocks) else None
        between = s[pos+len(code):nxt[2]] if nxt else ''
        if nxt and nxt[0]=='output' and 'cin' not in code and 'rand' not in code and 'time(' not in code:
            try:
                out=subprocess.run(['/tmp/cc/t'],capture_output=True,text=True,timeout=5,cwd='/tmp/cc').stdout
            except Exception as e:
                print('RUN FAIL',f,line,e); bad+=1; continue
            norm=lambda t:[l.rstrip() for l in t.strip('\n').split('\n')]
            if norm(out)!=norm(nxt[1]):
                bad+=1; print(f'OUTPUT MISMATCH {f}:{line}\n--- got:\n{out}\n--- book:\n{nxt[1]}')
print(f'checked {n} programs, problems: {bad}')
