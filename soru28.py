liste = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
aranan = int(input("Aramak istediğiniz sayıyı girin: "))
sol = 0                       
sag = len(liste) - 1           
adim = 0
bulundu_mu = False             
while sol <= sag:
    adim += 1                 
    orta = (sol + sag) // 2
    if liste[orta] == aranan:
        print(f"Çıktı: İndeks: {orta} ({adim} adım)")
        bulundu_mu = True     
        break                
    elif aranan < liste[orta]:
        sag = orta - 1         
    else:
        sol = orta + 1 
if not bulundu_mu:
    print(f"Çıktı: Bulunamadı - İndeks: -1 ({adim} adım)")