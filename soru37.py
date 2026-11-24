metin = input()
durumlar = [["", metin]]

for adim in range(len(metin)):
    yeni_durumlar = []
    for kelime, kalan in durumlar:
        for i in range(len(kalan)):
            yeni_kelime = kelime + kalan[i]
            yeni_kalan = kalan[:i] + kalan[i+1:]
            yeni_durumlar.append([yeni_kelime, yeni_kalan])
    durumlar = yeni_durumlar

for kelime, kalan in durumlar:
    print(kelime, end=" ")

print()
print(len(durumlar), "permütasyon")