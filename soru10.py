toplam = 0
sayac = 0
while True:
    sayi = float(input("bir sayı girin (Çıkmak için 0 a basın): "))
    if sayi == 0:
        break
    if sayi < 0:
        continue
    toplam = toplam + sayi
    sayac = sayac + 1
if sayac == 0:
    print("hiç sayı girmediniz")
else:
    ortalama = toplam / sayac
    print(f"Ortalama: {ortalama}")