import os

import google_auth_oauthlib.flow
from google.oauth2 import service_account
import googleapiclient.discovery
# import youtube_dl
from yt_dlp import YoutubeDL

class Song(object):
    def __init__(self,artist,track):
        self.artist = artist
        self.track = track
class Playlist(object):
    def __init__(self,id,title):
        self.id = id
        self.title = title


class YouTubeClient():
    def __init__(self,credentials_locations):
        
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    credentials_locations, scopes)

        credentials = flow.run_local_server()

        # credentials = service_account.Credentials.from_service_account_file(
        #     credentials_locations, scopes=scopes)
        print(credentials,"Crendentials")
        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)
        self.youtube_client = youtube_client

    
    def get_playlists(self):
        request = self.youtube_client.playlists().list(
            part="id,snippet",
            maxResults=50,
            mine =True
        )
        response = request.execute()
        
        playlists = [Playlist(item['id'],item['snippet']["title"]) for item in response["items"]]
        
        return playlists
    
    def get_videos_from_playlist(self,playlist_id):
        songs = []
        request = self.youtube_client.playlistItems().list(
            playlistId=playlist_id,
            part="id,snippet",
            maxResults=50
        )
        response = request.execute()
        
        for item in response['items']:
            video_id = item["snippet"]["resourceId"]["videoId"]
            artist, track = self.get_artist_and_track_from_video(video_id)
            
            songs.append(Song(artist, track))
            
        # print(response,"Youtube response")
        return songs 
    
    def get_artist_and_track_from_video(self,video_id):
        with YoutubeDL({'outtmpl': '%(id)s.%(ext)s'}) as ydl:
            try:
                info_dict = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
                artist = info_dict.get('artist', None)
                track = info_dict.get('title', None)
                # print(info_dict,"This is info dict")
                return artist,track
            except Exception as e:
                print(f"Error fetching metadata: {e}")
                return None, None
      
    
    
        
    