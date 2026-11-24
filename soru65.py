sayi = int(input("roma sayısı ya da normal sayı girin: "))
if sayi < 1 or sayi > 3999:
    print("Geçersiz sayı")
else:
    roma_tablosu = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
        (1, "I")
    ]
    roma_metni = ""
    for deger, sembol in roma_tablosu:
        while sayi >= deger:
            roma_metni += sembol
            sayi -= deger
    print(roma_metni)