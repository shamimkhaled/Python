from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.
def movies_list(request):
    movie_objects = Movies.objects.all()
    # search functionality and implementing by name=movie_name in html input form
    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movie_objects = movie_objects.filter(name__icontains=movie_name)
    # Page paginator
    paginator = Paginator(movie_objects, 4)
    page = request.GET.get('page')
    movie_objects = paginator.get_page(page)
    return render(request, 'newapp/movie_list.html', {'movie_objects':movie_objects})
