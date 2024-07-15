from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Artist, Album, Song

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artist_list.html', {'artists': artists})

def album_list(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'album_list.html', {'artist': artist})

def song_list(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'song_list.html', {'album': album})

def search(request):
    query = request.GET.get('q', '')
    if query:
        artists = Artist.objects.filter(name__icontains=query)
        albums = Album.objects.filter(title__icontains=query)
        songs = Song.objects.filter(title__icontains=query)

        artist_results = [{'id': artist.id, 'name': artist.name} for artist in artists]
        album_results = [{'id': album.id, 'title': album.title} for album in albums]
        song_results = [{'id': song.id, 'title': song.title, 'album': song.album.title} for song in songs]

        results = {
            'artists': artist_results,
            'albums': album_results,
            'songs': song_results
        }
        return JsonResponse(results)
    return JsonResponse({'artists': [], 'albums': [], 'songs': []})

