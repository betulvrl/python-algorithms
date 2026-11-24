n = int(input("tam sayi giriniz: "))
if n < 0:
    print("Negatif sayının faktöriyeli tanımsızdır")
else:
    faktoriyel = 1
    for i in range(1, n + 1):
        faktoriyel *= i  
    print(f"{n}! = {faktoriyel}")