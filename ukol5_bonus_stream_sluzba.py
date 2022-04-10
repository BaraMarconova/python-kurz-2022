class Polozka():
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr

  def get_info(self):
    return (f"Polozka se jmenuje: {self.nazev}, jeji zanr je: {self.zanr}.")

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka

  def get_info(self):
      text = super().get_info()
      text = text + f" Film ma delku {self.delka} minut."
      print(text)
  
  def get_celkova_delka(self):
    celkova_delka = self.delka
    return celkova_delka

class Serial(Polozka):
  def __init__(self, nazev, zanr, pocet_epizod, delka_epizod):
    super().__init__(nazev, zanr)
    self.pocet_epizod = pocet_epizod
    self.delka_epizod = delka_epizod

  def get_info(self):
      text = super().get_info()
      print(text + f" Serial ma {self.pocet_epizod} epizod o delce {self.delka_epizod} minut.")

  def get_celkova_delka(self):
    celkova_delka = self.pocet_epizod * self.delka_epizod
    return celkova_delka


film = Film('Gladiator', 'historicky', 135)
serial = Serial('Pobrezni hlidka', 'akcni', 23, 45)

# film.get_info()
print(serial.get_celkova_delka())

class Uzivatel():
  def __init__ (self, uzivatelske_jmeno):
    self.uzivatelske_jmeno = uzivatelske_jmeno
    self.delka_sledovani = 0

  def pripocti_shlednuti(self, celkova_delka):
    self.delka_sledovani = self.delka_sledovani + self.celkova_delka
    print(self.delka_sledovani)

lenka = Uzivatel('Lenka Hola')
print(lenka.pripocti_shlednuti(film.celkova_delka))