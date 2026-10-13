import pickle, pathlib, requests, urllib.parse, re, html, json
s=requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36','Accept':'application/json, text/html','Referer':'https://rdprental.id/','Origin':'https://rdprental.id','X-Requested-With':'XMLHttpRequest'})
pkl_path = pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies4.pkl")
cookies = pickle.loads(pkl_path.read_bytes())
s.cookies.update(cookies)
def api_get(url):
    xsrf = s.cookies.get('XSRF-TOKEN')
    if xsrf:
        s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(xsrf)})
    r = s.get(url, timeout=30, allow_redirects=True)
    return r
for url in ['https://rdprental.id/', 'https://rdprental.id/account/services', 'https://rdprental.id/account/saldo']:
    r = api_get(url)
    print(url, r.status_code, r.url)
    m = re.search(r'data-page="(.+?)"', r.text, re.DOTALL)
    if not m:
        print("  NO data-page, len", len(r.text), r.text[:300])
        continue
    data = json.loads(html.unescape(m.group(1)))
    print("  component:", data.get("component"))
    p = data['props']
    if 'customer' in p and p['customer']:
        print("  customer:", p['customer'].get('phone'), "wallet:", p.get('walletBalance'))
    if 'rentals' in p:
        print(f"  rentals: {len(p['rentals'])}")
        for x in p['rentals'][:5]:
            print(f"   - {x['id']} {x['machine_name']} {x['status']}/{x['billing_mode']} paid={x['price_paid']}")
    if 'machines' in p:
        ms = p['machines']
        av = [x for x in ms if x.get('is_available')]
        print(f"  machines: {len(ms)} avail: {len(av)} ids: {[x['id'] for x in av]}")
        m30 = next((x for x in ms if x['id']==30), None)
        if m30:
            print(f"  id30: avail={m30['is_available']} maint={m30['under_maintenance']} exp={m30['rental_expires_at']} hourly={m30['price_hourly']}")
    if 'balance' in p:
        print("  saldo balance:", p['balance'], "tx:", len(p.get('transactions',[])))
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies5.pkl","wb").write(pickle.dumps(s.cookies))
print("session refreshed OK")
