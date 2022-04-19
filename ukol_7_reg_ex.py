import re
with open("posta.html", encoding='utf-8') as vstup:
  text = vstup.read()

text = text.replace('/n'," ")
print(text)

reg_vyraz = re.compile("  +")

print(re.sub(reg_vyraz, ' ', text))