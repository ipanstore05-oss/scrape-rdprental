import re, json, requests, html, pathlib
headers={'User-Agent':'Mozilla/5.0'}
r=requests.get('https://rdprental.id/', headers=headers, timeout=30)
m=re.search(r'data-page="(.+?)"', r.text, re.DOTALL)
print("status", r.status_code, "len", len(r.text))
if m:
    raw=html.unescape(m.group(1))
    pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\landing.json").write_text(raw, encoding='utf-8')
    data=json.loads(raw)
    machines=data['props']['machines']
    print(f"TOTAL: {len(machines)}")
    avail=[x for x in machines if x.get('is_available')]
    print(f"AVAILABLE: {len(avail)}")
    for x in machines:
        print(x['id'], x['name'], repr(x['package_name']), 'avail='+str(x['is_available']), 'hourly='+str(x['price_hourly']), 'uptime='+str(x['uptime_percent']))
else:
    print('no data-page')
