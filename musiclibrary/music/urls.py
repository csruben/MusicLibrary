from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('artist/<int:artist_id>/albums/', views.album_list, name='album_list'),
    path('album/<int:album_id>/songs/', views.song_list, name='song_list'),
    path('search/', views.search, name='search'),
]
