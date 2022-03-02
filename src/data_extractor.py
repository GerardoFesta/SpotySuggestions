import spotipy
from spotipy.oauth2 import SpotifyOAuth
from data_utils import getAllSongsFromCall, songsToDf

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

saved_tracks = getAllSongsFromCall(spotify, spotify.current_user_saved_tracks())
songsToDf(saved_tracks)
#commento gianluca 
#commento emanueleee
#commento carmine