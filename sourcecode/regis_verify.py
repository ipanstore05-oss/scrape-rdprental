import requests, urllib.parse, pickle, pathlib
s = requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0','Accept':'application/json','Referer':'https://rdprental.id/','Origin':'https://rdprental.id/','X-Requested-With':'XMLHttpRequest','Content-Type':'application/json'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies4.pkl").read_bytes())
s.cookies.update(cookies)
s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN'))})
phone = "6285117834250"
for payload in [{'phone': phone, 'otp': '405663'}, {'phone': phone, 'otp': '405663', 'name': 'Tester'}]:
    r = s.post('https://rdprental.id/api/customer/otp/verify', json=payload, timeout=30)
    print("payload:", {k:('***' if k=='otp' else v) for k,v in payload.items()}, "->", r.status_code, r.text[:2000])
    if r.status_code == 200:
        break
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies5.pkl","wb").write(pickle.dumps(s.cookies))
