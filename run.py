import os
from yt_client import YouTubeClient
from spfy_client import SpotifyClient

def run():
    youtube_client = YouTubeClient('./creds/client_secret.json')
    spotify_client = SpotifyClient()
    spotify_client.call_refresh()
    # spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))

    while True:
        playlists = youtube_client.get_playlists()

        for idx, playlist in enumerate(playlists):
            print(f"{idx}: {playlist.title}")

        print("Enter 'exit' to exit.")
        choice = input("Enter your choice: ")

        if choice == 'exit':
            print("See ye. Bye!")
            break

        try:
            choice = int(choice)
            chosen_playlist = playlists[choice]
            print(f"You selected: {chosen_playlist.title}")

            songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
            print(f"Adding {len(songs)} songs to your Spotify playlist")

            for song in songs:
                print("ARtist and tract :")
                print(song.artist)
                print(song.track)
                spotify_song_id = spotify_client.search_song(song.artist, song.track)
                print("song id: ", spotify_song_id)

                if spotify_song_id is not None:
                    added_song = spotify_client.add_song_to_spotify(spotify_song_id)
                    if added_song:
                        print(f"Added {song.artist} - {song.track} to your Spotify playlist")
                    else:
                        print(f"{song.artist} - {song.track} not added to your Spotify playlist")
                else:
                    print("No song id found")
        except Exception as e:
            print("Invalid input. Please enter a valid number.")

 
if __name__ == '__main__':
    run()