puan = int(input("Puanınızı giriniz: "))
if puan < 0 or puan > 100:
    print("geçersiz not")
elif puan >= 90:
    print("AA")
elif puan >= 85:
    print("BA")
elif puan >= 80:
    print("BB")
elif puan >= 75:
    print("CB")
elif puan >= 70:
    print("CC")
elif puan >= 65:
    print("DC")
elif puan >= 60:
    print("DD")
elif puan >= 50:
    print("FD")
else:
    print("FF")
