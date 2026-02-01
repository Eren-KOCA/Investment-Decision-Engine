# --- Veri Girişi ---
yillik_faiz = float(input("Yıllık Faiz Oranını Giriniz (Örn: 0.20): "))
aylik_faiz = yillik_faiz / 12  # Aylık taksitler için faizi 12'ye böldük

# SEÇENEK A: PEŞİN ALIM
pesin_fiyat = float(input("Ürünün Peşin Fiyatı: "))
bakim_masrafi = float(input("Yıllık Bakım Masrafı: "))
bakim_yili = int(input("Bakım Süresi (Yıl): "))

# SEÇENEK B: TAKSİTLİ ALIM
taksitli_pesinat = float(input("Taksitli Peşinat Miktarı: "))
taksit_tutari = float(input("Aylık Taksit Tutarı: "))
taksit_sayisi = int(input("Toplam Taksit Sayısı (Ay): "))

# --- Hesaplama ---
pv_a = pesin_fiyat
for i in range(1, bakim_yili + 1):
    # Yıllık bakım yıllık faizle çekilir
    pv_a += bakim_masrafi / (1 + yillik_faiz)**i

pv_b = taksitli_pesinat
for t in range(1, taksit_sayisi + 1):
   pv_b += taksit_tutari / (1 + aylik_faiz)**t

# --- Sonuç Raporu ---
print("-" * 30)
print(f"Peşin Alım Maliyeti (PV): {round(pv_a, 2)} TL")
print(f"Taksitli Alım Maliyeti (PV): {round(pv_b, 2)} TL")

if pv_a < pv_b:
    print(f"KARAR: Peşin alım {round(pv_b - pv_a, 2)} TL daha avantajlı.")
elif pv_b < pv_a:
    print(f"KARAR: Taksitli alım {round(pv_a - pv_b, 2)} TL daha avantajlı.")
else:
    print("KARAR: Her iki seçenek de maliyet açısından eşittir.")
