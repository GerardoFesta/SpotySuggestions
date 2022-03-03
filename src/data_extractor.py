import spotipy
from spotipy.oauth2 import SpotifyOAuth
from data_utils import getAllSongsFromCall, songsToDf, getTracksFromPlaylists

CLIENT_ID="1a37e6452b7649b7b218d75b5be3d377"
CLIENT_SECRET="c0f4dfea62ce47c496fcf1b3cccad4fa"
SCOPE=["user-library-read","user-read-playback-position","user-top-read","user-read-recently-played","user-follow-read","playlist-read-private"]
REDIRECT="http://localhost:8080"


#autenticazione utente con autorizzazione per l'app
spotify=spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT,
    scope=SCOPE
))


#Canzoni salvate dall'utente
saved_tracks = getAllSongsFromCall(spotify, spotify.current_user_saved_tracks())
df=songsToDf(spotify,saved_tracks)
df.to_csv("salvate.csv", index=False)

#Canzoni più ascoltate dall'utente
short_top_tracks = getAllSongsFromCall(spotify, spotify.current_user_top_tracks(time_range='short_term'))
df=songsToDf(spotify, short_top_tracks)
df.to_csv("Top_short.csv.csv", index=False)

medium_top_tracks = getAllSongsFromCall(spotify, spotify.current_user_top_tracks(time_range='medium_term'))
df=songsToDf(spotify, medium_top_tracks)
df.to_csv("Top_medium.csv", index=False)

longdf=long_top_tracks = getAllSongsFromCall(spotify, spotify.current_user_top_tracks(time_range='long_term'))
df=songsToDf(spotify, long_top_tracks)
df.to_csv("Top_long.csv", index=False)

#Prime (max 20) playlist
df=getTracksFromPlaylists(spotify, spotify.current_user_playlists(limit=20))
df.to_csv("Tutte_playlist.csv", index=False)
print("FINE")
