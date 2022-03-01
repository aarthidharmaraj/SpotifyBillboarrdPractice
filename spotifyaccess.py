import json
import base64
from xml.etree.ElementTree import indent
import requests
authurl = "https://accounts.spotify.com/api/token"
authheaders = {}
authdata = {}
clientId = "*****" #app client id
clientSecret = "****" #app client secret

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
    playlistEndpoint= f"https://api.spotify.com/v1/playlists/{playlistID}"
    getHeader={
       'Authorization' : 'bearer'+ token
    }
    res = requests.get(playlistEndpoint, headers=getHeader) #get request with no data
    playlistobject=res.json()
    return playlistobject

##Api requests
token=getAccessToken(clientId,clientSecret)
    # print(token)
playlistID = "3rhI0UCEDbEhRk4HCzd0Uc?si=1b547ea625324eaf"

tracklist=getPlayListTracks(token,playlistID)
print(json.dumps(tracklist,indent=2))

with open('tracklist.json','w') as f:
    json.dump(tracklist,f)
    