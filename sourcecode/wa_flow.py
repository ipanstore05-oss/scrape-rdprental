import re, pathlib
t = pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\landing.js").read_text(encoding="utf-8")
# cari konteks generate-code / check-verification / confirm-phone-change / wa-verify
for kw in ["generate-code", "check-verification", "confirm-phone-change", "wa-verify", "wa_verification", "telegram"]:
    print("="*15, kw)
    for m in re.finditer(r'.{0,350}'+re.escape(kw)+r'.{0,350}', t, re.IGNORECASE):
        s = m.group(0).replace("\n"," ")[:750]
        print(" ", s); print(" ---")
