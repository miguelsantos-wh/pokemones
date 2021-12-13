import requests


def get_pokemons():
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=10'
    response = requests.get(url)
    if response.ok:
        payload = response.json()
        results = payload.get('results', [])
    return results


def get_pokemonstype(id_tipo):
    url = 'https://pokeapi.co/api/v2/type/' + str(id_tipo)
    response = requests.get(url)
    if response.ok:
        payload = response.json()
        results = payload.get('pokemon', [])
    return results


def get_pokemon(id):
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(id)
    response = requests.get(url)
    if response.ok:
        payload = response.json()
        results = payload
    return results


def get_imagen(url):
    #url = 'https://pokeapi.co/api/v2/pokemon/' + str(id)
    response = requests.get(url)
    if response.ok:
        response_json = response.json()
        sprite = response_json['sprites']
        id = response_json['id']
        nombre = response_json['name']
        data = {
            'imagen': sprite['front_default'],
            'id': id,
            'nombre': nombre,
        }
        return data


def get_idtipo(url):
    response = requests.get(url)
    if response.ok:
        response_json = response.json()
        id = response_json['id']
        name = response_json['name']
        data = {
            'id': id,
            'name': name,
        }
        return data
