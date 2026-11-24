def tr_buyuk(metin):
    metin = metin.replace("i", "İ").replace("ı", "I")
    buyukm = metin.upper()
    return buyukm
girdi = input("kurum adı giriniz: ")
buyyuuk = tr_buyuk(girdi)
print("Çıktı:")
print(buyyuuk)
kelimeler = girdi.split()
kısaltma = ""
for kelime in kelimeler:
    ilkharf = kelime[0]
    buyuk_harf = tr_buyuk(ilkharf)
    kısaltma = kısaltma + buyuk_harf
print("kısaltma:", kısaltma)    