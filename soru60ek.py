gizli = 25
sayac = 0
max_hak = 5
while sayac < max_hak:
    tahmin = int(input("bir sayı giriniz: "))
    sayac += 1
    if tahmin > gizli:
        print("Daha küçük")
    elif tahmin < gizli:
        print("Daha büyük")
    else:
        print(f"Bildiniz! {sayac} denemede buldunuz.")
        break
else:
    print(f"Hakkınız bitti! Gizli sayı {gizli} idi.")