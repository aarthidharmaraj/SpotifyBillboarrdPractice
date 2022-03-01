import requests

CLIENT_ID = '*****'
CLIENT_SECRET = '*****'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST request with client credentials and save the responses
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
track_id ='0Ul2NGGDAybeXWU0RLnv83?si'

# actual GET request with proper header
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

#convert this response to JSON

# r = r.json()
# print(r)
artist_id = '36QJpDe2go2KgaRleHCDTp'
#artist_id='521uA5nxi1L31JgK6yd2lA?si'##mugin rao album
# artist_id='1eBHjBxiNA3gyEWEN7oRxM?si' ##vijay artist
# pull all artists albums
r1 = requests.get(BASE_URL + 'artists/' + artist_id + '/albums', 
                 headers=headers, 
                 params={'include_groups': 'album', 'limit': 50})
d = r1.json()
# print(d)
# import json
# res=json.dumps(d,indent=2)#takes the dictionary object book and dumps as a string
# print(res)

for album in d['items']:
    print(album['name'], ' --- ', album['release_date'])
    

data = []   # will hold all track info
albums = [] # to keep track of duplicates

# loop over albums and get all tracks
for album in d['items']:
    album_name = album['name']

    # to avoid duplicated albums
    dup_name = album_name.split('(')[0].strip()
    if dup_name.upper() in albums or int(album['release_date'][:4]) > 1983:##filtering the albums after 1983
        continue
    albums.append(dup_name.upper()) # use upper() to standardize
       
    # print(album_name)
    
    # pull all tracks from this album
    r = requests.get(BASE_URL + 'albums/' + album['id'] + '/tracks', 
        headers=headers)
    tracks = r.json()['items']
    
    for track in tracks:
        # get audio features (key, liveness, danceability, ...)
        f = requests.get(BASE_URL + 'audio-features/' + track['id'], 
            headers=headers)
        f = f.json()
        
        # combine with album info
        f.update({
            'track_name': track['name'],
            'album_name': album_name,
            'short_album_name': dup_name,
            'release_date': album['release_date'],
            'album_id': album['id']
        })
        
        data.append(f) ##subsets
        
##collecting them in a dataframe
import pandas as pd

df = pd.DataFrame(data)
##convert that to a dateformat
df['release_date'] = pd.to_datetime(df['release_date'])
df = df.sort_values(by='release_date')

# Zeppelin-specific: get rid of live album, remixes, vocal tracks, ...
df = df.query('short_album_name != "The Song Remains The Same"')
# df = df[~df['track_name'].str.contains('Live|Mix|Track')]

print(df)

import matplotlib.pyplot as plt
df.plot()
plt.show()
