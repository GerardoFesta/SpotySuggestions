from score_assigner import dataPreparation, getSingleGenre
import pandas as pd

def assignSingleGenre(fulldf):
    fulldf["genere"]=""
    for idx in fulldf.index:
        genere=getSingleGenre(fulldf.loc[idx])
        fulldf.at[idx,"genere"]=genere
    
    return fulldf

def one_to_all_fav_artists(fulldf,dict_artisti):
    for idx in fulldf.index:
        artista=fulldf.loc[idx]['artist_name']
        if(not dict_artisti.get(artista)==None):
            fulldf.at[idx, 'TopArtista']=1
    return fulldf


#dataPreparation()
fulldf=pd.read_csv("ProvaScore.csv")
art_short_df=pd.read_csv("Artisti_short.csv")
art_medium_df=pd.read_csv("Artisti_medium.csv")
art_long_df=pd.read_csv("Artisti_long.csv")
art_df=pd.concat([art_short_df,art_medium_df,art_long_df], ignore_index=True)
art_df.drop_duplicates('id',keep='first', inplace=True)
colonne=["id","name"]
art_df=art_df[colonne]

dict_artisti={}


top_shortdf=pd.read_csv("Top_short.csv")
top_mediumdf=pd.read_csv("Top_short.csv")
top_longdf=pd.read_csv("Top_short.csv")
colonne=["artist_id","artist_name"]
top_shortdf=top_shortdf[colonne]
top_mediumdf=top_mediumdf[colonne]
top_longdf=top_longdf[colonne]

top_df=pd.concat([top_shortdf,top_mediumdf,top_longdf], ignore_index=True)
top_df.drop_duplicates('artist_id',keep='first', inplace=True)
print(top_df)
top_df = top_df.rename(columns={'artist_id': 'id', 'artist_name': 'name'})

tuttiartisti_df=pd.concat([top_df,art_df], ignore_index=True)

tuttiartisti_df.drop_duplicates('id',keep='first', inplace=True)

for artista in tuttiartisti_df['name'].tolist() :
    dict_artisti[artista]=1


fulldf=assignSingleGenre(fulldf)
fulldf=one_to_all_fav_artists(fulldf)
fulldf.to_csv("READY_ARTISTI_GENERI.csv", index=False)
#tuttiartisti_df.to_csv("LISTA_COMPLETA_ARTISTI.csv", index=False)
#one_to_all_fav_artists(fulldf)