import re, pathlib
tmp = pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode")
for f in ["landing.js", "saldo-BZUVpUsL.js", "services-D6EGha4H.js"]:
    p = tmp / f
    if not p.exists():
        print(f, "MISSING"); continue
    t = p.read_text(encoding="utf-8")
    print("="*20, f, len(t))
    urls = sorted(set(re.findall(r'\"(/(?:api|sewa|account)[^\"\\\']*)\"', t)))
    for u in urls:
        print(" ", u)
    # pola w.post/get ke path relatif
    calls = sorted(set(re.findall(r'w\.(post|get|put|delete)\(\s*[\"\\\']([^\"\\\']+)[\"\\\']', t)))
    for m in calls:
        print("  CALL", m)
    # kata kunci fitur
    for kw in ["trial", "storage", "topup", "extend", "relay", "invoice", "usdt", "qris", "auto_continue", "convert"]:
        c = len(re.findall(kw, t, re.IGNORECASE))
        if c: print(f"  kw {kw}: {c}x")
