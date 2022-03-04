import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
##to list the names of all the albums released by the artist
artist_uri = 'spotify.com/artist/4zCH9qm4R2DADamUHMCa6O?si=y2a52FlVQnyzpXAApLFTxA' ##pass the artist url
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(artist_uri, album_type='album')
artist_album=json.dumps(results,sort_keys=4,indent=4)
    
    #save it as a json file
with open('Anirudh_albums.json','w') as f:
    f.write(artist_album)
    
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

#cover art for the top 10 tracks
results = spotify.artist_top_tracks(artist_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
