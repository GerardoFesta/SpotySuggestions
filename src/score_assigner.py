import pandas as pd

#BISOGNA PULIRE LE " PRIMA DI []
#"[""canzone d'autore"", 'classic italian pop', 'folk rock italiano', 'italian adult pop']" DIVENTA
#["canzone d'autore", 'classic italian pop', 'folk rock italiano', 'italian adult pop']

#Nella chiamata passare a tuttigeneri tuttigeneri=dati['genres'].tolist()
def generiPreferiti(tuttigeneri):
    generi={}
    for listaGeneri in tuttigeneri:
        for genere in listaGeneri:
            if(generi.get(genere)==None):
                generi[genere]=1
            else:
                generi[genere]+=1
    print(generi)

#Nella chiamata passare a listapop listapop=dati['popularity'].tolist()
def popolaritaMedia(listapop):
    tot=0
    i=0
    for pop in listapop:
        tot+=pop
        i+=1
    print(round(tot/i))
    return round(tot/i)

#Probabilmente inutile... Ha senso fare una media di valori così? Servirebbe clustering forse
def mediaAudioFeautures(l_danceability,l_energy,l_key,l_loudness,l_speechiness,l_acousticness,l_instrumentalness,l_liveness,l_valence,l_tempo,l_time_signature):
    dict={'m_danceability':0,'m_energy':0 ,'m_key':0,'m_loudness':0,'m_speechiness':0,'m_acousticness':0,'m_instrumentalness':0,'m_liveness':0,'m_valence':0,'m_tempo':0,'m_time_signature':0}
    i=0
    
    while i<len(l_danceability):
        dict['m_danceability']+=l_danceability[i]
        
        
        
        i+=1

    dict['m_danceability']=dict['m_danceability']/len(l_danceability)
    

linea1=['3sSi7rkknbzSNc02yac6Tz','Pezzi di vetro',45,'audio_features','False','False','187733','1','2','16FJYC4FqKhZXiXIzMI4ul','Francesco De Gregori','16FJYC4FqKhZXiXIzMI4ul','Francesco De Gregori','5c1TMPBpOc4qJebACcOm7K','Rimmel','1975-11-27','9','album',["canzone d'autore", 'classic italian pop', 'folk rock italiano', 'italian adult pop'],0.563,0.113,2,-19.92,0.0583,0.935,0.000278,0.106,0.391,138.72,4]
linea2=['0ioTTk5l0Zz7Oh48qEocgj','KEEP IT UP',79,'audio_features','False','False','183000','1','1','7pbDxGE6nQSZVfiFdq9lOL','Rex Orange County','7pbDxGE6nQSZVfiFdq9lOL','Rex Orange County','36IWMZ2DOpKbLb0IrzWc4U','KEEP IT UP','2022-01-26','1','album',['bedroom pop'',' 'pop'],0.708,0.477,8,-7.297,0.0565,0.292,1.75e-06,0.255,0.733,149.929,4]
linea3=['0sTlGEld0h8kIPZaKDYUf4','Notion',91,'audio_features','False','False','195121','1','1','1QfpRUtH14JLoY6F6AYmwt','The Rare Occasions','1QfpRUtH14JLoY6F6AYmwt','The Rare Occasions','4Uf8BVznefnd2xZm2nRFUx','Notion','2021-12-02','1','album',['la indie', "canzone d'autore"],0.309,0.883,9,-3.825,0.0808,0.0673,0.00111,0.0849,0.312,159.488,4]
dati=[linea1, linea2, linea3]
df=pd.DataFrame(dati, columns=['id','name','popularity','type','is_local','explicit','duration_ms','disc_number','track_number','artist_id','artist_name','album_artist_id','album_artist_name','album_id','album_name','album_release_date','album_tracks','album_type','genres','danceability','energy','key','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo','time_signature'])

generiPreferiti(df['genres'].tolist())
popolaritaMedia(df['popularity'].tolist())
mediaAudioFeautures(df['danceability'].tolist(),df['energy'].tolist(),df['key'].tolist(),df['loudness'].tolist(),df['speechiness'].tolist(),df['acousticness'].tolist(),df['instrumentalness'].tolist(),df['liveness'].tolist(),df['valence'].tolist(),df['tempo'].tolist(),df['time_signature'].tolist())