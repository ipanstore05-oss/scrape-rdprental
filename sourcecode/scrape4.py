import requests, re
headers={'User-Agent':'Mozilla/5.0'}
j=open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\landing.js",encoding="utf-8").read()
# semua string "/..." 
paths=sorted(set(re.findall(r'\"(/[a-zA-Z0-9/\-_{}]+)\"', j)))
for p in paths:
    if len(p)>2 and not p.startswith("/_") and ".png" not in p and ".jpg" not in p and ".ico" not in p:
        print(p)
print("=== href ===")
for p in sorted(set(re.findall(r'href:\s*\"([^\"]+)\"', j)))[:80]:
    print(p)
