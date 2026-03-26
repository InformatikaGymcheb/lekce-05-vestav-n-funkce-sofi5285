# ÚLOHA 1: Zvětšovač (použij +=)
cislo = int(input("Zadej číslo: "))
# Sem doplň kód:
cislo += 10
print("Výsledek po zvětšení o 10 je:", cislo)


# ÚLOHA 2: Útrata (zaokrouhli na 2 místa)
celkem = float(input("Celková suma (Kč): "))
lidi = int(input("Počet lidí: "))
# Sem doplň výpočet a print s round():
vypocet = celkem / lidi
na_jednoho = round(vypocet, 2)
print(f"Každý má zaplatit {na_jednoho} Kč.")


# ÚLOHA 3: Plocha kruhu (zaokrouhli na celé číslo)
r = float(input("Zadej poloměr: "))
plocha = 3.14 * r * r
# Sem doplň kód:
vysledek = round(plocha)
print(f"Plocha kruhu je: {vysledek}")
