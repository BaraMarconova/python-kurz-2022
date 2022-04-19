nazev_souboru = "mereni.txt"

with open(nazev_souboru) as vstup:
  mereni = vstup.readlines()

print(mereni)

radky = [den.strip() for den in mereni]
print(radky)

radky = [den.split() for den in mereni]
print(radky)
radky = [[den[0], float(den[1])] for den in radky]
print(radky)