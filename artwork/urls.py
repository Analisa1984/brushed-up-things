from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_view, name='about_us'),
    path('gallery/', views.gallery, name='gallery'),
    path('artists/', views.artist_directory, name='artist_directory'),
    path('artists/edit/<int:artist_id>/',
         views.edit_artist, name='edit_artist'),
    path('artists/delete/<int:artist_id>/',
         views.delete_artist, name='delete_artist'),
    path('directory/', views.artwork_directory, name='artwork_directory'),
    path('edit/<int:artwork_id>/', views.edit_artwork, name='edit_artwork'),
    path('delete/<int:artwork_id>/',
         views.delete_artwork, name='delete_artwork'),
    path('contact/', views.contact_view, name='contact'),
]
