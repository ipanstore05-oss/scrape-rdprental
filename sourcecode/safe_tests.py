import pickle, pathlib, requests, urllib.parse, json
s=requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)','Accept':'application/json','Referer':'https://rdprental.id/','Origin':'https://rdprental.id/','X-Requested-With':'XMLHttpRequest','Content-Type':'application/json'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies9.pkl").read_bytes())
s.cookies.update(cookies)
def hdr():
    s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(s.cookies.get('XSRF-TOKEN'))})
out = {}
def run(label, method, url, payload=None):
    hdr()
    try:
        if method=='GET':
            r = s.get(url, timeout=30)
        else:
            r = s.post(url, json=payload or {}, timeout=30)
        print(f"[{label}] {method} {url} {payload} -> {r.status_code}")
        print("  ", r.text[:600].replace("\n"," "))
        out[label] = {"status": r.status_code, "body": r.text[:2000]}
    except Exception as e:
        print(f"[{label}] ERR {e}")
        out[label] = {"status": "ERR", "body": str(e)}

# 1. syarat host (GET publik? coba tanpa auth dulu)
run("jadi-host-syarat", "GET", "https://rdprental.id/jadi-host/syarat")
# 2. trial saat sudah pernah klaim -> harus 422, tidak bikin rental
run("checkout-trial-ineligible", "POST", "https://rdprental.id/sewa/checkout", {"machine_id":30,"duration_type":"trial"})
# 3. machine invalid
run("checkout-invalid-machine", "POST", "https://rdprental.id/sewa/checkout", {"machine_id":999999,"duration_type":"daily"})
# 4. topup amount 0 (invalid, tidak bikin invoice)
run("topup-amount-0", "POST", "https://rdprental.id/account/saldo/topup", {"amount":0,"gateway_method":"qris"})
# 5. storage size invalid
run("storage-invalid", "POST", "https://rdprental.id/account/storage/subscribe", {"size_gb":1})
# 6. WA generate-code (milik sendiri, aman - hanya bikin kode)
run("wa-generate-code", "POST", "https://rdprental.id/api/customer/whatsapp/generate-code", {})
# 7. end-block-preview rental cleaned 2068 (GET, read-only)
run("end-block-preview-cleaned", "GET", "https://rdprental.id/sewa/rentals/2068/end-block-preview")
# 8. notify-availability di PC penuh id 1 (subscribe notif, ringan, tidak ganggu sewa jalan)
run("notify-id1", "POST", "https://rdprental.id/sewa/machines/1/notify-availability", {})

pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\safe_tests.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies10.pkl","wb").write(pickle.dumps(s.cookies))
print("saved safe_tests.json")
