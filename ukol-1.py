# baliky = {
#     "B541X": True,
#     "B547X": False,
#     "B251X": False,
#     "B501X": True,
#     "B947X": False,
# }
# kod_baliku = input("Napis kod tveho baliku:")
# if kod_baliku in baliky:
#   if baliky[kod_baliku] == True:
#     print("Balík byl předán kurýrovi.")
#   else:
#     print("Balík zatím nebyl předán kurýrovi.")
# else:
#   print("Cislo baliku neni v databazi.")

baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
kod_baliku = input("Napis kod tveho baliku:")
if kod_baliku in baliky:
  if baliky[kod_baliku]:
    print("Balík byl předán kurýrovi.")
  else:
    print("Balík zatím nebyl předán kurýrovi.")
else:
  print("Cislo baliku neni v databazi.")
