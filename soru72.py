girdi = input("bosluklarla sayılar giriniz: ").split()
sayilar = [int(x) for x in girdi]
benzersiz = []
for sayi in sayilar:
    if sayi not in benzersiz:
        benzersiz.append(sayi)
print(benzersiz)