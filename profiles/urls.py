from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('delete/', views.delete_profile, name='delete_profile'),
    path('management/', views.staff_dashboard, name='staff_dashboard'),
    path('management/add-artist/', views.add_artist, name='add_artist'),
    path('management/add-artwork/', views.add_artwork, name='add_artwork')
]
