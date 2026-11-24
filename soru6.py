yil = int(input("bir yıl giriniz: "))
a = yil % 4 == 0 and yil % 100 != 0
b = yil % 400 == 0
if (a) or (b):
    print("artık yıl")
else:
    print("artık yıl değil")