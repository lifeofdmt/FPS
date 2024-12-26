import pandas as pd


country_file = pd.read_csv('countryInfo.txt', delimiter='\t')


countries = []

countries.append(country_file['Country'])
print(countries)