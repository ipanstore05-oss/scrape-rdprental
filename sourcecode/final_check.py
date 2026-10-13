import pickle, pathlib, requests, urllib.parse, re, html, json
def load(p):
    s = requests.Session()
    s.headers.update({'User-Agent':'Mozilla/5.0','Accept':'text/html','Referer':'https://rdprental.id/'})
    s.cookies.update(pickle.loads(pathlib.Path(p).read_bytes()))
    return s
def props(s, url):
    s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN')), 'X-Requested-With':'XMLHttpRequest'})
    r = s.get(url, timeout=40)
    return json.loads(html.unescape(re.search(r'data-page="(.+?)"', r.text, re.DOTALL).group(1)))['props'], r.status_code

# akun lama 533
s_old = load(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies10.pkl")
p, c = props(s_old, 'https://rdprental.id/account/services')
print("AKUN 533 services:", c, "rentals:", len(p['rentals']))
for x in p['rentals'][:3]:
    print(f"  {x['id']} {x['status']}/{x['billing_mode']} paid={x['price_paid']}")
# status 2074
s_old.headers.update({'Accept':'application/json'})
r = s_old.get('https://rdprental.id/sewa/rentals/2074/status', timeout=30)
print("2074 status:", r.status_code, r.text[:300])
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies12.pkl","wb").write(pickle.dumps(s_old.cookies))

# akun baru 576
s_new = load(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies9.pkl")
p2, c2 = props(s_new, 'https://rdprental.id/account/services')
print("AKUN 576 services:", c2, "rentals:", len(p2['rentals']))
for x in p2['rentals']:
    print(f"  {x['id']} {x['status']}/{x['billing_mode']}")
s_new.headers.update({'Accept':'application/json'})
r2 = s_new.get('https://rdprental.id/account/saldo/topup/878/status', timeout=30)
print("topup 878 status:", r2.status_code, r2.text[:500])
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies10.pkl","wb").write(pickle.dumps(s_new.cookies))
