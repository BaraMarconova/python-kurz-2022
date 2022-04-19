# school_report = {
#   "Český jazyk": 1,
#   "Anglický jazyk": 1,
#   "Matematika": 1,
#   "Přírodopis": 2,
#   "Dějepis": 1,
#   "Fyzika": 2,
#   "Hudební výchova": 4,
#   "Výtvarná výchova": 2,
#   "Tělesná výchova": 3,
#   "Chemie": 4,
# }

# pocet_znamek = (len(school_report.values()))
# sum_znamek = 0
# for znamka in school_report.values():
#   sum_znamek = sum_znamek + znamka
# average = sum_znamek/pocet_znamek
# print(average)

# for predmet,znamka in school_report.items():
#   if znamka == 1:
#     print(predmet)
  

#uloha 2
from itertools import count


books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]
pocet_prectenych_stran = 0
dobre_knihy = []
for book in books:
  pocet_prectenych_stran += book["pages"]
  dobre_knihy.append(book["title"]) #seznamdobrych knih
print(pocet_prectenych_stran)

print(",".join(dobre_knihy))

# pocet_dobrych_knih = 0
# for book in books:
#   if book["rating"] > 7:
#     pocet_dobrych_knih += 1
# print(pocet_dobrych_knih)


 
# bonusove cviceni
# plates = {"4A2 3000": "František Novák",
#   "6P5 4747": "Jana Pilná",
#   "3B7 3652": "Jaroslav Sečkár",
#   "1P5 5269": "Marta Nováková",
#   "37E 1252": "Martina Matušková",
#   "2A5 2241": "Jan Král"}

# for znacka, jmeno in plates.items():
#   if znacka[1] == "P":
#     print(jmeno) 