from pickle import FALSE
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
def songsToDf(songs):
    
    
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
    #Aggiungere parte che prende l'artist_id e lo usa per ricavare i generi e lo aggiunge qua
    df['artist_id'] = df['artists'].apply(lambda x: x[0]['id'])
    df['artist_name'] = df['artists'].apply(lambda x: x[0]['name'])
    select_columns = ['id', 'name', 'popularity', 'type', 'is_local', 'explicit', 'duration_ms', 'disc_number',
                      'track_number',
                      'artist_id', 'artist_name', 'album_artist_id', 'album_artist_name',
                      'album_id', 'album_name', 'album_release_date', 'album_tracks', 'album_type']
    prodotto=df[select_columns]
    prodotto.to_csv("primiDati.csv", index=FALSE)


#Per dare un peso al genere, un algo pesato sulle occorrenze? Prendiamo top songs, poi arriviamo alla lista di generi
#passando per l'artista. Mettiamo tutte queste liste in una lista più grande, dove assegniamo a ogni genere un peso
#in base alla frequenza con cui è presente

