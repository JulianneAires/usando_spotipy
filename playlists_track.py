import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configurar as credenciais da API 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope='playlist-modify-private user-library-read user-top-read', 
    client_id='##',
    client_secret='##',
    redirect_uri='http://localhost:8888/callback'
))

def get_recommendations(top_tracks_ids):
    recommendations = sp.recommendations(seed_tracks = top_tracks_ids, limit = 5)
    recommended_ids = [track['id'] for track in recommendations['tracks']]
    recommended_ids = [str(track_id) for track_id in recommended_ids]
    return recommended_ids

def get_top_tracks_ids(limit = 5):
    top_tracks = sp.current_user_top_tracks(time_range='medium_term', limit = limit)

    top_tracks_ids = [track['id'] for track in top_tracks['items']]
    return top_tracks_ids

def main():
    top_tracks_ids = get_top_tracks_ids()
    recommended_tracks = get_recommendations(top_tracks_ids)

    playlist = sp.user_playlist_create(
        user = sp.me()['id'], 
        name = input('Digite o nome da sua playlist: '),
        public = False
    )

    sp.playlist_add_items(playlist_id=playlist['id'], items= recommended_tracks)
    print(f"Playlist '{playlist['name']}' criada com sucesso!")
    return playlist

if __name__ == "__main__":
    main()
