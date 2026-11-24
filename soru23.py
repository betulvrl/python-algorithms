girdi = input("bir liste ve k değeri giriniz örnek : 1 2 3 4 5, 2: ")
parcalar = girdi.split(",")
liste_kismi = parcalar[0]
k_kismi = parcalar[1]
liste = []
for sayi in liste_kismi.split():
    liste.append(int(sayi))
k = int(k_kismi.strip())
n = len(liste)
k_gercek = k % n
if k_gercek == 0:
    sonuc = liste
else:
    sag_parca = liste[-k_gercek:]
    sol_parca = liste[:-k_gercek]
    sonuc = sag_parca + sol_parca
print(sonuc)    

