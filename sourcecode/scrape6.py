import requests, re, html, json
headers={'User-Agent':'Mozilla/5.0'}
for url in ["https://rdprental.id/sewa"]:
    r=requests.get(url, headers=headers, timeout=30)
    print(url, r.status_code, len(r.text))
    m=re.search(r'data-page="(.+?)"', r.text, re.DOTALL)
    if m:
        data=json.loads(html.unescape(m.group(1)))
        print("component:", data.get("component"))
        print("props keys:", list(data.get("props",{}).keys()))
        # simpan ringkas
        print(str(data)[:2000])
    else:
        print(r.text[:2000])
