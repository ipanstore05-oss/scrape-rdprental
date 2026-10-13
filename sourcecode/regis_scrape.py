import pickle, pathlib, requests, urllib.parse, re, html, json
s = requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0','Accept':'text/html,application/xhtml+xml','Referer':'https://rdprental.id/'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies5.pkl").read_bytes())
s.cookies.update(cookies)
def fetch(url):
    xsrf = s.cookies.get('XSRF-TOKEN')
    if xsrf:
        s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(xsrf), 'X-Requested-With':'XMLHttpRequest'})
    r = s.get(url, timeout=30)
    data = json.loads(html.unescape(re.search(r'data-page="(.+?)"', r.text, re.DOTALL).group(1)))
    return data['props']
landing = fetch('https://rdprental.id/')
print("customer:", landing['customer'])
print("wallet:", landing.get('walletBalance'), "trial:", landing.get('canClaimTrial'), "storage:", landing.get('customerHasStorage'))
print("machines:", len(landing['machines']), "avail:", sum(1 for x in landing['machines'] if x.get('is_available')))
services = fetch('https://rdprental.id/account/services')
print("rentals:", len(services['rentals']), "telegram:", services['telegramLinked'])
saldo = fetch('https://rdprental.id/account/saldo')
print("saldo:", saldo['balance'], "tx:", len(saldo['transactions']), "storageAddons:", len(saldo['storageAddons']), "tiers:", saldo['storageTiers'], "eligible:", saldo['eligibleRentals'])
out = pathlib.Path(r"C:\Users\rent.bvnqahr1\Downloads\project\hasil\akun_baru_576.json")
out.write_text(json.dumps({"customer": landing['customer'], "walletBalance": landing['walletBalance'], "canClaimTrial": landing['canClaimTrial'], "customerHasStorage": landing['customerHasStorage'], "rentals_count": len(services['rentals']), "saldo": saldo['balance'], "transactions_count": len(saldo['transactions'])}, ensure_ascii=False, indent=2), encoding="utf-8")
print("saved", out)
open(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\regis_cookies6.pkl","wb").write(pickle.dumps(s.cookies))
