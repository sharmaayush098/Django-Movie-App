from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View


from movie1.forms import UserForm
from movie1.models import Movie, Song
from django.views.generic import CreateView, UpdateView, DeleteView


class IndexView(generic.ListView):
    template_name = 'movie1/index.html'

    def get_queryset(self):
        return Movie.objects.all()


class Index1View(generic.DetailView):
    model = Movie
    template_name = 'movie1/index1.html'


class MovieCreate(CreateView):
    model = Movie
    fields = ['actor', 'actor_movie', 'genre', 'movie_logo']


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['actor', 'actor_movie', 'genre', 'movie_logo']


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie1:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'movie1/registration_form.html'

    def get(self, request):
        form = self.form_class
        context = {'form': form}
        return render(request, self.template_name, context)
    # process the data

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

        # cleaned (normalized) data
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()

        # return user objects if credentials are correct
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('movie1:index')
        return render(request, self.template_name, {'form': form})





