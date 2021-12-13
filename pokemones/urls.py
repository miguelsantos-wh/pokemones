from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'pokemones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pokemones/', include('apipokemones.urls', namespace="pokemones")),
    url(r'^$', include('apipokemones.urls', namespace="index")),
]
