A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
toplam_matrisi = []
for i in range(3):
    satir = []
    for j in range(3):
        satir.append(A[i][j] + B[i][j])
    toplam_matrisi.append(satir)
carpim_matrisi = []
for i in range(3): 
    satir = []
    for j in range(3): 
        hucre_degeri = 0
        for k in range(3): 
            hucre_degeri += A[i][k] * B[k][j]
        satir.append(hucre_degeri)
    carpim_matrisi.append(satir)        
transpoz_matrisi = []
for i in range(3):
    satir = []
    for j in range(3):
        satir.append(A[j][i]) 
    transpoz_matrisi.append(satir)
print("Toplam:")
for satir in toplam_matrisi:
    print(satir)
print("Çarpım:")
for satir in carpim_matrisi:
    print(satir)
print("Transpoz:")
for satir in transpoz_matrisi:
    print(satir)    