from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movies_app.models import *
# from movies_app.serializers import *
# Create your views here.
from movies_app.serializaers import MovieSerializer, MovieDetailsSerializer, RatingSerializer


@api_view(['GET'])
def movies_list(request):
  movies_qs=Movie.objects.all()
  if 'name' in request.query_params:
    movies_qs = movies_qs.filter(name__iexact=request.query_params['name'])
  if 'duration_from' in request.query_params:
    movies_qs = movies_qs.filter(duration_in_min__gte=request.query_params['duration_from'])
  if 'duration_to' in request.query_params:
    movies_qs = movies_qs.filter(duration_in_min__lte=request.query_params['duration_to'])
  if 'description' in request.query_params:
    movies_qs = movies_qs.filter(description__icontains=request.query_params['description'])

  if not movies_qs:
    return Response(status=status.HTTP_204_NO_CONTENT)

  serializer = MovieSerializer(movies_qs, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def movie_details(request, movie_id: int):
    try:
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieDetailsSerializer(movie, many=False)
        return Response(serializer.data)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def rating_list(request):
  rating_qs=Rating.objects.all()
  if 'rating' in request.query_params:
    rating_qs = rating_qs.filter(rating__iexact=request.query_params['rating'])

  serializer = RatingSerializer(rating_qs, many=True)
  return Response(serializer.data)

