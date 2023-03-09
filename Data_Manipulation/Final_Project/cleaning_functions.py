import matplotlib.pyplot as plt
import pandas as pd

##returns the last name from the name column
def change_names(happy, covid):
    countries_happiness = list(happy['country'])
    countries_covid = list(covid['Country'])
    for i in range(len(countries_covid)):
        if countries_covid[i] not in countries_happiness:
            print(countries_covid[i])
    names_to_change = []
    for i in range(len(countries_happiness)):
        if countries_happiness[i] not in countries_covid:
            names_to_change.append(countries_happiness[i])
    final_names = ['Czechia', "Cote d'Ivoire", 'Congo', 'Turks and Caicos Islands', 'Palestine', 'Democratic Republic of Congo']
    for i in range(len(names_to_change)):
        happy = happy.replace(names_to_change[i], final_names[i])
    return happy

## returns a plot which shows survival rates by pclass
## expects the titanic dataframe in pandas format
def total_vaccinations(df):
    return(df['People_Fully_Vaccinated'] / df['Population'])
