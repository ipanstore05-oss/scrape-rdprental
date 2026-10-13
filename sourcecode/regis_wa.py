import requests, urllib.parse, pickle, pathlib, json
s = requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)','Accept':'application/json','Referer':'https://rdprental.id/','Origin':'https://rdprental.id/','X-Requested-With':'XMLHttpRequest','Content-Type':'application/json'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies.pkl").read_bytes())
s.cookies.update(cookies)
s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN'))})
phone = "6285117834250"
r = s.post('https://rdprental.id/api/customer/whatsapp/generate-code', json={'phone': phone}, timeout=30)
print("generate-code:", r.status_code, r.text[:2000])
try:
    data = r.json()
    pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_wa.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    if "code" in data:
        print("CODE:", data.get("code"))
    if "wa_link" in data:
        print("WA_LINK:", data.get("wa_link"))
    if "owner_phone" in data:
        print("OWNER:", data.get("owner_phone"))
except Exception as e:
    print("parse err", e)
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies2.pkl","wb").write(pickle.dumps(s.cookies))
