import pickle, pathlib, requests, urllib.parse, re
s=requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies8.pkl").read_bytes())
s.cookies.update(cookies)
xsrf = s.cookies.get('XSRF-TOKEN')
if xsrf:
    s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(xsrf), 'X-Requested-With':'XMLHttpRequest', 'Accept':'application/json', 'Referer':'https://rdprental.id/account/saldo'})
r = s.get('https://rdprental.id/account/saldo', timeout=30)
jss = sorted(set(re.findall(r'/build/assets/[^\"]+\.js', r.text)))
print("saldo page JS:", jss)
for js in jss:
    if 'saldo' in js.lower():
        t = s.get('https://rdprental.id'+js, timeout=30).text
        print("==", js, len(t))
        pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\saldobundle.js").write_text(t, encoding="utf-8")
        urls = sorted(set(re.findall(r'\"(/(?:api|sewa|account)[^\"\\\']*)\"', t)))
        for u in urls: print(" ", u)
        tmpl = sorted(set(re.findall(r'/(?:sewa|account|api)/[A-Za-z0-9/\-_${}]+', t)))
        for u in tmpl: print("  T:", u)
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies9.pkl","wb").write(pickle.dumps(s.cookies))
