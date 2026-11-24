n = int(input("bir sayı giriniz: "))
sayac = 1
for i in range(1, n + 1):
    for j in range(i):
        print(sayac, end=" ")
        sayac += 1  
    print()