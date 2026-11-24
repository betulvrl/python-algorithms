girdi = input("cümle ya da kelime giriniz: ")
metin = ""
for i in girdi:
    if i.isalpha():
        metin = metin + i.lower()
if metin == metin[::-1]:
    print("polindromdur")
else:
    print("polindrom değildir")
