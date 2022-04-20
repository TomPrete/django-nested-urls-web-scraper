from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, Actor, Role
# Create your views here.

class MovieListView(ListView):
    model = Movie
    template_name='movies/movie_list.html'
    context_object_name = 'all_movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "List of all Movies"
        return context

class MovieDetailView(DetailView):
    model = Movie
    template_name='movies/movie_detail.html'
    context_object_name='movie'
    pk_url_kwarg='movie_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roles'] = context['object'].roles.all()
        return context

class ActorListView(ListView):
    model = Actor
    template_name='actors/actor_list.html'
    context_object_name = 'all_actors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "List of all Actors"
        context['movie'] = Movie.objects.get(id=self.kwargs['movie_id'])
        return context

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Movie.objects.get(id=movie_id).actors.all()

class ActorDetailView(DetailView):
    model = Actor
    template_name = 'actors/actor_detail.html'
    pk_url_kwarg='actor_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        actor_id = self.kwargs['actor_id']
        return Actor.objects.filter(id=actor_id)
