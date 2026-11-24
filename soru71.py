birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
def uc_basamak_cevir(n):
    parcalar = []
    yuz = n // 100
    on = (n % 100) // 10
    bir = n % 10
    if yuz == 1:
        parcalar.append("yüz")
    elif yuz > 1:
        parcalar.append(birler[yuz] + " yüz")
    if on > 0:
        parcalar.append(onlar[on])
    if bir > 0:
        parcalar.append(birler[bir])
    return " ".join(parcalar)
sayi = int(input("Sayıyı girin: "))
if sayi == 0:
    print("sıfır")
else:
    sonuc = []
    binler = sayi // 1000
    kalan = sayi % 1000
    if binler == 1:
        sonuc.append("bin")
    elif binler > 1:
        sonuc.append(uc_basamak_cevir(binler) + " bin")
    if kalan > 0:
        sonuc.append(uc_basamak_cevir(kalan))
    print(" ".join(sonuc))