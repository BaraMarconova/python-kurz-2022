sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
# print(sales.keys())
# print(sales.values())

#for cyklus
# nazvy = ['Zkus mě chytit', 'Vrah zavolá v deset', 'Zločinný steh']
# for nazev in nazvy:
#   print(nazev)

# jmeno = "lenka"
# for pismeno in jmeno:  #pismeno je nova promena, kazda cast sequence
#   print(pismeno.upper())

# nazvy = ['Zkus mě chytit', 'Vrah zavolá v deset', 'Zločinný steh']
# for nazev in nazvy:
#   if len(nazev) > 15:
#     print(f" ")
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
# for book in sales:
#   if len(book) > 15:
#     print(book)   #primarne vypise klice

# for book in sales:
#   if len(book) > 15:
#     print(f' titulu {book} se prodalo {sales[book]} ks.') 

#.keys() :vsechny klice
# .values(): vsechny hodnoty 
# .items(): dvojice
# print(sales.items())

# for book,count in sales.items(): #dve promene
#   if len(book) > 15:
#     print(f'titilu {book} se prodalo {count} kusu.')

# for item in sales.items():
#   key, value = item
#   print(key)

# books = [ #seznam=list
#   {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
#   {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
#   {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
# ]
# books[0] #slovnik
# print(books[0]["sold"])# vysledek je cislo

# rok = 2019
# pocet_prodanych_knih = 0
# for book in books:
#   if book["year"] == rok:
#     #pocet_prodanych_knih = pocet_prodanych_knih + book["sold"]
#     pocet_prodanych_knih += book["sold"]
# print(f"Za rok {rok} jsem prodali {pocet_prodanych_knih} knih")

books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

books_2019 = list(filter(lambda item: item["year"] == 2019, books))
print(books_2019)