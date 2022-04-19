class Auto:
  def __init__ (self, registracni_znacka, typ_vozidla, najete_km, volne=True):
    self.registracni_znacka = registracni_znacka
    self.typ_vozidla = typ_vozidla
    self.najete_km = najete_km

  def pujc_auto(self):
    if self.volne:
      self.volne = False
      print("Potvrzuji zapůjčení vozidla")
    else:
      print("Vozidlo není k dispozici")

  def get_info(self):
      return f"Registracni znacka je {self.registracni_znacka}, jedna se o {self.typ_vozidla}."

Peugeot = Auto('4A2 3020','Peugeot 403 Cabrio', '47534')
Skoda = Auto('1P3 4747', 'Škoda Octavia', '41253')

vypujcit = input("Jake auto chcete vypujcit:")
print(vypujcit)