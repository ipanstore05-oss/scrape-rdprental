import requests
headers={'User-Agent':'Mozilla/5.0'}
for url in [
 "https://rdprental.id/account/services",
 "https://rdprental.id/jadi-host",
 "https://rdprental.id/register",
 "https://rdprental.id/forgot-password",
 "https://rdprental.id/terms-of-service",
]:
    try:
        r=requests.get(url, headers=headers, timeout=20, allow_redirects=False)
        print(url, r.status_code, r.headers.get('Location','')[:120], "len", len(r.text))
    except Exception as e:
        print(url, "ERR", e)
