import re, pathlib
t = pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\services-D6EGha4H.js").read_text(encoding="utf-8")
# ganti backtick section jadi readable: cari 400 char sekitar rentals/
for m in re.finditer(r'.{0,250}/account/rentals/.{0,250}', t):
    print(m.group(0)[:600]); print("-----")
print("=====SEWA=====")
for m in re.finditer(r'.{0,250}/sewa/rentals/.{0,250}', t):
    print(m.group(0)[:600]); print("-----")
print("=====STORAGE=====")
for m in re.finditer(r'.{0,250}storage-addons.{0,250}', t):
    print(m.group(0)[:600]); print("-----")
