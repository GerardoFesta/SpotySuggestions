import pandas as pd



def getAllSongsFromCall(spotify, chiamata):

    '''
    Restituisce l'intero insieme associato alla chiamata passata in input

    :param spotify: token autenticato Spotify   
    :param chiamata: lista di "items" ricevuta a partire da una chiamata alle API di Spotify 
    :return dati:  lista di items 
    '''

    #Le canzoni sono strutturate all'interno di items
    risultati=chiamata
    dati=risultati["items"]
    while risultati['next']:
        risultati = spotify.next(risultati)
        dati.extend(risultati['items'])
    return dati
    
   
def songsToDf(spotify,songs):
    '''
    La funzione crea un dataset formattato correttamente a partire dall'insieme di canzoni dato in input

     :param spotify: token autenticato Spotify
     :param songs: lista di canzoni
     :return prodotto:  pd.dataframe formattato correttamente
    '''
#prende in input lista di songs non formattate e ritorna un df formattato
    df = pd.DataFrame(songs)
    if 'track' in df.columns.tolist():
        df = df.drop('track', 1).assign(**df['track'].apply(pd.Series))
       
    print(len(df.index))
    #elimina eventuali righe vuote   
    nan_value = float("NaN")
    df['album'].replace("", nan_value, inplace=True)
    df.dropna(subset = ["album"], inplace=True)
    print(len(df.index))

    
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

    '''
    La funzione crea un dataset contenente le canzoni delle playlist,
    formattate correttamente
    :param spotify: token autenticato Spotify
    :param chiamata: lista di "items" ricevuta a partire da una chiamata alle API di Spotify 
    :return songToDf: dataframe formattato correttamente
    '''
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
    '''
    La funzione restituisce un dataframe contenente un insieme di artisti,
    selezionando alcuni campi più importanti (vedesi return)

    :param spotify: token autenticato Spotify   
    :param chiamata: lista di "items" ricevuta a partire da una chiamata alle API di Spotify 
    :return df[["id","uri","type", "name", "genres"]]: dataframe formattato avente colonne "id","uri","type", "name", "genres"
    contenente le informazioni relative agli artisti più ascoltati
    '''
    risultati = chiamata
    #print(risultati)
    #risultati = risultati["artists"]
    dati=risultati["items"]
    while risultati['next']:
        risultati = spotify.next(risultati)
        dati.extend(risultati['items'])
    df = pd.DataFrame(dati)
    return df[["id","uri","type", "name", "genres"]]


 
def getRecommendations(spotify, songs):
    '''
    Restituisce 20 canzoni suggerite per ogni canzone della lista passata in input
    :param spotify: token autenticato Spotify
    :param songs: lista di canzoni
    :return songToDf: dataframe formattato correttamente
    '''
    dati=[]
    for song in songs:
        rec = spotify.recommendations(seed_tracks=[song])
        dati.extend(rec['tracks'])
    return songsToDf(spotify,dati)





#Per dare un peso al genere, un algo pesato sulle occorrenze? Prendiamo top songs, poi arriviamo alla lista di generi
#passando per l'artista. Mettiamo tutte queste liste in una lista più grande, dove assegniamo a ogni genere un peso
#in base alla frequenza con cui è presente
