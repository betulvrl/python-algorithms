# BÖLÜM 1: Onluk sayıyı ikiliğe çevirme (Girdi: 13, Çıktı: 1101)[cite: 1]
sayi = 13
ikilik_sonuc = ""

while sayi > 0:
    kalan = sayi % 2  # Sayıyı 2'ye böl, kalanı al (1 veya 0)
    ikilik_sonuc = str(kalan) + ikilik_sonuc  # Kalanı metin yap ve BAŞA ekle
    sayi = sayi // 2  # Sayıyı ikiye bölerek küçült

print("1. Bölüm Çıktısı:", ikilik_sonuc)


# BÖLÜM 2: İkilik metni onluk sayıya çevirme (Girdi: 101010, Çıktı: 42)[cite: 1]
ikilik_metin = "101010"
onluk_sonuc = 0
carpan = 1  # İkilik sistemde sağdan sola basamaklar 1, 2, 4, 8 diye artar

indis = len(ikilik_metin) - 1  # Kelimenin EN SONUNDAN (en sağdan) başlamak için

while indis >= 0:
    rakam = int(ikilik_metin[indis])  # O anki harfi sayıya çevir
    
    if rakam == 1:
        onluk_sonuc = onluk_sonuc + carpan  # Rakam 1 ise çarpanı toplama ekle
        
    carpan = carpan * 2  # Sola doğru bir adım kaydığımız için çarpanı 2 kat büyüt
    indis = indis - 1    # Bir soldaki karaktere geç

print("2. Bölüm Çıktısı:", onluk_sonuc)