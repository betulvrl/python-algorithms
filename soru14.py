n = int(input("bir sayı giriniz: "))
adım = 0 
print(n, end=" ")
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    adım += 1
    print(n, end=" ")
print(f"\n{adım} adım")
