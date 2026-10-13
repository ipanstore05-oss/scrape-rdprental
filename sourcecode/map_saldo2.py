import re, pathlib
t = pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\saldobundle.js").read_text(encoding="utf-8")
for m in re.finditer(r'.{0,300}saldo/topup.{0,300}', t):
    print(m.group(0)[:700]); print("-----")
print("=====STORAGE=====")
for m in re.finditer(r'.{0,300}storage/subscribe.{0,300}', t):
    print(m.group(0)[:700]); print("-----")
print("=====RENTALS S=====")
for m in re.finditer(r'.{0,300}/account/rentals/\$.{0,300}', t):
    print(m.group(0)[:700]); print("-----")
