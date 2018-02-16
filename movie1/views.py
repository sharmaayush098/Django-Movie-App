from django.http import Http404
from django.shortcuts import render, get_object_or_404
from movie1.models import Movie, Song


def index(request):
    all_movies = Movie.objects.all()

    context = {
        "all_movies": all_movies,
    }
    return render(request, 'movie1/index.html', context)


def detail(request, movie_id):
    # Http404 shortcut
    m1 = get_object_or_404(Movie, pk=movie_id)
    return render(request, "movie1/index1.html", {'m1': m1})


def favorite(request, movie_id):
    m1 = get_object_or_404(Movie, pk=movie_id)
    try:
        selected_song = m1.song_set.get(pk=request.POST['ong'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'movie1/index1.html', {'m1': m1, 'error_message': 'You Did not selected song'})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'movie1/index1.html', {'m1': m1})
