metin = input("Bir metin girin: ").lower()
harf_sayilari = {}
for karakter in metin:
    if karakter.isalpha():
        harf_sayilari[karakter] = harf_sayilari.get(karakter, 0) + 1
turk_alfabesi = "abcçdefgğhıijklmnoöprsştuüvyz"
print("\n--- Harf Histogramı ---")
for harf in turk_alfabesi:
    if harf in harf_sayilari:
        adet = harf_sayilari[harf]
        yildizlar = "*" * adet  
        print(f"{harf}: {yildizlar} ({adet})")