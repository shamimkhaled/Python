from django.shortcuts import render
from rest_framework import viewsets
from .models import MovieData
from .serializers import MovieSerializers

# Create your views here.
# ViewSets define the view behavior.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializers

# Movies Genre
class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='Action')
    serializer_class = MovieSerializers

class ScifiViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='Sci-fi')
    serializer_class = MovieSerializers

