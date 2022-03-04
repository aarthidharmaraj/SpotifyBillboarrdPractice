import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id='*****', client_secret='****')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_link = "https://open.spotify.com/playlist/5La7XzPzlzdGgZ4MsZAlzm?si=e740f1d128b84daf"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

for track in sp.playlist_tracks(playlist_URI)["items"]:
    #URI
    track_uri = track["track"]["uri"]
    print("The URI ID Is : ",track_uri)
    #Track name
    track_name = track["track"]["name"]
    print("The Track name is : ",track_name)
    #Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    print("The artist information is : ",artist_info)
    #Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    print("The artist name is : ",artist_name)
    artist_pop = artist_info["popularity"]
    print("The artist popularity is : ",artist_pop)
    artist_genres = artist_info["genres"]
    print("The artist genre is : ",artist_genres)
    #Album
    album = track["track"]["album"]["name"]
    print("The artist  album name is : ",album)
    #Popularity of the track
    track_pop = track["track"]["popularity"]
    print("The Popularity of track is : ",track_pop)
    print("The audio features",sp.audio_features(track_uri)[0])