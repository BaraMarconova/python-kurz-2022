# nasobeni
# def mult(a:int,b:int):
#   return(a*b)

# vysledek_nasobeni = mult(4,8)
# print(vysledek_nasobeni)

# hotel

# def total_price(persons:int, breakfast=False):
#   cena_za_noc = 850
#   cena_za_snidani = 125
#   if breakfast:
#     vysledna_cena = persons * (cena_za_noc + cena_za_snidani) 
#   else:
#     vysledna_cena = persons * cena_za_noc
#   return vysledna_cena

# print(total_price(3, False))

# bonus
# def month_of_birth(rodne_cislo):
#   if (int(rodne_cislo[2])) >= 2:
#     mesic = int(rodne_cislo[2:4]) - 50
#   else:
#     mesic = int(rodne_cislo[2]+rodne_cislo[3])
#   return(mesic)

# rodne_cislo = input("zadej rodne cislo:")
# print(month_of_birth(rodne_cislo))

#ruleta
import random
def ruleta():
  nahodne_cislo = random.randit