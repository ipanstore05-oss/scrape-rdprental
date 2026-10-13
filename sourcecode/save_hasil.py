import pickle, pathlib, requests, urllib.parse, re, html, json, csv
s=requests.Session()
s.headers.update({'User-Agent':'Mozilla/5.0'})
cookies = pickle.loads(pathlib.Path(r"C:\Users\RENT~1.BVN\AppData\Local\Temp\opencode\otp_cookies4.pkl").read_bytes())
s.cookies.update(cookies)
out = pathlib.Path(r"C:\Users\rent.bvnqahr1\Downloads\project\hasil")
out.mkdir(exist_ok=True)

def get_props(url):
    xsrf = s.cookies.get('XSRF-TOKEN')
    if xsrf:
        s.headers.update({'X-XSRF-TOKEN': urllib.parse.unquote(xsrf)})
    r = s.get(url, timeout=30)
    data = json.loads(html.unescape(re.search(r'data-page="(.+?)"', r.text, re.DOTALL).group(1)))
    return data['props']

landing = get_props('https://rdprental.id/')
services = get_props('https://rdprental.id/account/services')
saldo = get_props('https://rdprental.id/account/saldo')

# 1. account summary (tanpa password)
summary = {
  'customer': {k:v for k,v in landing['customer'].items() if k != 'wallet'},
  'walletBalance': landing['walletBalance'],
  'canClaimTrial': landing['canClaimTrial'],
  'customerHasStorage': landing['customerHasStorage'],
  'telegramLinked': services['telegramLinked'],
  'saldo_balance': saldo['balance'],
  'storageAddons_count': len(saldo['storageAddons']),
  'transactions_count': len(saldo['transactions']),
  'rentals_count': len(services['rentals']),
}
(out/'account_summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')

# 2. rentals.csv (redaksi password)
with open(out/'rentals.csv','w',newline='',encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=['id','machine_name','package_name','status','billing_mode','is_paused','price_paid','starts_at','expires_at','can_extend','rdp_host','rdp_port'])
    w.writeheader()
    for x in services['rentals']:
        c = x.get('connection') or {}
        w.writerow({'id':x['id'],'machine_name':x['machine_name'],'package_name':x['package_name'],'status':x['status'],'billing_mode':x['billing_mode'],'is_paused':x['is_paused'],'price_paid':x['price_paid'],'starts_at':x['starts_at'],'expires_at':x['expires_at'],'can_extend':x['can_extend'],'rdp_host':c.get('host',''),'rdp_port':c.get('port','')})

# 3. transactions.csv
with open(out/'transactions.csv','w',newline='',encoding='utf-8-sig') as f:
    cols=['id','type','amount','balance_after','reference_type','reference_id','note','created_at']
    w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
    w.writeheader()
    w.writerows(saldo['transactions'])

print("saved:", list(out.iterdir()))
