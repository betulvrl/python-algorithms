girdi = input("Sayıları aralarında boşluk bırakarak girin: ")
sayilar_kabarcik = []
for x in girdi.split():
    sayilar_kabarcik.append(int(x))    
sayilar_secmeli = sayilar_kabarcik.copy() 
takas_kabarcik = 0
uzunluk = len(sayilar_kabarcik)
for i in range(uzunluk):
    for j in range(uzunluk - 1):
        if sayilar_kabarcik[j] > sayilar_kabarcik[j + 1]:
            sayilar_kabarcik[j], sayilar_kabarcik[j + 1] = sayilar_kabarcik[j + 1], sayilar_kabarcik[j]
            takas_kabarcik += 1 
takas_secmeli = 0
uzunluk_s = len(sayilar_secmeli)
for i in range(uzunluk_s):
    en_kucuk_indeks = i    
    for j in range(i + 1, uzunluk_s):
        if sayilar_secmeli[j] < sayilar_secmeli[en_kucuk_indeks]:
            en_kucuk_indeks = j 
    if en_kucuk_indeks != i:
        sayilar_secmeli[i], sayilar_secmeli[en_kucuk_indeks] = sayilar_secmeli[en_kucuk_indeks], sayilar_secmeli[i]
        takas_secmeli += 1
print(f"\nKabarcık: {sayilar_kabarcik} ({takas_kabarcik} takas)")
print(f"Seçmeli: {sayilar_secmeli} ({takas_secmeli} takas)")