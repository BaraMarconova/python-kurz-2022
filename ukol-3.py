# funkce 1
def overeni_cisla(tel_cislo:int):
  # funkce overi spravnou delku cisla a vypise true/false, pokud jsou v cisle mezery odstrani ji
  tel_cislo = tel_cislo.replace(" ", "")
  if "+420" in tel_cislo:
    if len(tel_cislo) == 13:
      return True
  if len(tel_cislo) == 9:
    return True
  else:
    return False

# funkce 2
import math
def cena_sms(zprava):
# funkce pocita celkovou cenu za zpravu, podle poctu znaku.
  pocet_zprav = len(zprava)/180
  celkova_cena = math.ceil(pocet_zprav) * 3
  print(f'Cena zpravy je {celkova_cena}kc.')

# volani 1
tel_cislo = input("Napiste vase telefonni cislo:")
(overeni_cisla(tel_cislo))

if (overeni_cisla(tel_cislo)) == True:
  zprava = input("Napis SMS:")
  cena_sms(zprava)
else:
  print('Spatne telefonni cislo.')

