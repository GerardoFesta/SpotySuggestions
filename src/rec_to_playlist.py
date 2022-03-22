import pandas as pd
import spotipy


def getListaRipetute():
    
    salvatedf=pd.read_csv("salvate.csv")
    lista1=salvatedf['id'].tolist()

    top_shortdf=pd.read_csv("Top_short.csv")
    top_mediumdf=pd.read_csv("Top_medium.csv")
    top_longdf=pd.read_csv("Top_long.csv")
    top_shortdf=top_shortdf['id']
    top_mediumdf=top_mediumdf['id']
    top_longdf=top_longdf['id']
    top_df=pd.concat([top_shortdf,top_mediumdf,top_longdf], ignore_index=True)
    top_df.drop_duplicates('id',keep='first', inplace=True)

    lista2=top_df['id'].tolist()
    return list(set(lista1 + lista2))

def cleanDuplicates(df, lista):
    df.drop(df[df.id not in lista].index, inplace=True)
    return df

def getBestSongs():
    recdf=pd.read_csv("OutputR.csv")
    listaEsclusione=getListaRipetute()
    recdf=cleanDuplicates(recdf,listaEsclusione)
    #scarta topArtista=0
    recdf = recdf[recdf.TopArtista == 1]
    
    recdf.sort_values(['score', 'p_classificazione'], descending=[True, True], inplace=True)
    recdf.reset_index(drop=True, inplace=True)
    migliori=[]
    for idx in recdf.index:
        if(not idx<30): break
        else:
            migliori.append(recdf.at[idx,'id'])
    return migliori


    

def addBestToPlaylist(spotify):
    top=getBestSongs()

    utente=spotify.me()
    playlist=spotify.user_playlist_create(utente['id'], "SpotySuggestion Playlist", public=True, collaborative=False, description='Nuovi consigli')
    spotify.user_playlist_add_tracks(utente['id'], playlist['id'], top, position=None)


    