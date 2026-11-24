rehber = {}
while True:
    print("\n--- Telefon Rehberi Menüsü ---")
    print("1) Ekle")
    print("2) Ara")
    print("3) Sil")
    print("4) Listele")
    print("5) Çıkış")    
    secim = input("Seçiminiz (1-5): ")    
    if secim == "1":
        isim = input("Eklenecek kişinin adı: ")
        numara = input("Telefon numarası: ")
        rehber[isim] = numara
        print(f"{isim} eklendi.")        
    elif secim == "2":
        isim = input("Aranan kişinin adı: ")
        if isim in rehber:
            print(f"{isim}: {rehber[isim]}")
        else:
            print(f"{isim} rehberde yok.")            
    elif secim == "3":
        isim = input("Silinecek kişinin adı: ")
        if isim in rehber:
            del rehber[isim]
            print(f"{isim} rehberden silindi.")
        else:
            print(f"{isim} rehberde yok, bu yüzden silinemedi.")            
    elif secim == "4":
        if len(rehber) == 0:
            print("Rehber boş.")
        else:
            print("\n--- Rehber Listesi (Alfabetik) ---")
            for isim, numara in sorted(rehber.items()):
                print(f"{isim}: {numara}")                
    elif secim == "5":
        print("Görüşmek üzere!")
        break        
    else:
        print("Geçersiz bir seçim yaptınız, lütfen 1-5 arasında bir sayı girin.")