a = int(input("1. kenarı giriniz: "))
b = int(input("2. kenarı giriniz: "))
c = int(input("3. kenarı giriniz: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        tur = "Eşkenar"
    elif a == b or a == c or b == c:
        tur = "İkizkenar"
    else:
        tur = "Çeşitkenar"
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print(f"{tur} (dik) üçgen")
    else:
        print(f"{tur} üçgen")
else:
    print("Üçgen oluşturmaz")