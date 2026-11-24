bolluk = 0 
for sayi in range(1, 101):
    bolen_toplamı = 0
    for i in range(1, (sayi // 2) + 1):
        if sayi % i == 0:
            bolen_toplamı += i
    if bolen_toplamı > sayi:
        bolluk += 1
print(f"1-100 arasında {bolluk} adet bolluk sayısı vardır.")              

