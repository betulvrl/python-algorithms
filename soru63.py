n = int(input("bir sayı giriniz: "))
for sayi in range(1, n + 1):
    bolenler = []
    for i in range(1, (sayi // 2) + 1):
        if sayi % i == 0:
            bolenler.append(i)
    if sum(bolenler) == sayi and sayi > 0:
        bolen_metni = " + ".join(map(str, bolenler))
        print(f"{sayi} = {bolen_metni}")      
  
