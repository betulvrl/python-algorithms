sayi = int(input("bir tam sayı giriniz: "))
if sayi == 0:
    print("sıfır")
else:
    if sayi > 0:
        isaret = "pozitif"
    else:
        isaret = "negatif"
    if sayi % 2 == 0:
        durum = "çift"
    else:
        durum = "tek"
    print(f"{isaret} {durum} sayı")
                        

        