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
        
