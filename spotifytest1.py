import requests
import json
import base64
client_id = '768397ee06d1480381d47e4f728a4c8d'
client_secret = '5adaecabce97484798f394e64b7c54aa'

##for access token
client_creds = f"{client_id}:{client_secret} "
# print(type(client_creds))

client_creds_b64=base64.b64encode(client_creds.encode())
# print(client_creds_b64)
# print(base64.b64encode(client_creds_b64))
# print(client_creds.encode().decode())
token_url="https://accounts.spotify.com/api/token"
method="POST"
token_data={
    "grant_type":"client_credentials"
}
token_headers = {
    "Authorization":f"Basic {client_creds_b64.decode()}" #<base64 encoded client_id:client_secret>
}
# print(token_header)
r=requests.post(token_url,data=token_data,headers=token_headers)
r1 = r.json()
print(r1)