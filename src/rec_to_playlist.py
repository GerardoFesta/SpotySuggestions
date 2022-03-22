import pandas as pd
import spotipy


def getListaRipetute():
    
    salvatedf=pd.read_csv("salvate.csv")
    lista1=salvatedf['id'].tolist()

    top_shortdf=pd.read_csv("Top_short.csv")
    top_mediumdf=pd.read_csv("Top_medium.csv")
    top_longdf=pd.read_csv("Top_long.csv")
    top_df=pd.concat([top_shortdf,top_mediumdf,top_longdf])
    top_df.drop_duplicates(subset=['id'], inplace=True)
    print(top_df)
    lista2=top_df['id'].tolist()
    return list(set(lista1 + lista2))

def cleanDuplicates(df, lista):
    for idx in df.index:
        if df.at[idx, 'id'] in lista:
            df.drop(idx, inplace=True)
    return df

def getBestSongs():
    recdf=pd.read_csv("OutputR.csv")
    listaEsclusione=getListaRipetute()
    recdf=cleanDuplicates(recdf,listaEsclusione)
    #scarta topArtista=0
    recdf = recdf[recdf.TopArtista == 1]
    
    recdf.sort_values(['score', 'p_classificazione'], ascending=[True, True], inplace=True)
    migliori=[]
    i=0
    for idx in reversed(recdf.index):
        if(not i<30): break
        else:
            migliori.append(recdf.at[idx,'id'])
        i+=1
    return migliori


    

def addBestToPlaylist(spotify):
    top=getBestSongs()

    utente=spotify.me()
    playlist=spotify.user_playlist_create(utente['id'], "SpotySuggestion Playlist", public=True, collaborative=False, description='Nuovi consigli')
    spotify.user_playlist_add_tracks(utente['id'], playlist['id'], top, position=None)


    