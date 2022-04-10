nazev_souboru = input("Zadej nazev souboru:")

with open(nazev_souboru) as vstup:
  auta = vstup.readlines()

auta_split = [auto.split() for auto in auta]
auta_prevod_cisla = [[auto[0], float(auto[1].replace(",","."))] for auto in auta_split]

soucet_km = sum([(auto[1]) for auto in auta_prevod_cisla])
print(soucet_km)