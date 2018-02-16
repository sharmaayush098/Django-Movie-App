from django.conf.urls import url

from . import views
# namespace
app_name = 'movie1'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /music/a.id
    url(r'^(?P<pk>[0-9]+)/$', views.Index1View.as_view(), name='detail'),


]