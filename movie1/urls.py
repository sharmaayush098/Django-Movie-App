from django.conf.urls import url

from . import views
# namespace
app_name = 'movie1'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),
    # /music/a.id
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/a.id/favorite
    url(r'^(?P<movie_id>[0-9]+)/favorite/$', views.favorite, name='favorite')
]