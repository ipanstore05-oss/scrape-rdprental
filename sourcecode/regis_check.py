import requests, urllib.parse, pickle, pathlib
s = requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0','Accept':'application/json','Referer':'https://rdprental.id/','Origin':'https://rdprental.id/','X-Requested-With':'XMLHttpRequest','Content-Type':'application/json'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies2.pkl").read_bytes())
s.cookies.update(cookies)
s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN'))})
phone = "6285117834250"
r = s.post('https://rdprental.id/api/customer/whatsapp/check-verification', json={'phone': phone}, timeout=30)
print("check:", r.status_code, r.text[:2000])
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies3.pkl","wb").write(pickle.dumps(s.cookies))
