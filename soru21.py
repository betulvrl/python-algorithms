metin = input("bir metin giriniz: ")
genislik = int(input("genişlik giriniz: "))
mevcut_satir = []
mevcut_uzunluk = 0 
for kelime in metin.split():
    if kelime in metin.split():
        if mevcut_uzunluk + len(kelime) + (1 if mevcut_satir else 0) > genislik:
            print(" ".join(mevcut_satir))
            mevcut_satir = [kelime]
            mevcut_uzunluk = len(kelime)
        else:
            mevcut_satir.append(kelime)
            mevcut_uzunluk += len(kelime) + (1 if mevcut_satir else 0)
if mevcut_satir:
        print(" ".join(mevcut_satir))            

