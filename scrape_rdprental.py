"""Scraper publik rdprental.id — tanpa login.
Mengambil data-page Inertia dari / dan /sewa, output JSON + CSV.
Jalankan: python scrape_rdprental.py
"""
import re, json, html, csv, pathlib, urllib.request

BASE = "https://rdprental.id"
OUT_DIR = pathlib.Path(__file__).parent / "hasil"
OUT_DIR.mkdir(exist_ok=True)

def fetch_machines(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        text = r.read().decode("utf-8", errors="replace")
    m = re.search(r'data-page="(.+?)"', text, re.DOTALL)
    if not m:
        raise RuntimeError(f"data-page tidak ketemu di {url}")
    data = json.loads(html.unescape(m.group(1)))
    return data["props"]

def main():
    props = fetch_machines(BASE + "/")
    machines = props.get("machines", [])
    print(f"TOTAL PC: {len(machines)}")
    avail = [x for x in machines if x.get("is_available")]
    print(f"TERSEDIA (bisa sewa langsung): {len(avail)}")

    # simpan JSON mentah
    (OUT_DIR / "machines.json").write_text(json.dumps(machines, ensure_ascii=False, indent=2), encoding="utf-8")

    # simpan CSV ringkas
    cols = ["id","name","package_name","cpu","ram_gb","gpu","gpu_vram_gb","storage",
            "os_name","upload_mbps","download_mbps",
            "price_hourly","price_daily","price_weekly","price_monthly",
            "is_available","under_maintenance","uptime_percent","connection_mode",
            "provisioning_type","reviews_avg_rating","reviews_count","rental_expires_at"]
    with open(OUT_DIR / "machines.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(machines)

    print("\n== YANG BISA DISEWA SEKARANG ==")
    for x in avail:
        print(f"- [{x['id']}] {x['name']} | {x['package_name']} | Rp{x['price_hourly']}/jam | uptime {x['uptime_percent']}% | {x['cpu']} | RAM {x['ram_gb']}GB | {x['gpu']}")

    print("\n== PENUH / TIDAK BISA DISEWA ==")
    for x in machines:
        if not x.get("is_available"):
            status = "maintenance" if x.get("under_maintenance") else f"disewa s/d {x.get('rental_expires_at')}"
            print(f"- [{x['id']}] {x['name']} | {x['package_name']} | {status}")

    print(f"\nFile tersimpan di: {OUT_DIR.resolve()}")

if __name__ == "__main__":
    main()
