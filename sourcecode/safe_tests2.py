import pickle, pathlib, requests, urllib.parse, json
s=requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0','Accept':'application/json','Referer':'https://rdprental.id/','Origin':'https://rdprental.id/','X-Requested-With':'XMLHttpRequest','Content-Type':'application/json'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies10.pkl").read_bytes())
s.cookies.update(cookies)
s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN'))})
# WA generate-code pakai nomor sendiri
r = s.post('https://rdprental.id/api/customer/whatsapp/generate-code', json={'phone':'6283115405281'}, timeout=30)
print("wa-generate-code+phone:", r.status_code, r.text[:1000])
r2 = s.post('https://rdprental.id/api/customer/whatsapp/check-verification', json={'phone':'6283115405281'}, timeout=30)
print("wa-check-verification:", r2.status_code, r2.text[:1000])
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies11.pkl","wb").write(pickle.dumps(s.cookies))
