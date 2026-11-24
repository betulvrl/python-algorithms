sayilar = [int(x) for x in input().split()]
en_buyuk = float("-inf")
ikinci_buyuk = float("-inf")
for sayi in sayilar:
    if sayi > en_buyuk:
        ikinci_buyuk = en_buyuk
        en_buyuk = sayi
    elif sayi > ikinci_buyuk and sayi != en_buyuk:
        ikinci_buyuk = sayi
if ikinci_buyuk == float("-inf"):
    print("İkinci en büyük yok")
else:
    print(ikinci_buyuk)