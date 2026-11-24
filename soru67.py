alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
metin = input("Metni girin: ")
k = int(input("Kaydırma miktarını girin: "))
sonuc = ""
for karakter in metin:
    if karakter in alfabe:
        konum = alfabe.index(karakter)
        yeni_konum = (konum + k) % 29
        sonuc += alfabe[yeni_konum]
    else:
        sonuc += karakter
print("Çıktı:", sonuc)