import pickle, pathlib, requests, urllib.parse, re, html, json
s=requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0','Accept':'application/json','Referer':'https://rdprental.id/','Origin':'https://rdprental.id/','X-Requested-With':'XMLHttpRequest'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies7.pkl").read_bytes())
s.cookies.update(cookies)
def hdr():
    s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN'))})
hdr()
# 1. poll status rental 2074
r = s.get('https://rdprental.id/sewa/rentals/2074/status', timeout=30)
print("status poll:", r.status_code, r.text[:2000])
# 2. check-now
r2 = s.post('https://rdprental.id/sewa/rentals/2074/check-now', timeout=30)
print("check-now:", r2.status_code, r2.text[:2000])
# 3. refresh services
r3 = s.get('https://rdprental.id/account/services', timeout=30)
m = re.search(r'data-page="(.+?)"', r3.text, re.DOTALL)
data = json.loads(html.unescape(m.group(1)))
rs = data['props']['rentals']
print(f"rentals now: {len(rs)}")
for x in rs[:4]:
    print(f" - {x['id']} {x['machine_name']} {x['status']}/{x['billing_mode']} paid={x['price_paid']} exp={x['expires_at']}")
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies8.pkl","wb").write(pickle.dumps(s.cookies))
