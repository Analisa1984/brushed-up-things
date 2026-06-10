from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('artists/', views.artist_directory, name='artist_directory'),
    path('artists/edit/<int:artist_id>/',
         views.edit_artist, name='edit_artist'),
    path('artists/delete/<int:artist_id>/',
         views.delete_artist, name='delete_artist'),
]
