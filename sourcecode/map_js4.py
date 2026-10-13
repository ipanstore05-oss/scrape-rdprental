import re, pathlib
tmp = pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode")
for f in ["landing.js", "services-D6EGha4H.js"]:
    t = (tmp/f).read_text(encoding="utf-8")
    print("="*20, f)
    # semua pola /sewa/... termasuk template literal backtick
    pats = sorted(set(re.findall(r'/sewa/[A-Za-z0-9/\-_${}]+', t)))
    for p in pats: print(" ", p)
    pats2 = sorted(set(re.findall(r'/account/[A-Za-z0-9/\-_${}]+', t)))
    for p in pats2: print(" ", p)
    pats3 = sorted(set(re.findall(r'/api/[A-Za-z0-9/\-_${}]+', t)))
    for p in pats3: print(" ", p)
