n = int(input("bir sayı giriniz: "))  
for i in range(n , 0, -1):
    bosluklar = " " * (n - i)
    yildizlar = "*" * ((2 * i) - 1)
    print(bosluklar + yildizlar)