import pickle, pathlib, requests, urllib.parse
s = requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0','Accept':'application/json','Referer':'https://rdprental.id/account/saldo','Origin':'https://rdprental.id/','X-Requested-With':'XMLHttpRequest','Content-Type':'application/json'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies8.pkl").read_bytes())
s.cookies.update(cookies)
s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN'))})
payload = {"size_gb": 50}
print("POST /account/storage/subscribe", payload)
r = s.post('https://rdprental.id/account/storage/subscribe', json=payload, timeout=40)
print("storage:", r.status_code, r.text[:2000])
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies9.pkl","wb").write(pickle.dumps(s.cookies))
