import requests, urllib.parse
s=requests.Session()
base_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36','Accept':'application/json','X-Requested-With':'XMLHttpRequest','Referer':'https://rdprental.id/','Origin':'https://rdprental.id'}
s.headers.update(base_headers)
r0=s.get('https://rdprental.id/sanctum/csrf-cookie', timeout=30)
print("cookies:", dict(s.cookies))
xsrf = s.cookies.get('XSRF-TOKEN')
print("xsrf raw:", (xsrf or "")[:120])
if xsrf:
    xsrf_decoded = urllib.parse.unquote(xsrf)
    s.headers.update({'X-XSRF-TOKEN': xsrf_decoded})
    print("header set, len", len(xsrf_decoded))
phone="6283115405281"
r=s.post('https://rdprental.id/api/customer/otp/request', json={'phone': phone}, timeout=30)
print("otp/request:", r.status_code)
print(r.text[:3000])
print("cookies after:", dict(s.cookies))
# simpan cookies untuk step verify nanti
import pathlib
pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_session.json").write_text(requests.utils.dict_from_cookiejar(s.cookies).__str__())
# simpan full session via pickle
import pickle
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies.pkl","wb").write(pickle.dumps(s.cookies))
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_headers.json","w").write(str(dict(s.headers)))
