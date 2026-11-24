metin = input("bir metin giriniz: ")
unluler = "aeıioöuüAEIİOÖUÜ"
unlu_sayisi = 0
unsuz_sayisi = 0
for karakter in metin:
    if karakter.isalpha():
        if karakter in unluler:
            unlu_sayisi += 1
        else:
            unsuz_sayisi += 1
print(f"Ünlü: {unlu_sayisi}")
print(f"Ünsüz: {unsuz_sayisi}")