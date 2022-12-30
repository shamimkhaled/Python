from newapp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', views.movies_list, name='movie_list')
]
