import requests, urllib.parse, pickle, pathlib, re, html, json
s=requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36','Accept':'text/html,application/xhtml+xml','Referer':'https://rdprental.id/','Origin':'https://rdprental.id'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies2.pkl").read_bytes())
s.cookies.update(cookies)

def fetch(url):
    # update xsrf header tiap request
    xsrf = s.cookies.get('XSRF-TOKEN')
    if xsrf:
        s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(xsrf), 'X-Requested-With':'XMLHttpRequest'})
    r = s.get(url, timeout=30, allow_redirects=True)
    print("==", url, r.status_code, "final:", r.url, "len", len(r.text))
    m = re.search(r'data-page="(.+?)"', r.text, re.DOTALL)
    if m:
        data = json.loads(html.unescape(m.group(1)))
        print(" component:", data.get("component"))
        print(" props keys:", list(data.get("props",{}).keys()))
        # simpan
        safe = url.replace("https://","").replace("/","_").strip("_") or "root"
        pathlib.Path(rf"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\auth_{safe}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2)[:500000], encoding="utf-8")
        return data
    else:
        print(r.text[:1000])
        return None

d1 = fetch('https://rdprental.id/')
if d1:
    p = d1['props']
    print("customer:", p.get('customer'))
    print("walletBalance:", p.get('walletBalance'))
    print("canClaimTrial:", p.get('canClaimTrial'))
    print("customerHasStorage:", p.get('customerHasStorage'))
    ms = p.get('machines', [])
    print("machines:", len(ms), "avail:", sum(1 for x in ms if x.get('is_available')))

d2 = fetch('https://rdprental.id/account/services')
if d2:
    p = d2['props']
    # tampilkan ringkas, jangan dump kredensial penuh ke log? tampilkan keys + jumlah
    print("account/services full keys:", list(p.keys()))
    for k,v in p.items():
        if isinstance(v, list):
            print(f" - {k}: list len {len(v)}")
            if v:
                print("   sample keys:", list(v[0].keys()) if isinstance(v[0], dict) else str(v[0])[:300])
        elif isinstance(v, dict):
            print(f" - {k}: dict keys {list(v.keys())}")
        else:
            print(f" - {k}: {str(v)[:300]}")

# simpan cookies terbaru
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies3.pkl","wb").write(pickle.dumps(s.cookies))
