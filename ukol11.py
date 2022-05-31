import pandas
zam_praha = pandas.read_csv(r"C:\Users\bmeu1yzr\OneDrive - Avon\Documents\Python\zam_praha.csv", sep=",")
zam_plzen = pandas.read_csv(r"C:\Users\bmeu1yzr\OneDrive - Avon\Documents\Python\zam_plzeň.csv", sep=",")
zam_liberec = pandas.read_csv(r"C:\Users\bmeu1yzr\OneDrive - Avon\Documents\Python\zam_liberec.csv", sep=",")
platy = pandas.read_csv(r"C:\Users\bmeu1yzr\OneDrive - Avon\Documents\Python\platy_2021_02.csv", sep=",")

# print(zam_praha.head())

#novy sloupecek

zam_praha['mesto']="Praha"
zam_plzen['mesto']="Plzen"
zam_liberec['mesto']="Liberec"

#union

zamestnanci = pandas.concat([zam_praha, zam_plzen, zam_liberec], ignore_index=True)
# print(zamestnanci.shape)

# left join
platy_zamestnancu = pandas.merge(zamestnanci,platy, on = ['cislo_zamestnance'], how='left')
# print(platy_zamestnancu.shape)
# print(platy_zamestnancu['plat'].mean())

# BONUS
# uz_nepracuji = platy_zamestnancu[platy_zamestnancu['plat'].isnull()]
# nepracujici_cnt = uz_nepracuji['cislo_zamestnance'].count()
# nepracujici_jmena = (uz_nepracuji[['jmeno','prijimeni']])
# nepracujici_jmena.to_csv('export_nepracujici_jmena',sep=',',index=False)

# PROJEKTY
vykazy = pandas.read_csv(r"C:\Users\bmeu1yzr\OneDrive - Avon\Documents\Python\vykazy.csv", sep=',')
# print(vykazy)
# print(vykazy.groupby('project')['hours'].sum())

vykazy_zamestnancu = pandas.merge(platy_zamestnancu, vykazy,  how='left', left_on = ['cislo_zamestnance'], right_on = ['emloyee_id'])

print(vykazy_zamestnancu)

print(vykazy_zamestnancu.groupby(['mesto','project'])['hours'].sum())