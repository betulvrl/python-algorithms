liste1 = [int(x) for x in input("1. listeyi giriniz: ").split()]
liste2 = [int(x) for x in input("2. listeyi giriniz: ").split()]
sonuc = []
i = 0
j = 0
while i < len(liste1) and j < len(liste2):
    if liste1[i] <= liste2[j]:
        sonuc.append(liste1[i])
        i += 1
    else:
        sonuc.append(liste2[j])
        j += 1
sonuc.extend(liste1[i:])
sonuc.extend(liste2[j:])
print(sonuc)