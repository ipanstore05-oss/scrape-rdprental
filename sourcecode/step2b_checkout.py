import pickle, pathlib, requests, urllib.parse, json
s=requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36','Accept':'application/json','Referer':'https://rdprental.id/','Origin':'https://rdprental.id/','X-Requested-With':'XMLHttpRequest','Content-Type':'application/json'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies6.pkl").read_bytes())
s.cookies.update(cookies)
s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN'))})
payload = {"machine_id": 30, "duration_type": "hourly", "hours": 2}
print("POST /sewa/checkout", payload)
r = s.post('https://rdprental.id/sewa/checkout', json=payload, timeout=30)
print("status:", r.status_code)
print(r.text[:8000])
if r.status_code in (200,201):
    data = r.json()
    pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\checkout_qris.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies7.pkl","wb").write(pickle.dumps(s.cookies))
