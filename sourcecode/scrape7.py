import requests, re
headers={'User-Agent':'Mozilla/5.0'}
# cari nama file Login terbaru dari html login
r=requests.get("https://rdprental.id/login", headers=headers, timeout=30).text
m=re.findall(r'/build/assets/[^\"]+\.js', r)
print(m)
for js in m:
    if 'Login' in js or 'app-' in js:
        url="https://rdprental.id"+js
        t=requests.get(url, headers=headers, timeout=30).text
        print("==", js, len(t))
        print(t[:3000])
        print("----ROUTES----")
        for p in sorted(set(re.findall(r'\"(/[a-zA-Z0-9/\-_{}]+)\"', t)))[:100]:
            print(p)
