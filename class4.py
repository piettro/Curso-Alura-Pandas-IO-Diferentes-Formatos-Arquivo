import pandas as pd

data_html = pd.read_html('https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies')
top_movies = data_html[1]
print(top_movies.head())

top_movies.to_html('Data/top_movies.html')
top_movies.to_csv('Data/top_movies.csv', index=False)

data_xml = pd.read_xml('https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/imdb_top_1000.xml')
print(data_xml.head())

data_xml.to_xml('Data/movies_imdb.xml')