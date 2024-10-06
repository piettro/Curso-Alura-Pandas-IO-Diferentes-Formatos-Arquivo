import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data.csv'
data = pd.read_csv(url)
data_nrows = pd.read_csv(url,nrows=5)
data_usecols = pd.read_csv(url, usecols=['Id', 'Year_Birth', 'Income'])

print(data.head())
print(data_nrows.head())
print(data_usecols.head())

data_nrows.to_csv('Data/clients_market_nrows.csv', index=False)
data_usecols.to_csv('Data/clients_market_usecols.csv', index=False)