import pandas
zvirata = pandas.read_csv(r"C:\Users\bmeu1yzr\OneDrive - Avon\Documents\Python\adopce-zvirat.csv", sep=";")
zvirata.info()
print(zvirata.shape) # 513 radku a 6 sloupcu
print(zvirata.columns)
print(zvirata.iloc[34,1:3])

# Bonus
zvirata_index = pandas.read_csv(r"C:\Users\bmeu1yzr\OneDrive - Avon\Documents\Python\adopce-zvirat.csv", delimiter=";", index_col=1)
zvirata_index.info()
print(zvirata_index.index.is_unique) #True
zvirata_index = zvirata_index.sort_index()
zvirata_index.info()
print(zvirata_index.loc["Outloň váhavý"])
print(zvirata_index.loc["Želva Smithova":"Želva žlutočelá"])