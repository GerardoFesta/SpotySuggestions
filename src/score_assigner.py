import pandas as pd
import ast
import numpy as np
from score_utils import creaPunteggioArtisti, popolaritaFasce, creaPunteggioPopolarita, generiPreferiti, creaPunteggioGenere



#BISOGNA PULIRE LE " PRIMA DI []
#"[""canzone d'autore"", 'classic italian pop', 'folk rock italiano', 'italian adult pop']" DIVENTA
#["canzone d'autore", 'classic italian pop', 'folk rock italiano', 'italian adult pop']


def evalScore(moltProvenienza,punteggiPop,punteggiGeneri,punteggiArtista,song):
    score=1
    pop=song['popularity']
    if(pop<=20):
        fascia='1-20'
    if(pop>=21 and pop<=40):
        fascia='21-40'
    else:
        if(pop<=61):
            fascia='41-60'
        else:
            if(pop<=80):
                fascia='61-80'
            else:
                fascia='81-100'
    popScore=punteggiPop.get(fascia)
    if(popScore==None):
        popScore=1
    artScore=punteggiArtista.get(song['artist_name'])
    if(artScore==None):
        artScore=1
    listaGeneri=song['genres']
    genreScore=1
    for genere in listaGeneri:
        if(not punteggiGeneri.get(genere)==None):
            if(genreScore==1):
                genreScore=punteggiGeneri[genere]
            else:
                genreScore+=punteggiGeneri[genere]

    rng = np.random.default_rng()
    rfloat = rng.random()
    score=moltProvenienza*(genreScore+popScore+artScore)*rfloat
    
    return round(score,3)

def dataSongsClean(df):
    df = df[df.genres != '[]']
    df['genres'] = df['genres'].str.replace('"\[','\[')
    df['genres'] = df['genres'].str.replace('\]"','\]')
    df['genres']=df['genres'].str.replace('""','"')
    df['genres']=df['genres'].apply(lambda x:ast.literal_eval(x))
    df = df[df.popularity != 0]
    return df
    
def dataPreparation():
    PLAYLIST_X=1.2
    SALVATE_X=1.4
    PREFERITE_X=1.5


    dfArtisti=pd.read_csv('Artisti_long.csv')
    listaArtisti=dfArtisti['name'].tolist()
    punteggiArtista=creaPunteggioArtisti(listaArtisti)

    preferitedf=pd.read_csv('top_medium.csv')
    preferitedf=dataSongsClean(preferitedf) 

    fascepopolarita=popolaritaFasce(preferitedf['popularity'].tolist())
    punteggiPop=creaPunteggioPopolarita(fascepopolarita)

    generi=generiPreferiti(preferitedf['genres'].tolist())
    punteggiGeneri=creaPunteggioGenere(generi)
    

    playlistdf=pd.read_csv('Tutte_playlist.csv')
    playlistdf=dataSongsClean(playlistdf)
    playlistdf['score']=0
    
    for idx in playlistdf.index:
        score=evalScore(PLAYLIST_X, punteggiPop,punteggiGeneri,punteggiArtista,playlistdf.loc[idx])
        playlistdf.at[idx, 'score']=score
        

    salvatedf=pd.read_csv('salvate.csv')
    salvatedf=dataSongsClean(salvatedf)
    salvatedf['score']=0

    for idx in salvatedf.index:
        score=evalScore(SALVATE_X, punteggiPop,punteggiGeneri,punteggiArtista,salvatedf.loc[idx])
        salvatedf.at[idx, 'score']=score

    
    preferitedf['score']=0

    for idx in preferitedf.index:
        score=evalScore(PREFERITE_X, punteggiPop,punteggiGeneri,punteggiArtista,preferitedf.loc[idx])
        preferitedf.at[idx, 'score']=score
    
    finaldf=pd.concat([playlistdf,preferitedf,salvatedf], ignore_index=True)
    finaldf.sort_values('score', ascending=False).drop_duplicates('id').sort_index()

    finaldf['TopArtista']=0
    for idx in finaldf.index:
        artista=finaldf.loc[idx]['artist_name']
        if(not punteggiArtista.get(artista)==None):
            finaldf.at[idx, 'TopArtista']=1


    finaldf.to_csv("ProvaScore.csv", index=False)

dataPreparation()
    


