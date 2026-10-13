import requests, re
headers={'User-Agent':'Mozilla/5.0'}
j=requests.get("https://rdprental.id/build/assets/landing-4Xq0rb4g.js", headers=headers, timeout=30).text
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\landing.js","w",encoding="utf-8").write(j)
# print sekitar checkout
for m in re.finditer(r'.{0,200}sewa.{0,200}', j):
    print(m.group(0)[:500])
    print("----")
# cari route() calls
print("ROUTE CALLS:")
for m in sorted(set(re.findall(r'route\(\s*[\"\\\']([^\"\\\']+)[\"\\\']', j))):
    print(m)
print("FETCH URLS:")
for m in sorted(set(re.findall(r'\"/(?:sewa|api)[^\"\\\']*\"', j))):
    print(m)
