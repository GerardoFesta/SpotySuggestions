from score_assigner import dataPreparation
from score_utils import getSingleGenre, dataSongsClean, assignSingleGenre, one_to_all_fav_artists
import pandas as pd




#dataPreparation()
def getReadyCsv():
    fulldf=pd.read_csv("ProvaScore.csv")
    fulldf=dataSongsClean(fulldf)
    art_short_df=pd.read_csv("Artisti_short.csv")
    art_medium_df=pd.read_csv("Artisti_medium.csv")
    art_long_df=pd.read_csv("Artisti_long.csv")
    art_df=pd.concat([art_short_df,art_medium_df,art_long_df], ignore_index=True)
    art_df.drop_duplicates('id',keep='first', inplace=True)
    colonne=["id","name"]
    art_df=art_df[colonne]

    dict_artisti={}


    top_shortdf=pd.read_csv("Top_short.csv")
    top_mediumdf=pd.read_csv("Top_medium.csv")
    top_longdf=pd.read_csv("Top_long.csv")
    colonne=["artist_id","artist_name"]
    top_shortdf=top_shortdf[colonne]
    top_mediumdf=top_mediumdf[colonne]
    top_longdf=top_longdf[colonne]

    top_df=pd.concat([top_shortdf,top_mediumdf,top_longdf], ignore_index=True)
    top_df.drop_duplicates('artist_id',keep='first', inplace=True)
    print(top_df)
    top_df = top_df.rename(columns={'artist_id': 'id', 'artist_name': 'name'})

    tuttiartisti_df=pd.concat([top_df,art_df], ignore_index=True)

    tuttiartisti_df.drop_duplicates(subset=['id'],keep='first', inplace=True)

    for artista in tuttiartisti_df['name'].tolist() :
        dict_artisti[artista]=1


    fulldf=assignSingleGenre(fulldf)
    fulldf=one_to_all_fav_artists(fulldf,dict_artisti)
    fulldf.to_csv("READY_ARTISTI_GENERI.csv", index=False)
#tuttiartisti_df.to_csv("LISTA_COMPLETA_ARTISTI.csv", index=False)
#one_to_all_fav_artists(fulldf)