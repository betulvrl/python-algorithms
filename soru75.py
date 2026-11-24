def parcala(liste, k):
    return [liste[i : i + k] for i in range(0, len(liste), k)]
def duzlestir(ic_ice):
    return [eleman for alt_liste in ic_ice for eleman in alt_liste]
liste = [int(x) for x in input().split()]
k = int(input())
parcali = parcala(liste, k)
print(parcali)
print(duzlestir(parcali))