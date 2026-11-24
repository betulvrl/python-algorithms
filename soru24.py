liste_a = [x**2 for x in range(1, 21) if x % 2 == 0]
print(f"a- {liste_a}")
liste_b = [x for x in range(1, 51) if x % 3 == 0 and x % 5 != 0]
print(f"b- {liste_b}")
liste_c = [eleman for alt_liste in [[1, 2], [3, 4, 5], [6]] for eleman in alt_liste]
print(f"c- {liste_c}")
liste_d = [kelime.upper() for kelime in ["elma", "armut", "kivi", "karpuz"] if len(kelime) > 4]
print(f"d- {liste_d}")
