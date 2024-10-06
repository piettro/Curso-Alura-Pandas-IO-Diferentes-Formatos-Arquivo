import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, inspect

engine = create_engine('sqlite:///:memory:')

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/clientes_banco.csv'
data = pd.read_csv(url)
print(data.head())

data.to_sql('Clients', engine, index=False)

inspector = inspect(engine)
print(inspector.get_table_names())

query = 'SELECT * FROM Clients WHERE Categoria_de_renda = "Empregado"'
employees = pd.read_sql(query, engine)
employees.to_sql('employees', con=engine, index=False)

read_employees = pd.read_sql_table('employees', engine, columns=['ID_Cliente','Grau_escolaridade','Rendimento_anual'])
print(read_employees.head())

query = 'SELECT * FROM Clients'
all_table = pd.read_sql(query, engine)
print(all_table.head())

query = 'DELETE FROM Clients WHERE ID_Cliente = "5008804"'
with engine.connect() as conn:
    conn.execute(query)

query = 'SELECT * FROM Clients'
all_table_without_client_id_5008804 = pd.read_sql_table('Clients', engine)
print(all_table_without_client_id_5008804.head())

query = 'UPDATE Clients SET Grau_escolaridade="Ensino superior" WHERE ID_Cliente=5008808'
with engine.connect() as conn:
    conn.execute(query)
all_table_with_client_5008808_updated = pd.read_sql_table('Clients', engine)
print(all_table_with_client_5008808_updated.head())
