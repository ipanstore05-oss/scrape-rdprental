import requests, re, pathlib
headers={'User-Agent':'Mozilla/5.0'}
# 1. cek dashboard tanpa login
r=requests.get('https://rdprental.id/dashboard', headers=headers, timeout=30, allow_redirects=False)
print("dashboard no-login:", r.status_code, r.headers.get('Location',''))

# 2. ambil JS landing + app untuk cari endpoint API
for js in [
 "https://rdprental.id/build/assets/landing-4Xq0rb4g.js",
 "https://rdprental.id/build/assets/app-Bz2uBCX0.js",
]:
    try:
        j=requests.get(js, headers=headers, timeout=30)
        print(js, len(j.text))
        # cari pola url/api/route
        found=sorted(set(re.findall(r'/(?:api|machines|rentals?|rental|order|sewa|topup|saldo|balance|payment|pay|checkout|cart|dashboard)[\w\-/]*', j.text)) )[:100]
        print("  endpoints:", found[:40])
        # cari axios/fetch post
        posts=re.findall(r'(?:post|get|put|\"url\")\s*[:\(]\s*[\"\\\']([^\"\\\']+)[\"\\\']', j.text)[:40]
        print("  calls:", posts[:20])
    except Exception as e:
        print("err", e)

# 3. cek sanctum csrf
r2=requests.get('https://rdprental.id/sanctum/csrf-cookie', headers=headers, timeout=30)
print("csrf-cookie:", r2.status_code, r2.headers.get('Set-Cookie','')[:200])
