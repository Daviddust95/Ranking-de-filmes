from flask import Flask
import requests

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
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

    # Cria uma string HTML para exibir os resultados
    html = '<h1>Filmes Populares</h1>'
    for movie in results['results']:
        html += f"<p>{movie['title']} - Popularidade: {movie['popularity']}</p>"

    # Retorna a string HTML como resposta
    return html

if __name__ == '__main__':
    app.run()
