import pickle, pathlib, requests, urllib.parse, re, html, json
s = requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0','Accept':'application/json','Referer':'https://rdprental.id/','Origin':'https://rdprental.id/','X-Requested-With':'XMLHttpRequest','Content-Type':'application/json'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies6.pkl").read_bytes())
s.cookies.update(cookies)
s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN'))})
# cek mesin available terbaru
r = s.get('https://rdprental.id/', timeout=30)
data = json.loads(html.unescape(re.search(r'data-page="(.+?)"', r.text, re.DOTALL).group(1)))
ms = data['props']['machines']
av = [x for x in ms if x.get('is_available')]
print("avail:", [(x['id'], x['name'], x['price_hourly']) for x in av])
print("canClaimTrial:", data['props']['canClaimTrial'])
# klaim trial di id 30
payload = {"machine_id": 30, "duration_type": "trial"}
print("POST /sewa/checkout", payload)
r2 = s.post('https://rdprental.id/sewa/checkout', json=payload, timeout=30)
print("trial:", r2.status_code, r2.text[:3000])
if r2.status_code in (200, 201):
    pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\trial_576.json").write_text(r2.text, encoding="utf-8")
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies7.pkl","wb").write(pickle.dumps(s.cookies))
