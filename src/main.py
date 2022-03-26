from data_extractor import getSavedTracks, getTopSong, getTopPlaylist, getTopArtisti, getRacomandedSongs
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from r_scripts_loader import runScripts
from rec_to_playlist import addBestToPlaylist
import os
from dotenv import load_dotenv
from score_assigner import dataPreparation
from post_score_editor import getReadyCsv
from recom_preparation import getReadyRec


#Autenticazione dell'utente
def autentication():
    load_dotenv()
    CLIENT_ID=os.getenv("CLIENT_ID")
    CLIENT_SECRET=os.getenv("CLIENT_SECRET")
    SCOPE=["user-library-read","user-read-playback-position","ugc-image-upload","user-top-read","user-read-recently-played","user-follow-read","playlist-read-private","playlist-modify-private","playlist-read-collaborative","playlist-read-private","playlist-modify-public"]
    REDIRECT="http://localhost:8080"

    spotify=spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT,
        scope=SCOPE
    ))
    return spotify

def main():
    spotify=autentication()
    
    #Richiamo metodi di estrazione dei dati
    
    print("Prendo canzoni salvate. . .")
    getSavedTracks(spotify)
    print("Prendo canzoni Top. . .")
    getTopSong(spotify)
    print("Prendo canzoni playlist. . .")
    getTopPlaylist(spotify)
    print("Prendo i migliori artisti. . .")
    getTopArtisti(spotify)
    print("Genero consigli canzoni. . .")
    getRacomandedSongs(spotify)
    print("Fine estrazione dati.")
    
    print("Preparazione dati per Machine Learning. . .")
    dataPreparation()
    getReadyCsv()
    getReadyRec()
    
    print("Esecuzione script R. . .")
    runScripts()
    
    print("Preparazione playlist finale. . .")
    addBestToPlaylist(spotify)
    print("Finito! Troverai la tua playlist come SpotySuggestions!")


main()