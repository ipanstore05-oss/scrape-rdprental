import pickle, pathlib, requests, urllib.parse, re, html, json, time
s = requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0','Accept':'text/html','Referer':'https://rdprental.id/'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies7.pkl").read_bytes())
s.cookies.update(cookies)
for i in range(4):
    s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN')), 'X-Requested-With':'XMLHttpRequest'})
    r = s.get('https://rdprental.id/account/services', timeout=40)
    data = json.loads(html.unescape(re.search(r'data-page="(.+?)"', r.text, re.DOTALL).group(1)))
    rs = data['props']['rentals']
    for x in rs:
        c = x.get('connection') or {}
        print(f"try{i} id={x['id']} status={x['status']} paid={x['price_paid']} host={c.get('host')} port={c.get('port')}")
    open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies7.pkl","wb").write(pickle.dumps(s.cookies))
    if i < 3:
        time.sleep(20)
