import requests, urllib.parse, pickle, pathlib
s=requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36','Accept':'application/json','X-Requested-With':'XMLHttpRequest','Referer':'https://rdprental.id/','Origin':'https://rdprental.id'})
# load cookies dari step request
pkl = pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies.pkl")
cookies = pickle.loads(pkl.read_bytes())
s.cookies.update(cookies)
print("loaded cookies:", dict(s.cookies))
xsrf = s.cookies.get('XSRF-TOKEN')
s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(xsrf)})
phone="6283115405281"
otp="789784"
# coba tanpa nama dulu, kalau perlu nama user baru
for payload in [{'phone': phone, 'otp': otp}, {'phone': phone, 'otp': otp, 'name': ''}]:
    r=s.post('https://rdprental.id/api/customer/otp/verify', json=payload, timeout=30)
    print("payload:", payload, "->", r.status_code)
    print(r.text[:3000])
    if r.status_code==200:
        break
# simpan session baru
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies2.pkl","wb").write(pickle.dumps(s.cookies))
print("cookies now:", dict(s.cookies))
