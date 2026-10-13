# Laporan Scrape rdprental.id

Tanggal: 13 Okt 2026. Akun uji: `6283115405281` (id 533, lama) dan `6285117834250` (id 576, baru).
Sesi rental aktif 2073 (metered, akun 533) tidak diganggu selama pengujian.

## 1. Fitur yang SUDAH di-scrape / di-tes

| # | Fitur | Endpoint / Cara | Hasil | Bukti |
|---|-------|-----------------|-------|-------|
| 1 | Marketplace publik | `GET /`, `GET /sewa` (Inertia `public/landing`, `data-page`) | 24 PC, 5–6 available (30, 63, 71, 78, 82; belakangan + PC-2). Harga, spek, uptime, Direct/Relay, review | `hasil/machines.csv`, `hasil/machines.json` |
| 2 | Login OTP customer | `GET /sanctum/csrf-cookie` → header `X-XSRF-TOKEN`, `POST /api/customer/otp/request {phone}`, `POST /api/customer/otp/verify {phone, otp, name?}` | 533 login OK; tanpa nama pun lolos | — |
| 3 | Regis nomor baru | Alur yang sama di sesi fresh | 576 teregistrasi (`phone_verified_at`, `wa_verified_at` 13 Okt) | `hasil/akun_baru_576.json` |
| 4 | Verifikasi WhatsApp | `POST /api/customer/whatsapp/generate-code {phone}` → `{code, wa_link, owner_phone}`, `POST .../check-verification`, `POST .../confirm-phone-change` (mismatch) | Kode `DENT` ke `628116204121`; `false` → `true` setelah kirim | — |
| 5 | Alternatif Telegram | Link `t.me/RdpRentalBot`, `telegramLinked:false` di kedua akun | Terpetakan, tidak dieksekusi | `hasil/account_summary.json` |
| 6 | Trial gratis | `POST /sewa/checkout {machine_id:30, duration_type:trial}` | Rental 2075 `provisioning` → `active` di `direct30.rdprental.id:20043`; `canClaimTrial` 576 jadi `False`. Akun 533 ditolak 422 (sudah pakai 6 Okt) | `hasil/trial_576.json` |
| 7 | Checkout QRIS (block) | `POST /sewa/checkout {machine_id:30, duration_type:hourly, hours:2}` (1 jam ditolak: minimal 2). Poll `GET /sewa/rentals/{id}/status`, `POST .../check-now` | Rental 2074 `pending_payment`, Rp4.000 (unik 4.446), expired 20:13 WIB | `hasil/rentals.csv` |
| 8 | Cek rental | `GET /account/services` (`public/services`) | 12 rental (2074 pending, 2073 active metered, 10 riwayat). Koneksi host/port tanpa password di CSV | `hasil/rentals.csv` |
| 9 | Saldo + riwayat | `GET /account/saldo` (`public/saldo`) | Lama: 3.987 (turun dari 4.280 karena metered jalan), 50 transaksi. Baru: 0/0 | `hasil/transactions.csv`, `hasil/account_summary.json` |
| 10 | Topup beneran | `POST /account/saldo/topup {amount:10000, gateway_method:qris}`, `GET .../topup/{id}/status`, `POST .../check-now` | Topup 878 Rp10.000 (unik 10.159), expired 20:50 WIB, status `pending` | `hasil/topup_576.json` |
| 11 | Storage | Tier 50/100/250GB (Rp70/110/210). `POST /account/storage/subscribe {size_gb:1}` → 422; `{50}` dengan saldo 0 → 422 saldo tidak cukup | Validasi terbukti, langganan nunggu topup lunas | `hasil/safe_tests.json` |
| 12 | Notif PC penuh | `POST /sewa/machines/1/notify-availability` | `200 {ok:true}` (PC-1) | `hasil/safe_tests.json` |
| 13 | Validasi error | Trial ineligible, machine 999999, topup 0, preview rental cleaned 2068 (`422 tidak bisa diakhiri`) | Semua 422 tanpa efek samping | `hasil/safe_tests.json` |
| 14 | Halaman statis | `GET /jadi-host`, `GET /jadi-host/syarat`, `GET /terms-of-service`, `GET /privacy-policy`, `GET /forgot-password`, `GET /login` (Panel Admin) | Judul + bundle JS teridentifikasi | — |
| 15 | Logout customer | `POST /api/customer/logout` | Terpetakan dari bundle | — |

## 2. Link / URL yang sudah di-scrape

