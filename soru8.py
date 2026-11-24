sayı1 = float(input("1. sayıyı giriniz: "))
işlem = input("bir işelem işareti giriniz '+, -, *, /, **, %' gibi: ")
sayı2 = float(input("2. sayıyı giriniz: "))
match işlem:
    case "+":
        print(sayı1 + sayı2)
    case "-":
        print(sayı1 - sayı2)
    case "*":
        print(sayı1 * sayı2)
    case "/":
        print(sayı / sayı2)
    case "**":
        print(sayı1 ** sayı2)
    case "/" if sayi2 == 0:
        print("sıfıra bölünemez")    
    case "%":
        print(sayı1 % sayı2)
    case _:
        print("Geçersiz işlem")   