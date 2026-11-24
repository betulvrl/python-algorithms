adlar = ["Ali", "Zeynep", "Can", "Elif"]
notlar = [72, 95, 58, 88]
ogrenciler = list(zip(adlar, notlar))
sirali_ogrenciler = sorted(ogrenciler, key=lambda x: x[1], reverse=True)
for sira, (ad, notu) in enumerate(sirali_ogrenciler, start=1):
    print(f"{sira}. {ad:8} {notu}")
ortalama = sum(notlar) / len(notlar)
print(f"ortlama: {ortalama}")
#tuple bir kez oluşturulduktan sonra içindeki veriler silinemez, güncellenemez veya yeni veri eklenemez.