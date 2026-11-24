gizli = 37
sayac = 0
while True:
    tahmin = int(input("bir sayı tahmin ediniz: "))
    sayac += 1
    if tahmin > gizli:
        print("Daha küçük")
    elif tahmin < gizli:
        print("Daha büyük")
    else:
        print(f"Bildiniz! {sayac} denemede buldunuz.")
        break