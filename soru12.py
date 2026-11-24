n = int(input("bir sayı giriniz: "))  
for i in range(1, n + 1):
    bosluklar = " " * (n - i)
    yildizlar = "*" * ((2 * i) - 1)
    print(bosluklar + yildizlar)