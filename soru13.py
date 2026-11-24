a = int(input("birinci sayıyı giriniz: "))
b = int(input("ikinci sayıyı giriniz: "))
eskia = a
eskib = b 
while b != 0:
    a, b = b, a % b
ebob = a
ekok = eskia * eskib // ebob
print("EBOB", ebob)
print("EKOK", ekok)