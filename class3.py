import pandas as pd

data = pd.read_json('https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/pacientes.json')
print(data.head())

data_2 = pd.read_json('https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/pacientes_2.json')
print(data_2.head())

data_2_normalize = pd.json_normalize(data_2['Pacientes'])
print(data_2_normalize.head())

data_2_normalize.to_json('Data/history_patients_normalize.json')