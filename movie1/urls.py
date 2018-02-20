from django.conf.urls import url

from . import views
# namespace
app_name = 'movie1'

urlpatterns = [
    # /movie1/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /movie/a.id
    url(r'^(?P<pk>[0-9]+)/$', views.Index1View.as_view(), name='detail'),
    # model form
    url(r'^add/$', views.MovieCreate.as_view(), name='movie-add'),
    # Form Update and delete url
    url(r'^movie1/(?P<pk>[0-9]+)/$', views.MovieUpdate.as_view(), name='movie-update'),
    url(r'^movie1/(?P<pk>[0-9]+)/delete$', views.MovieDelete.as_view(), name='movie-delete'),

    # registration
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    ]

