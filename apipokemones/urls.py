from django.conf.urls import url, include
from apipokemones.views import pokemon_list, pokemon_detail, pokemon_listtype

urlpatterns = [
    url(r'^listar/$', pokemon_list, name="pokemon_listarfuncion"),
    url(r'^tipo/(?P<id_tipo>\d+)/$$', pokemon_listtype, name="pokemon_listartipofuncion"),
    url(r'^pokemon/(?P<id_pokemon>\d+)/$', pokemon_detail, name="pokemon_detallefuncion"),
    url(r'^$', pokemon_list, name="index"),
    #url(r'', index, name="index"), #(?P<url>\d+)/
]