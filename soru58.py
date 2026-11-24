gun_no = int(input("1-7 arası sayı giriniz: "))
gunler = ["", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
match gun_no:
    case 1 | 2 | 3 | 4 | 5:
        print(f"{gunler[gun_no]} (hafta içi)")
    case 6 | 7:
        print(f"{gunler[gun_no]} (hafta sonu)")
    case _:
        print("Geçersiz gün")