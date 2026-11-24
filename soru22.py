girdi = input("araya virgul koyarak sayılar giriniz: ")
parcalar = girdi.split(",")
sayilar = []
for parca in parcalar:
    gercek_sayi = int(parca)
    sayilar.append(gercek_sayi)
en_buyuk = sayilar[0]
en_kucuk = sayilar[0]
toplam = 0 
for sayi in sayilar:
    toplam += sayi
    if sayi > en_buyuk:
        en_buyuk = sayi 
    if sayi < en_kucuk:
        en_kucuk = sayi
ortalama = toplam / len(sayilar) 
print("en büyük", en_buyuk)
print("en küçük", en_kucuk)
print("ortalama", ortalama)
