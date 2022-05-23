import pandas
temperature = pandas.read_csv (r"C:\Users\bmeu1yzr\OneDrive - Avon\Documents\Python\temperature.csv")
print(temperature.head())
print(temperature[temperature['City']=='Prague'])
print(temperature[temperature['AvgTemperature']>80])
print(temperature[(temperature['AvgTemperature']>60) & (temperature['Region']=='Europe')])
print(temperature[(temperature['AvgTemperature']>80) | (temperature['AvgTemperature']<-20)])

# Bonus
# import pytemperature - nefunguje mi istalace

# Bonus 1
print(temperature[temperature['AvgTemperature']>30])
print(temperature[(temperature['AvgTemperature']>15) & (temperature['Region']=='Europe')])
print(temperature[(temperature['AvgTemperature']>30) | (temperature['AvgTemperature']<-10)])

# Bonus 2
temperature_us_13 = (temperature[(temperature['Day']==13) & (temperature['Country']=='US')])
print(temperature_us_13[temperature_us_13['City'].isin(['Washington','Philadelphia'])])