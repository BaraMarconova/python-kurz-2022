nazev_souboru = 'praha.txt'
with open(nazev_souboru) as vstup:
  slohova_prace = vstup.readlines()

# print(slohova_prace)

# radky = [radek.strip() for radek in slohova_prace]
# print(radky)
radky = [radek.split() for radek in slohova_prace]
print(radky)
pocet_slov = [len(slovo) for slovo in radky]
print(pocet_slov)
print(sum(pocet_slov))
