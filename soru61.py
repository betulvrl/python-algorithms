sayi = int(input("bir sayı giriniz: "))
toplam = 0
ters = 0
while sayi > 0:
    basamak = sayi % 10          
    toplam += basamak            
    ters = ters * 10 + basamak   
    sayi //= 10                  
print(f"Basamak toplamı: {toplam}")
print(f"Tersi: {ters}")