import pickle, pathlib, requests, urllib.parse, json
s = requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0','Accept':'application/json','Referer':'https://rdprental.id/account/saldo','Origin':'https://rdprental.id/','X-Requested-With':'XMLHttpRequest','Content-Type':'application/json'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies7.pkl").read_bytes())
s.cookies.update(cookies)
s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN'))})
payload = {"amount": 10000, "gateway_method": "qris"}
print("POST /account/saldo/topup", payload)
r = s.post('https://rdprental.id/account/saldo/topup', json=payload, timeout=40)
print("topup:", r.status_code, r.text[:3000])
if r.status_code in (200, 201):
    pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\topup_576.json").write_text(r.text, encoding="utf-8")
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies8.pkl","wb").write(pickle.dumps(s.cookies))
