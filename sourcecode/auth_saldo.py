import requests, re, pickle, pathlib, urllib.parse, html, json
s=requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies3.pkl").read_bytes())
s.cookies.update(cookies)
for url in ['https://rdprental.id/account/saldo']:
    r = s.get(url, timeout=30)
    print(url, r.status_code, r.url, len(r.text))
    m = re.search(r'data-page="(.+?)"', r.text, re.DOTALL)
    if m:
        data = json.loads(html.unescape(m.group(1)))
        print(" component:", data.get("component"))
        print(" props keys:", list(data.get("props",{}).keys()))
        for k,v in data['props'].items():
            if isinstance(v,list):
                print(f" - {k}: len {len(v)}", (list(v[0].keys()) if v and isinstance(v[0],dict) else str(v[:1])[:200]))
            elif isinstance(v,dict):
                print(f" - {k}: keys {list(v.keys())} val {str(v)[:500]}")
            else:
                print(f" - {k}: {str(v)[:500]}")
        pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\auth_saldo.json").write_text(json.dumps(data['props'], ensure_ascii=False, indent=2)[:400000], encoding="utf-8")
    jsfiles = sorted(set(re.findall(r'/build/assets/[^\"]+\.js', r.text)))
    print("JS:", jsfiles)
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies4.pkl","wb").write(pickle.dumps(s.cookies))
