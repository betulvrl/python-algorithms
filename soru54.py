girdi = input("vize ve final notlarınızı araya virgul koyarak anlatınız: ")
notlar = girdi.split(",")
vize = float(notlar[0])
final = float(notlar[1])
son_not = (vize * 0.4) + (final * 0.6)
gectimi = son_not >= 50 
print("ortalama", son_not)
print("geçti mi", gectimi)