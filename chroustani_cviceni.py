# # cviceni 1
# cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
# nasobky_dvema = [cislo * 2 for cislo in cisla]
# print(nasobky_dvema)

# opacne_znamenko = [0 - cislo for cislo in cisla]
# print(opacne_znamenko)

# retezec = [ str(cislo) for cislo in cisla]
# print(retezec)

# #  cviceni 2
# jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']
# pocty_pismen = [len(jmeno) for jmeno in jmena]
# print(pocty_pismen)
# velka_jmena = [jmeno.upper() for jmeno in jmena]
# print(velka_jmena)
# zenska_jmena = [jmeno+'a' for jmeno in jmena]
# print(zenska_jmena)

#  cviceni 3
teploty = [
  [2.1, 5.2, 6.1, -0.1],
  [2.2, 4.8, 5.6, -1.0],
  [3.3, 6.5, 5.9, 1.2],
  [2.9, 5.6, 6.0, 0.0],
  [2.0, 4.6, 5.5, -1.2],
  [1.0, 3.2, 2.1, -2.0],
  [0.4, 2.7, 1.3, -2.8]
]
prumery = [sum(den)/len(den) for den in teploty]
print(prumery)
ranni_teploty = [den[0] for den in teploty]
print(ranni_teploty)

poledni_nocni = [[den[1],den[3]] for den in teploty]
print(poledni_nocni)