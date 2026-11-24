graf = {
    "Uşak": {"Afyon": 115, "Manisa": 165, "Denizli": 150},
    "Afyon": {"Uşak": 115, "Eskişehir": 145, "Konya": 225},
    "Manisa": {"Uşak": 165, "İzmir": 40},
    "Denizli": {"Uşak": 150, "İzmir": 225},
    "İzmir": {"Manisa": 40, "Denizli": 225},
    "Eskişehir": {"Afyon": 145, "Ankara": 235},
    "Konya": {"Afyon": 225, "Ankara": 260},
    "Ankara": {"Eskişehir": 235, "Konya": 260}
}

girdi = input().split(",")
bas, hedef = girdi[0].strip(), girdi[1].strip()

if bas not in graf or hedef not in graf:
    print("Bilinmeyen şehir")
else:
    mesafe = {bas: 0}
    rota = {bas: [bas]}
    bekleyen = [bas]

    while bekleyen:
        en_yakin = bekleyen[0]
        for s in bekleyen:
            if mesafe[s] < mesafe[en_yakin]:
                en_yakin = s
        bekleyen.remove(en_yakin)

        for komsu in graf[en_yakin]:
            yeni = mesafe[en_yakin] + graf[en_yakin][komsu]
            if komsu not in mesafe or yeni < mesafe[komsu]:
                mesafe[komsu] = yeni
                rota[komsu] = rota[en_yakin] + [komsu]
                if komsu not in bekleyen:
                    bekleyen.append(komsu)

    print("Mesafe:", mesafe[hedef], "km")
    print("Rota:", " → ".join(rota[hedef]))