import spotipy
from spotipy.oauth2 import SpotifyOAuth
from data_utils import getAllSongsFromCall, songsToDf, getTracksFromPlaylists, getAllArtistsDf,getRecommendations
import pandas as pd


#Canzoni salvate dall'utente
def getSavedTracks(spotify):
    """
    salva nel file salvate.csv le canzoni salvate (con il cuoricino) dall'utente
    :param spotify: token autenticato Spotify
    """
    saved_tracks = getAllSongsFromCall(spotify, spotify.current_user_saved_tracks())
    df=songsToDf(spotify,saved_tracks)
    df.to_csv("salvate.csv", index=False)

#Canzoni più ascoltate dall'utente
def getTopSong(spotify):
    """
    salva nei file Top_short.csv, Top_medium.csv, Top_long.csv le canzoni più ascoltate dall'utente nel breve, medio e lungo periodo
    :param spotify: token autenticato Spotify
    """
    short_top_tracks = getAllSongsFromCall(spotify, spotify.current_user_top_tracks(time_range='short_term'))
    df=songsToDf(spotify, short_top_tracks)
    df.to_csv("Top_short.csv", index=False)

    medium_top_tracks = getAllSongsFromCall(spotify, spotify.current_user_top_tracks(time_range='medium_term'))
    df=songsToDf(spotify, medium_top_tracks)
    df.to_csv("Top_medium.csv", index=False)

    long_top_tracks = getAllSongsFromCall(spotify, spotify.current_user_top_tracks(time_range='long_term'))
    df=songsToDf(spotify, long_top_tracks)
    df.to_csv("Top_long.csv", index=False)
    
#Prime (max 20) playlist
def getTopPlaylist(spotify):
    """
    salva nel file Tutte_playlist.csv le canzoni contenute nelle prime 20 playlist dell'utente
    :param spotify: token autenticato Spotify
    """
    df=getTracksFromPlaylists(spotify, spotify.current_user_playlists(limit=20))
    df.to_csv("Tutte_playlist.csv", index=False)

#Artisti preferiti
def getTopArtisti(spotify):
    """
    salva nei file Artisti_short.csv, Artisti_medium.csv, Artisti_long.csv gli artisti preferiti dall'utente nel breve, medio e lungo periodo
    :param spotify: token autenticato Spotify
    """
    top_artisti=getAllArtistsDf(spotify, spotify.current_user_top_artists(time_range='short_term'))
    top_artisti.to_csv("Artisti_short.csv", index=False)

    top_artisti=getAllArtistsDf(spotify, spotify.current_user_top_artists(time_range='medium_term'))
    top_artisti.to_csv("Artisti_medium.csv", index=False)

    top_artisti=getAllArtistsDf(spotify, spotify.current_user_top_artists(time_range='long_term'))
    top_artisti.to_csv("Artisti_long.csv", index=False)

def getRacomandedSongs(spotify):
    """
    salva nel file Rec_song.csv le canzoni consigliate a partire dalle canzoni preferite dall'utente nel lungo periodo
    :param spotify: token autenticato Spotify
    """
    dfrec=pd.read_csv("Top_long.csv")
    RecSongs= getRecommendations(spotify,dfrec['id'].tolist())
    RecSongs.to_csv("Rec_songs.csv", index=False)

