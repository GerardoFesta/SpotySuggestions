import pandas as pd


def getAllSongsFromCall(spotify, chiamata):

    #Le canzoni sono strutturate all'interno di items
    risultati=chiamata
    dati=risultati["items"]
    while risultati['next']:
        risultati = spotify.next(risultati)
        dati.extend(risultati['items'])
    return dati
    
#prende in input lista di songs non formattate e ritorna un df formattato
def songsToDf(spotify,songs):
    
    df = pd.DataFrame(songs)
    if 'track' in df.columns.tolist():
        df = df.drop('track', 1).assign(**df['track'].apply(pd.Series))
       
    
    
    df['album_id'] = df['album'].apply(lambda x: x['id'])
    df['album_name'] = df['album'].apply(lambda x: x['name'])
    df['album_release_date'] = df['album'].apply(lambda x: x['release_date'])
    df['album_tracks'] = df['album'].apply(lambda x: x['total_tracks'])
    df['album_type'] = df['album'].apply(lambda x: x['type'])
    df['album_artist_id'] = df['album'].apply(lambda x: x['artists'][0]['id'])
    df['album_artist_name'] = df['album'].apply(lambda x: x['artists'][0]['name'])
    
    #Dati artista
    df['artist_id'] = df['artists'].apply(lambda x: x[0]['id'])
    df['artist_name'] = df['artists'].apply(lambda x: x[0]['name'])
    #Aggiunta parte che prende l''id_artista e lo usa per ricavare i generi e lo aggiunge qua 
    df['genres'] = df['artist_id'].apply(lambda x: spotify.artist(x)['genres'])
    #Feature audio
    df['audio_features'] = df['id'].apply(lambda x: spotify.audio_features(x))
    df['audio_features'] = df['audio_features'].apply(pd.Series)
    df = df.drop('audio_features', 1).assign(**df['audio_features'].apply(pd.Series))

    select_columns = ['id', 'name', 'popularity', 'type', 'is_local', 'explicit', 'duration_ms', 'disc_number',
                      'track_number',
                      'artist_id', 'artist_name', 'album_artist_id', 'album_artist_name',
                      'album_id', 'album_name', 'album_release_date', 'album_tracks', 'album_type',
                      'genres', 'danceability', 'energy', 'key', 'loudness','speechiness', 'acousticness',
                      'instrumentalness','liveness','valence','tempo','time_signature'
                        ]
    prodotto=df[select_columns]
    return prodotto

def getTracksFromPlaylists(spotify, chiamata):

    playlists = chiamata
    tutte_playlist = playlists['items']
    dati=[]
   
    for playlist in tutte_playlist:
        saved_tracks = spotify.playlist(playlist['id'], fields="tracks, next")
        results = saved_tracks['tracks']
        dati.extend(results['items'])
        while results['next']:
            results = spotify.next(results)
            dati.extend(results['items'])
    
    return songsToDf(spotify,dati)


def getAllArtistsDf(spotify, chiamata):
    
    risultati = chiamata
    #print(risultati)
    #risultati = risultati["artists"]
    dati=risultati["items"]
    while risultati['next']:
        risultati = spotify.next(risultati)
        dati.extend(risultati['items'])
    df = pd.DataFrame(dati)
    return df[["id","uri","type", "name", "genres"]]




#Per dare un peso al genere, un algo pesato sulle occorrenze? Prendiamo top songs, poi arriviamo alla lista di generi
#passando per l'artista. Mettiamo tutte queste liste in una lista più grande, dove assegniamo a ogni genere un peso
#in base alla frequenza con cui è presente
