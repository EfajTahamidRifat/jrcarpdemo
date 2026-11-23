import base64,re,os
t=open('template.html').read()
def rep(m):
    k=m.group(1)
    for ext,mime in (('webp','image/webp'),('woff2','font/woff2')):
        p=f'img/{k}.{ext}'
        if os.path.exists(p): return f'data:{mime};base64,'+base64.b64encode(open(p,'rb').read()).decode()
    raise SystemExit('missing '+k)
out=re.sub(r'\{\{([\w-]+)\}\}',rep,t)
open('../index.html','w').write(out);print(len(out)//1024,'KB')
