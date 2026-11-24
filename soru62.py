n = int(input("bir sayı giriniz: "))
asal_sayi = 0
for sayi in range(2, n + 1):
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            break
    else:
        print(sayi, end=" ")
        asal_sayi += 1
if asal_sayi > 0:
    print()
    print(f"{asal_sayi} asal sayı")     
else:
    print("asal sayı yok")          

