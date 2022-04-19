class Balik:
  def __init__(self, adresa, hmotnost, doruceno=False):
    self.adresa = adresa
    self.hmotnost = hmotnost
    self.doruceno = doruceno
  
  def deliver (self):
    self.doruceno = True

  def __str__(self):
    if self.doruceno:
      return f"Balik ma adrsu {self.adresa}. vazi {self.hmotnost} kg a byl dorucen"
    else:
      return f"Balik ma adrsu {self.adresa}. vazi {self.hmotnost} kg a nebyl dorucen"

balik = Balik('Humpolecka 21', 10) 
print(balik)
balik.deliver()
print(balik) 


# 2 
# class Kniha:
#   def __init__(self, nazev, pocet_stran, cena):
#     self.nazev = nazev
#     self.pocet_stran = pocet_stran
#     self.cena = cena

#   def __str__(self):
#     return f"kniha {self.nazev} ma {self.pocet_stran} stran a stoji {self.cena}kc."

#   def sleva(self, procento_slevy):
#     self.cena = (1-procento_slevy) * self.cena
#     print(self.cena)

# babicka = Kniha('Babicka', 300, 250)
# print(babicka)
# babicka.sleva(0.2)
# print(babicka)