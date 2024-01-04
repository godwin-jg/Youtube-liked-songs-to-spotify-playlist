import requests
import urllib.parse
import requests
import json
from refresh import Refresh
class SpotifyClient():
    def __init__(self):
        self.api_token = ""

    def search_song(self, artist, track):
        query = urllib.parse.quote(f'{artist} {track}')
        url = f'https://api.spotify.com/v1/search?q={query}&type=track'
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        response_json = response.json()
        results = response_json['tracks']['items']
        if results:
            return results[0]['id']
        else:
            raise Exception(f"No song found for {artist} = {track}")
        
    def add_song_to_spotify(self, song_id):
        try:
            url = 'https://api.spotify.com/v1/playlists/6OOMrrIYGjcF50UWdjZgU0/tracks'
            request_body = json.dumps({
                "uris":[
                    f"spotify:track:{song_id}"
                ],
                "position":0
            })
            response = requests.post(
                url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_token}"
                },
                data=request_body,
                timeout=15
                
            )
            return response.ok 
        except Exception as e:
            print("Oops! can't add this song bro :)")
            
    def call_refresh(self):
        refreshCall = Refresh()
        self.api_token = refreshCall.refresh()
        print(self.api_token)
        # self.api_token = "BQCGYb20zMnsnNnq9kIQk--w9Y7Vz64w0TPOoc7ZHxFM7AYJSdclJ3Ak8d7T8vyeZTrH7h6wrD0_2cYbbGwUEphq5v8LuX2iUD-B19CkSTXzfdUydD9-RzjCGZ9s5_5Hwnx6VndioCmBoRKX5mzxTLdovHjesNI0BSobZZP-GKIX3HLTpJYfqeivhTWdqrF934YK2VQWkFKBimWqzu1wHm-nuSubqancqPvDuq4uwKCMCERahPAIkyE5hAGTcLwGFWOIFIo"
        
    # def get_token():
    #     client_id = 'a256f557f5724f81842eb24cb5c90bdd'
    #     client_secret = '671b2ad12aa545e8a04f8d30e3206f4d'
    #     redirect_uri = 'http%3A%2F%2Flocalhost%3A3000'

    #     # Step 1: Authorization URL
    #     authorization_url = (
    #         "https://accounts.spotify.com/authorize?"
    #         f"client_id={client_id}&"
    #         "response_type=code&"
    #         f"redirect_uri={redirect_uri}&"
    #         "scope=playlist-modify-private playlist-modify-public"
    #     )

    #     print("Authorization URL:", authorization_url)

    #     # Step 2: Redirect user to the authorization URL

    #     # Step 3: After redirection, obtain the authorization code from the query parameters

    #     # Step 4: Exchange authorization code for access token
    #     authorization_code = ''

    #     token_url = "https://accounts.spotify.com/api/token"
    #     token_data = {
    #         "grant_type": "authorization_code",
    #         "code": authorization_code,
    #         "redirect_uri": redirect_uri,
    #         "client_id": client_id,
    #         "client_secret": client_secret,
    #     }

    #     token_response = requests.post(token_url, data=token_data)
    #     token_json = token_response.json()

    #     # Step 5: Use the access token
    #     access_token = token_json.get("access_token")
    #     print("Access Token:", access_token)
