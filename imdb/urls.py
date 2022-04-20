from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('<int:movie_id>', views.MovieDetailView.as_view(), name='movie_detail'),
    path('<int:movie_id>/actors/', views.ActorListView.as_view(), name='actor_list'),
    path('<int:movie_id>/actors/<int:actor_id>', views.ActorDetailView.as_view(), name='actor_detail'),
]
