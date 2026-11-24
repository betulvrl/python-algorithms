eposta = input("E-posta adresini girin: ")
if " " in eposta:
    print("Geçersiz: boşluk içermemeli")
elif eposta.count("@") != 1:
    print("Geçersiz: tam olarak bir @ olmalı")
else:
    kullanici, alan = eposta.split("@")
    if kullanici == "":
        print("Geçersiz: kullanıcı adı boş")
    elif alan.count(".") == 0 or alan.startswith(".") or alan.endswith("."):
        print("Geçersiz: alan adı hatalı")
    else:
        print("Geçerli")