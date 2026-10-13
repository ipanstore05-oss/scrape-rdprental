import requests, urllib.parse, pickle, pathlib
s = requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36','Accept':'application/json','Referer':'https://rdprental.id/','Origin':'https://rdprental.id/','X-Requested-With':'XMLHttpRequest','Content-Type':'application/json'})
r0 = s.get('https://rdprental.id/sanctum/csrf-cookie', timeout=30)
print("csrf:", r0.status_code)
s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN'))})
phone = "6285117834250"
r = s.post('https://rdprental.id/api/customer/otp/request', json={'phone': phone}, timeout=30)
print("otp/request:", r.status_code, r.text[:2000])
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies.pkl","wb").write(pickle.dumps(s.cookies))
