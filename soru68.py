cumle = input("Cümleyi girin: ")
kelimeler = cumle.split()
toplam_uzunluk = 0
en_uzun = ""
kelime_sayisi = 0
for kelime in kelimeler:
    temiz = kelime.strip('.,;:!?"\'')
    if temiz:
        kelime_sayisi += 1
        toplam_uzunluk += len(temiz)
        if len(temiz) > len(en_uzun):
            en_uzun = temiz
ortalama = toplam_uzunluk / kelime_sayisi if kelime_sayisi > 0 else 0
print("Kelime sayısı:", kelime_sayisi)
print("En uzun kelime:", en_uzun)
print(f"Ortalama uzunluk: {ortalama:.2f}")