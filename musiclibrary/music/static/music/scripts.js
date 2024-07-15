function searchArtists() {
    const query = document.getElementById('searchBox').value;
    fetch(`/search/?q=${query}`)
        .then(response => response.json())
        .then(data => {
            let resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';
            resultsDiv.classList.add('fade-in');

            if (data.artists.length > 0) {
                let artistsList = document.createElement('ul');
                data.artists.forEach(artist => {
                    let listItem = document.createElement('li');
                    listItem.innerHTML = `<a href="/artist/${artist.id}/albums/">${artist.name}</a>`;
                    artistsList.appendChild(listItem);
                });
                resultsDiv.appendChild(artistsList);
            }

            if (data.albums.length > 0) {
                let albumsList = document.createElement('ul');
                data.albums.forEach(album => {
                    let listItem = document.createElement('li');
                    listItem.innerHTML = `<a href="/album/${album.id}/songs/">${album.title}</a>`;
                    albumsList.appendChild(listItem);
                });
                resultsDiv.appendChild(albumsList);
            }

            if (data.songs.length > 0) {
                let songsList = document.createElement('ul');
                data.songs.forEach(song => {
                    let listItem = document.createElement('li');
                    listItem.innerHTML = `${song.title} (Album: ${song.album})`;
                    songsList.appendChild(listItem);
                });
                resultsDiv.appendChild(songsList);
            }
        });
}

function loadSongs(albumId) {
    fetch(`/album/${albumId}/songs/`)
        .then(response => response.text())
        .then(html => {
            let songsDiv = document.getElementById('songs');
            songsDiv.innerHTML = html;
            songsDiv.classList.add('fade-in');
        });
}
