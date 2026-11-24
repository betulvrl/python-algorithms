# Kullanıcıdan satır sayısını alıyoruz pascal seysi
n = int(input())

for i in range(n):
    sayi = 1
    for j in range(i + 1):
        print(sayi, end=" ")
        # Sıradaki Pascal elemanını formülle doğrudan hesaplar
        sayi = sayi * (i - j) // (j + 1)
    print()