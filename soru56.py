agirlik = float(input("ağırlık giriniz: "))
if agirlik <= 0:
    print("Geçersiz ağırlık")
elif agirlik <= 1:
    print("Ücret: 30 TL")
elif agirlik <= 5:
    print("Ücret: 50 TL")
elif agirlik <= 20:
    ucret = 50 + (agirlik - 5) * 8
    print(f"Ücret: {ucret:g} TL")
else:
    print("Kargo kabul edilmez")