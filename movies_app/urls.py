from django.urls import path

from . import views

urlpatterns = [
    path('api/movies', views.movies_list),
    path('api/movies/<int:movie_id>', views.movie_details),
    path('api/rating', views.rating_list),
]