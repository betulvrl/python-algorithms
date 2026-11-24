girdi1 = "Matematik, Fizik, Programlama, Tarih"
girdi2 = "Programlama, Kimya, Matematik, Felsefe"
kume1 = set(girdi1.split(", "))
kume2 = set(girdi2.split(", "))
ortak = kume1 & kume2
yalnizca_1 = kume1 - kume2
yalnizca_2 = kume2 - kume1
toplam_farkli = kume1 | kume2
sadece_biri = kume1 ^ kume2
print(f"Ortak: {sorted(ortak)}")
print(f"Yalnızca 1. öğrenci: {sorted(yalnizca_1)}")
print(f"Yalnızca 2. öğrenci: {sorted(yalnizca_2)}")
print(f"Toplam farklı ders: {len(toplam_farkli)}") 
print(f"Yalnızca birinin aldığı: {sorted(sadece_biri)}")