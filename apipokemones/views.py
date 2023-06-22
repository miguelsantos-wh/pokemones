# import asyncio
# import time
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from apipokemones.api import get_pokemons, get_pokemon, get_imagen, get_idtipo, \
    get_pokemonstype


# Create your views here.


def pokemon_list(request):
    contexto = {'pokemones': get_pokemons()}
    id = 0
    contexto2 = {}
    for pokemon in contexto['pokemones']:
        id += 1
        imagen = get_imagen(pokemon['url'])
        contexto2[id] = {
            'id': imagen.get('id'),
            'nombre': pokemon['name'],
            'url': pokemon['url'],
            'imagen': imagen.get('imagen'),
        }
    return render(request, 'pokemones/pokemon_list.html', {'pokemones':contexto2})


def pokemon_detail(request, id_pokemon):
    contexto = get_pokemon(id_pokemon)
    idtipos = {}
    n = 0
    for tipo in contexto['types']:
        n += 1
        type = tipo.get('type')
        url = type.get('url')
        idtipos[n] = {'id': get_idtipo(url)}
    contexto2 = {
        'id': contexto['id'],
        'name': contexto.get('name'),
        'sprites': contexto.get('sprites'),
        'base_experience': contexto.get('base_experience'),
        'weight': contexto.get('weight'),
        'height': contexto.get('height'),
        'abilities': contexto.get('abilities'),
        'moves': contexto.get('moves'),
        'types': contexto.get('types'),
        'idtipos': idtipos,
    }
    return render(request, 'pokemones/pokemon_detail.html', {'object':contexto2})


def pokemon_listtype(request, id_tipo):
    contexto, tipo = get_pokemonstype(id_tipo)
    id = 0
    contexto2 = {}
    for pokemon in contexto:
        id += 1
        poke = pokemon['pokemon']
        imagen = get_imagen(poke['url'])
        contexto2[id] = {
            'id': imagen.get('id'),
            'nombre': poke['name'],
            'url': poke['url'],
            'imagen': imagen.get('imagen'),
        }
    return render(request, 'pokemones/pokemon_list.html', {'pokemones': contexto2, 'tipo': tipo})

