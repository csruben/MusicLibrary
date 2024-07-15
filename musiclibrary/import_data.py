import json
import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "musiclibrary.settings")
django.setup()

from music.models import Artist, Album, Song

def import_data(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for artist_data in data:
            artist = Artist.objects.create(name=artist_data['name'])
            for album_data in artist_data['albums']:
                album = Album.objects.create(
                    artist=artist,
                    title=album_data['title'],
                    description=album_data.get('description', '').strip()  # handle cases where description might be missing
                )
                for song_data in album_data['songs']:
                    Song.objects.create(
                        album=album,
                        title=song_data['title'],
                        length=song_data['length']
                    )

# Call the function with the path to your JSON file
import_data("../musiclibrary/data/data.json")
