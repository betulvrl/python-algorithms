girdi = input("bir metin ya da kod giriniz: ")
rakam_var = False 
for karakter in girdi:
    if karakter.isdigit():
        rakam_var = True
        break
if rakam_var:
    acılmısmetin = ""
    harf = ""
    sayı_metni = ""
    for karakter in girdi:
        if karakter.isdigit():
            sayı_metni += karakter
        else:
            if harf != "":
                acılmısmetin += harf * int(sayı_metni)
            harf = karakter
            sayı_metni = ""
    if harf != "":
        acılmısmetin += harf * int(sayı_metni)
    print("açılmış çıktı:", acılmısmetin)
else:
    sıkıstırılmısmetin = ""
    if len(girdi) > 0:
        harff = girdi[0]
        sayaç = 1 
        for i in range(1, len(girdi)):
            sıradakı = girdi[i]
            if sıradakı == harff:
                sayaç += 1
            else:
                sıkıstırılmısmetin += harff + str(sayaç)
                harff = sıradakı
                sayaç = 1
        sıkıstırılmısmetin += harff + str(sayaç)
    print("sıkıştıtılmıs çıktı:", sıkıstırılmısmetin)            

    