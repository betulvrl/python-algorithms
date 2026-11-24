kelime = input("kelime giriniz: ")
kalin_var = False 
ince_var = False
for harf in kelime:
    if harf in "aıou":
        kalin_var = True
    elif harf in "eiüö":
        ince_var = True
if kalin_var == True and ince_var == True:
    print("uymaz")
else:
    print("uymakta")

