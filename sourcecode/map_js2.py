import requests, re, pathlib
s = requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0'})
base = "https://rdprental.id"
tmp = pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode")
targets = {
 "landing": "/build/assets/landing-4Xq0rb4g.js",
 "saldo": None, "services": None, "become-host": "/build/assets/become-host-DgvJ7Tgs.js",
}
# cari nama saldo/services dari halaman auth? pakai cache lama
for f in ["saldo-BZUVpUsL.js", "services-D6EGha4H.js"]:
    p = tmp / f
    if p.exists():
        print(f, "cached", p.stat().st_size)
for js in ["/build/assets/become-host-DgvJ7Tgs.js"]:
    t = s.get(base+js, timeout=30).text
    print("==", js, len(t))
    for pat in [r'\"(/(?:api|sewa|account|jadi-host)[^\"\\\']*)\"', r'route\(\s*[\"\\\']([^\"\\\']+)[\"\\\']', r'(POST|GET|PUT|DELETE)\s*[^a-zA-Z]*(/(?:api|sewa|account)[\w\-/{}]*)']:
        found = sorted(set(re.findall(pat, t)))
        print(" ", pat[:30], "->", found[:60])
