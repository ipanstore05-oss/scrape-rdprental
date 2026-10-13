import pickle, pathlib, requests, urllib.parse, re, html, json
s = requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0','Accept':'text/html','Referer':'https://rdprental.id/'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies6.pkl").read_bytes())
s.cookies.update(cookies)
s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN')), 'X-Requested-With':'XMLHttpRequest'})
r = s.get('https://rdprental.id/account/services', timeout=40)
data = json.loads(html.unescape(re.search(r'data-page="(.+?)"', r.text, re.DOTALL).group(1)))
rs = data['props']['rentals']
print("rentals:", len(rs))
for x in rs:
    print(f" - {x['id']} {x['machine_name']} {x['status']}/{x['billing_mode']} paid={x['price_paid']}")
    if x.get('connection'):
        c = x['connection']
        print("   conn:", {k:v for k,v in c.items() if k in ('host','port','username_format_1')})
r2 = s.get('https://rdprental.id/', timeout=40)
d2 = json.loads(html.unescape(re.search(r'data-page="(.+?)"', r2.text, re.DOTALL).group(1)))
print("canClaimTrial now:", d2['props']['canClaimTrial'])
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies7.pkl","wb").write(pickle.dumps(s.cookies))
