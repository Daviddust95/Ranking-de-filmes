import requests

# Sua chave API do The Movie Database
api_key = 'bf3176de7b28b4b0e425df2af84922d4'

# URL base da API
base_url = 'https://api.themoviedb.org/3/'

# Parâmetros de consulta para obter os filmes mais populares
params = {
    'api_key': api_key,
    'language': 'pt-BR',
    'sort_by': 'popularity.desc',
    'page': 1
}

# Faz uma solicitação GET para obter os filmes mais populares
response = requests.get(base_url + 'movie/popular', params=params)

# Extrai os resultados em formato JSON
results = response.json()

# Itera sobre os resultados e exibe o título e a popularidade de cada filme
for movie in results['results']:
    print(movie['title'], movie['popularity'])
