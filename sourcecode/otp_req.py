import requests, json
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Accept':'application/json', 'X-Requested-With':'XMLHttpRequest', 'Referer':'https://rdprental.id/', 'Origin':'https://rdprental.id'}
s=requests.Session()
s.headers.update(headers)
# 1. ambil csrf cookie (Laravel Sanctum)
r0=s.get('https://rdprental.id/sanctum/csrf-cookie', timeout=30)
print("csrf:", r0.status_code, dict(s.cookies))
# 2. request OTP
phone="6283115405281"
r=s.post('https://rdprental.id/api/customer/otp/request', json={'phone': phone}, timeout=30)
print("otp/request:", r.status_code)
print(r.text[:2000])
