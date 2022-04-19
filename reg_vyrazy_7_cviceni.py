import re

# uzivatelske_jmeno = input("zadej uzivatelske jmeno:")

# reg_vyraz = re.compile("^[a-z]{8}")

# if reg_vyraz.fullmatch(uzivatelske_jmeno):
#   print("uzivatelske jmeno je spravne")
# else:
#   print("uzivatelske jmeno je chybne")

with open("rady.txt", encoding='utf-8') as vstup:
  text = vstup.read()

#print(text)

reg_vyraz = re.compile("https?://(?:w{3}\.)?(?:[a-z]+\.)+(?:com|org|cz)")

print(reg_vyraz.findall(text))