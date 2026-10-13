import requests, re, pickle, pathlib, urllib.parse, html, json
s=requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies3.pkl").read_bytes())
s.cookies.update(cookies)
r = s.get('https://rdprental.id/account/services', timeout=30)
m = re.search(r'data-page="(.+?)"', r.text, re.DOTALL)
data = json.loads(html.unescape(m.group(1)))
rentals = data['props']['rentals']
print(f"TOTAL RENTALS: {len(rentals)}")
for x in rentals:
    print(f"- id={x['id']} {x['machine_name']} | {x['package_name']} | status={x['status']} paused={x['is_paused']} billing={x['billing_mode']} bayar={x['price_paid']} mulai={x['starts_at']} habis={x['expires_at']} extend={x['can_extend']}")
    if x.get('connection'):
        c = x['connection']
        # jangan print password penuh, hanya info ada/tidak
        print(f"  conn keys: {list(c.keys())}")
        # tampilkan host/port/user saja
        for k in ['host','address','port','username','rdp_address','hostname']:
            if k in c:
                print(f"   {k}={c[k]}")
# cari JS bundle services untuk endpoint aksi
jsfiles = sorted(set(re.findall(r'/build/assets/[^\"]+\.js', r.text)))
print("JS:", jsfiles)
for js in jsfiles:
    if 'service' in js.lower() or 'account' in js.lower() or 'Service' in js:
        t = s.get('https://rdprental.id'+js, timeout=30).text
        print("==", js, len(t))
        paths = sorted(set(re.findall(r'\"(/(?:sewa|api|account)[^\"\\\']*)\"', t)))
        for p in paths:
            print(" ", p)
        # simpan
        pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode" + "/" + js.split("/")[-1]).write_text(t, encoding="utf-8")
