sifre = input("şifre girin : ")
buyukv = False 
kucukv = False 
rakamv = False 
ozelv = False 
for karakter in sifre:
    if karakter.isupper():
        buyukv = True
    elif karakter.islower():
        kucukv = True
    elif karakter.isdigit():
        rakamv = True 
    elif karakter in "!@#$%*.:":
        ozelv = True
eksikler = []
if len(sifre) < 8: 
    eksikler.append("en az 8 karakter") 
if not buyukv:
    eksikler.append("en az 1 büyük harf")
if not kucukv:
    eksikler.append("en az 1 kucuk harf")
if not rakamv:
    eksikler.append("en az 1 rakam")
if not ozelv:
    eksikler.append("en az 1 özel karakter ") 
puan = 5 - len(eksikler)
if puan == 5:
    print("şifre güçlü")  
elif puan >= 3:
    print("orta güçte")
    print(f"şifre orta güçe sahip, eksikler: {', '.join(eksikler)}")   
else:
    print("şifre zayıf")
    print(f"eksikler: {', ' .join(eksikler)}")     


