saniye = int(input("saniye giriniz. "))
saat = saniye // 3600
kalan_saniye = saniye % 3600
dakika = kalan_saniye // 60
s = kalan_saniye % 60
print(f"{saat} saat, {dakika} dakika, {s} saniye.")