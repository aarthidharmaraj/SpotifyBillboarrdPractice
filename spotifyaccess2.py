import json
import base64
from xml.etree.ElementTree import indent
import requests
authurl = "https://accounts.spotify.com/api/token"
authheaders = {}
authdata = {}
clientId = "1f1c8c80af8c409ba66133b6275b3457" #app client id
clientSecret = "59faebe005a441f09176e8253a2eafaf" #app client secret

## Encodeing client secret and client id
def getAccessToken(clientId,clientSecret):
    
    message = f"{clientId}:{clientSecret}"
    messageBytes = message.encode()#convert to bytes 
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode()#convert back to string
    authheaders['Authorization'] = f"Basic {base64Message}"
    authdata['grant_type'] = "client_credentials"
    r = requests.post(authurl, headers=authheaders, data=authdata)
    responseobject=r.json()
    print(json.dumps(responseobject,indent=2))
    AccessToken=responseobject['access_token']
    # print(AccessToken)
    #return json.dumps(responseobject,indent=2)
    return AccessToken
def getPlayListTracks(token,playlistID):
    base_url = 'https://api.spotify.com/v1/'

    playlistEndpoint="playlists/5HqyPLi4yJ6jh6JGB14BX0?si=e0c09995402441e7"
    playlisturl=base_url+playlistEndpoint   
    getHeader={
      'Authorization': 'Bearer {}'.format(token)
    }
    res = requests.get(playlisturl, headers=getHeader) #get request with no data
    playlistobject=res.json()
    return playlistobject

##Api requests
token=getAccessToken(clientId,clientSecret)
    # print(token)
playlistID ="https://open.spotify.com/playlist/5La7XzPzlzdGgZ4MsZAlzm?si=e740f1d128b84daf"

tracklist=getPlayListTracks(token,playlistID)
print(json.dumps(tracklist,indent=2))

with open('tracklist.json','w') as f:
    json.dump(tracklist,f)
    