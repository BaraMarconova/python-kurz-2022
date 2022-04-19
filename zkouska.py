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