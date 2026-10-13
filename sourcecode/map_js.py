import requests, re, pathlib
s = requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0'})
base = "https://rdprental.id"
# ambil daftar JS dari 3 halaman publik + 2 auth (tanpa auth untuk JS publik)
for page in ["/", "/jadi-host", "/terms-of-service", "/forgot-password"]:
    r = s.get(base+page, timeout=30)
    jss = sorted(set(re.findall(r'/build/assets/[^\"]+\.js', r.text)))
    print("==", page, len(r.text), jss)

# download dan parse JS kunci
for js in ["landing-4Xq0rb4g.js"]:
    # nama file bisa berubah (hash), cari dari homepage
    r = s.get(base+"/", timeout=30)
    m = re.findall(r'/build/assets/landing-[^\"]+\.js', r.text)
    print("landing js:", m)
