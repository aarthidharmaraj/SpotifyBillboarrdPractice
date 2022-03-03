from textwrap import indent
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import boto3
# client=boto3.client('s3')

#for creating bucket
# client.create_bucket(Bucket='myspotifyplaylists',
#                      CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})

##After activate the virtual enironment provide the details in terminal
# SET SPOTIPY_CLIENT_ID=***
# SET SPOTIPY_CLIENT_SECRET=***
# SET SPOTIPY_REDIRECT_URI=***
scope = "playlist-modify-public"
username='3172j37o53nutdinxbs3kh7ynyae'

token=SpotifyOAuth(scope=scope,username=username)
spotifyObject=spotipy.Spotify(auth_manager=token)

#crateing playlist
playlist_name=input("Enter the playlist name:")
playlist_description=input("Enter playlist description")
spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_description)
# sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=clientId , client_secret=clientSecret ,redirect_uri=redirect_url,scope=SCOPE, show_dialog=True, cache_path=CACHE)

##Add songs to the created playlists
user_input=input("Enter the song :")
listofsongs=[]

while user_input !='quit':
    result=spotifyObject.search(q=user_input)
    
    # play_song=json.dumps(result,sort_keys=4,indent=4)
    
    # #save it as a json file
    # with open('playlistsong.json','w') as f:
    #     f.write(play_song)
    ##put it in the s3 bucket
    #     response = client.put_object(
    #     Body=open('playlistsong.json','r').read(),#object data with open and read module of the uploading file
    #     Bucket='myspotifyplaylists',
    #     Key='playlistsCreated',#file name to be in s3
    #      )
    # print(response)
    ##grouping the song
    listofsongs.append(result['tracks']['items'][0]['uri'])##available in the json script ##uri is the needed data for adding songs
    user_input=input("Enter the song :")  #to add next song or we can quit.
    
    ##adding the songs to the playlist created

Createdplaylist=spotifyObject.user_playlists(user=username)

##accessing or find the created playlists
playlistaccess=Createdplaylist['items'][0]['id']
# print(playlistaccess)
spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlistaccess,tracks=listofsongs)