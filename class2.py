import pandas as pd

url = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'
data = pd.read_excel(url)
data_percapita = pd.read_excel(url, sheet_name='emissoes_percapita')
sources = pd.read_excel(url, sheet_name='fontes')
data_usecols = pd.read_excel(url, sheet_name='emissoes_C02', usecols= 'A:D')

print(pd.ExcelFile(url).sheet_names)
print(data.head())
print(data_percapita.head())
print(sources.head())

data_percapita.to_excel('Data/CO2_percapita.xlsx',index=False)

sheet_id = '1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog'
sheet_name = 'emissoes_percapita'
google_sheets_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
data_co2_sheets = pd.read_csv(url)
print(data_co2_sheets.head())
