metin = input("Metni girin: ")
en_uzun = ""
for i in range(len(metin)):
    for sag_baslangic in (i, i + 1):
        sol, sag = i, sag_baslangic
        while sol >= 0 and sag < len(metin) and metin[sol] == metin[sag]:
            if (sag - sol + 1) > len(en_uzun):
                en_uzun = metin[sol : sag + 1]
            sol -= 1
            sag += 1
print(en_uzun)