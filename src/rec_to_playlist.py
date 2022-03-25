import pandas as pd
import spotipy


def getListaRipetute():
    '''
    La funzione ritorna una lista composta da una concatenazione
    di più dataframe ovvero, canzoni salvate, top_short, medium e long.
    Ovviamente andando a droppare i duplicati che si ripetono all'interno dei dataframe
    :return list(set(lista1 + lista2)): lista di canzoni non ripetute prese dai vari dataframe sopra detti
    '''
    salvatedf=pd.read_csv("salvate.csv")
    lista1=salvatedf['id'].tolist()

    top_shortdf=pd.read_csv("Top_short.csv")
    top_mediumdf=pd.read_csv("Top_medium.csv")
    top_longdf=pd.read_csv("Top_long.csv")
    top_df=pd.concat([top_shortdf,top_mediumdf,top_longdf])
    top_df.drop_duplicates(subset=['id'], inplace=True)
    lista2=top_df['id'].tolist()
    return list(set(lista1 + lista2))

def cleanDuplicates(df, lista):
    '''
    La funzione restituisce un dataframe privo *delle canzoni contenute nella lista passata in input
    :param df: dataframe passato in input
    :param lista: lista di canzoni
    :return df: nuovo dataframe privo di impurita*
    '''
    for idx in df.index:
        if df.at[idx, 'id'] in lista:
            df.drop(idx, inplace=True)
    return df

def getBestSongs():
    '''
    Legge il file dato in output dal modello di ML, esclude le canzoni ripetute 
    e selezione le migliori 30 canzoni che restituisce

    :return migliori: lista contenente gli id delle migliori 30 canzoni
    '''
    recdf=pd.read_csv("OutputR.csv")
    listaEsclusione=getListaRipetute()
    recdf=cleanDuplicates(recdf,listaEsclusione)
    
    migliori=[]
    i=0
    for idx in reversed(recdf.index):
        if(not i<30): break
        else:
            migliori.append(recdf.at[idx,'id'])
        i+=1
    return migliori


    

def addBestToPlaylist(spotify):
    '''
    La funzione svolge l'operazione di aggiunta delle migliori 30 canzoni sopra citate,
    all'interno di una playlist in Spotify
    '''
    top=getBestSongs()
    print(top)
    utente=spotify.me()
    playlist=spotify.user_playlist_create(utente['id'], "SpotySuggestion Playlist", public=True, collaborative=False, description='Nuovi consigli')
    spotify.user_playlist_add_tracks(utente['id'], playlist['id'], top, position=None)


    