girdi = input("üç sayı giriniz: ")
parcalar = girdi.split(",")
a = int(parcalar[0])
b = int(parcalar[1])
c = int(parcalar[2])

if a < b:
    a, b = b, a

if a < c:
    a, c = c, a

if b < c:
    b, c = c, b

print(f"{a} {b} {c}")