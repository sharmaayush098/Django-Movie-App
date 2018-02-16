from django.views import generic
from django.shortcuts import render, get_object_or_404
from movie1.models import Movie, Song


class IndexView(generic.ListView):
    template_name = 'movie1/index.html'

    def get_queryset(self):
        return Movie.objects.all()


class Index1View(generic.DetailView):
    model = Movie
    template_name = 'movie1/index1.html'



