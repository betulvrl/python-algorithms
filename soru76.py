n = int(input("n: "))
matris = [[0] * n for _ in range(n)]
ust, alt = 0, n - 1
sol, sag = 0, n - 1
sayi = 1
while ust <= alt and sol <= sag:
    for i in range(sol, sag + 1):
        matris[ust][i] = sayi
        sayi += 1
    ust += 1
    for i in range(ust, alt + 1):
        matris[i][sag] = sayi
        sayi += 1
    sag -= 1
    if ust <= alt:
        for i in range(sag, sol - 1, -1):
            matris[alt][i] = sayi
            sayi += 1
        alt -= 1
    if sol <= sag:
        for i in range(alt, ust - 1, -1):
            matris[i][sol] = sayi
            sayi += 1
        sol += 1
genislik = len(str(n * n))
for satir in matris:
    print(" ".join(f"{eleman:>{genislik}}" for eleman in satir))