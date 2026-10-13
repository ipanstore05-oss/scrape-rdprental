import requests, re
headers={'User-Agent':'Mozilla/5.0'}
j=open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\landing.js",encoding="utf-8").read()
# potong sekitar otp
for m in re.finditer(r'.{0,300}otp.{0,300}', j, re.IGNORECASE):
    print(m.group(0)[:700])
    print("======")
    if "======" in m.group(0):
        break