### Halaman (GET)
- `https://rdprental.id/` — landing + `data-page.machines`
- `https://rdprental.id/sewa` — sama dengan `/`
- `https://rdprental.id/account/services` — rental + koneksi (auth)
- `https://rdprental.id/account/saldo` — saldo, transaksi, tier storage (auth)
- `https://rdprental.id/jadi-host` — info host
- `https://rdprental.id/jadi-host/syarat` — syarat host
- `https://rdprental.id/terms-of-service`
- `https://rdprental.id/privacy-policy` (terdaftar di bundle, belum di-fetch isi)
- `https://rdprental.id/forgot-password`
- `https://rdprental.id/login` — Panel Admin (email+password), redirect target `/dashboard`
- `https://rdprental.id/dashboard` — tanpa login 302 ke `/login`
- `https://rdprental.id/sanctum/csrf-cookie` — cookie `XSRF-TOKEN` + sesi

### API customer/auth (POST)
- `/api/customer/otp/request`, `/api/customer/otp/verify`, `/api/customer/logout`
- `/api/customer/whatsapp/generate-code`, `/api/customer/whatsapp/check-verification`, `/api/customer/whatsapp/confirm-phone-change`

### Sewa (POST/GET)
- `POST /sewa/checkout`, `GET /sewa/rentals/{id}/status`, `POST /sewa/rentals/{id}/check-now`, `POST /sewa/rentals/{id}/cancel-pending` (terpetakan, belum dieksekusi), `POST /sewa/machines/{id}/notify-availability`, `POST /sewa/rentals/{id}/end-metered-session` (terpetakan, SENGAJA tidak dieksekusi), `GET /sewa/rentals/{id}/end-block-preview`, `POST /sewa/rentals/{id}/restart`, `POST /sewa/rentals/{id}/reset-account`

### Akun/saldo/storage (POST/GET)
- `POST /account/rentals/{id}/extend`, `POST .../extend/check-now`, `POST .../extend-saldo`, `POST .../extra-ports`, `POST .../activate-relay`, `POST .../deactivate-relay`, `POST .../convert-to-block`, `POST .../approve-auto-continue` (terpetakan, tidak dieksekusi)
- `POST /account/saldo/topup`, `GET /account/saldo/topup/{id}/status`, `POST .../check-now`
- `POST /account/storage/subscribe`, `POST /account/storage-addons/{id}/cancel` (terpetakan)

### Host (terpetakan)
- `/api/host/otp/request`, `/api/host/otp/verify`, `/api/host/logout`

### Pembayaran
- `https://www.iniaku.my.id/pay/checkout/e0j5YrmSZJ2M6c3fKqsLDtKWtdKSiB22` — QRIS sewa 2074 (Rp4.446)
- `https://www.iniaku.my.id/pay/checkout/XJ0LFvfHDEe4Yvz6jq6VScIfwM4j2bLR` — QRIS topup 878 (Rp10.159)
- `https://www.iniaku.my.id/images/qris-gopay.png` — gambar QR

## 3. Yang BELUM di-scrape / di-tes

1. Bayar QRIS 2074 + 878 sampai `paid` (invoice masih `pending`, butuh bayar manual).
2. `cancel-pending` 2074 (batal aman, belum dieksekusi).
3. Retry `storage/subscribe 50GB` setelah topup 878 lunas.
4. `extend`, `extend-saldo`, `extra-ports`, `activate/deactivate-relay`, `convert-to-block`, `approve-auto-continue` (khusus rental cleaned biar aman).
5. `end-metered-session`, `restart`, `reset-account` pada 2073 (berbahaya, butuh izin eksplisit).
6. Link Telegram `t.me/RdpRentalBot` sampai akun ke-link.
7. Regis host full (`/api/host/...` butuh nomor host kedua).
8. `/dashboard` admin (butuh kredensial admin; `/login` hanya di-fetch).
9. `privacy-policy` isi lengkap, `reset-password/{token}`, `email/verify`.
10. Pembayaran USDT TRC-20 dan `payment_method:saldo` untuk block.
11. Kredensial RDP penuh (user/pass trial 2075 + 2073) — disensor di CSV, aslinya di `/account/services` sesi masing-masing.

## 4. File bukti di `hasil/`

`machines.csv`, `machines.json`, `rentals.csv`, `transactions.csv`, `account_summary.json`, `akun_baru_576.json`, `trial_576.json`, `topup_576.json`, `safe_tests.json`.
