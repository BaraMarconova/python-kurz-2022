# funkce
# print()
# sum()
# len([0,1,2])
# round(2.34,1)

# slovnik = {'1':"AB"}
# slovnik.items() #metoda
# slovnik.values()

# definice funkce
# def pozdrav(jmeno: str): # napoveda typu
#   print(f"Ahoj {jmeno}!")
# # volani
# jmeno_uzivatele = input ("Zadej sve jmeno: ")
# pozdrav(jmeno_uzivatele)

# funkce s navratovou hodnotou
# def secti_dve_cisla(a,b):
#   vysledek = a + b
#   return(vysledek) 
# # kratsi varianta
# def secti_dve_cisla(a,b):
#   return a + b

# vysledek_souctu = secti_dve_cisla(1,2)
# print(vysledek_souctu)

def prevod_eur_na_czk(pocet_eur: int, kurz: float = 25): # nepovinny parametr, urciv v definici kdyz neni vyplneny vezme se odtud
  # funkce prevadi eura na koruny
  """
  pro delsi komentar 
  pouzit tri uvozovky
  """
  return pocet_eur * kurz

print(prevod_eur_na_czk(pocet_eur=10, kurz=24.8))
print(prevod_eur_na_czk(10, kurz=24.8)) # funguje, obracene nefunguje

