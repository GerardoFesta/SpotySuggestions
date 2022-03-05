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

def popolatiyaFasce(listapop):
    dict={'1-20':0,'21-40':0,'41-60':0,'61-80':0,'81-100':0}
    for pop in listapop:
        if(pop>=1 and pop<=20):
            dict['1-20']+=1
        else:
            if(pop>=21 and pop<=40):
                dict['21-40']+=1
            else:
                if(pop>=41 and pop<=60):
                    dict['41-60']+=1
                else:
                    if(pop>=61 and pop<=80):
                        dict['61-80']+=1
                    else:
                        if(pop>=81 and pop<=100):
                            dict['81-100']+=1



def contaEsplicite(listaexplicit):
    return listaexplicit.count(True),listaexplicit.count(False)
    

#Applica lambda per prendere solo anno prima di richiamare
#df['album_release_date']=df['album_release_date'].apply(lambda x : x[0:4])
def raccoltaAnni(listaAnni):
    anni={}
    for anno in listaAnni:
        if(anni.get(anno)==None):
            anni[anno]=1
        else:
            anni[anno]+=1
    print(anni)



#Probabilmente inutile... Ha senso fare una media di valori così? Servirebbe clustering forse
def mediaAudioFeautures(l_danceability,l_energy,l_key,l_loudness,l_speechiness,l_acousticness,l_instrumentalness,l_liveness,l_valence,l_tempo,l_time_signature):
    dict={'m_danceability':0,'m_energy':0 ,'m_key':0,'m_loudness':0,'m_speechiness':0,'m_acousticness':0,'m_instrumentalness':0,'m_liveness':0,'m_valence':0,'m_tempo':0,'m_time_signature':0}
    i=0
    
    while i<len(l_danceability):
        dict['m_danceability']+=l_danceability[i]
        dict['m_energy']+=l_energy[i]
        dict['m_key']+=l_key[i]
        dict['m_loudness']+=l_loudness[i]
        dict['m_speechiness']+=l_speechiness[i]
        dict['m_acousticness']+=l_acousticness[i]
        dict['m_instrumentalness']+=l_instrumentalness[i]
        dict['m_liveness']+=l_liveness[i]
        dict['m_valence']+=l_valence[i]
        dict['m_tempo']+=l_tempo[i]
        dict['m_time_signature']+=l_time_signature[i]
        
        
        i+=1

    dict['m_danceability']=dict['m_danceability']/len(l_danceability)
    dict['m_energy']=dict['m_energy']/len(l_energy)
    dict['m_key']=dict['m_key']/len(l_key)
    dict['m_loudness']=dict['m_loudness']/len(l_loudness)
    dict['m_speechiness']=dict['m_speechiness']/len(l_speechiness)
    dict['m_acousticness']=dict['m_acousticness']/len(l_acousticness)
    dict['m_instrumentalness']=dict['m_instrumentalness']/len(l_instrumentalness)
    dict['m_liveness']=dict['m_liveness']/len(l_liveness)
    dict['m_valence']=dict['m_valence']/len(l_valence)
    dict['m_tempo']=dict['m_tempo']/len(l_tempo)
    dict['m_time_signature']=dict['m_time_signature']/len(l_time_signature)
    print(dict)
    return dict
    

linea1=['3sSi7rkknbzSNc02yac6Tz','Pezzi di vetro',45,'audio_features',False,False,'187733','1','2','16FJYC4FqKhZXiXIzMI4ul','Francesco De Gregori','16FJYC4FqKhZXiXIzMI4ul','Francesco De Gregori','5c1TMPBpOc4qJebACcOm7K','Rimmel','1975-11-27','9','album',["canzone d'autore", 'classic italian pop', 'folk rock italiano', 'italian adult pop'],0.563,0.113,2,-19.92,0.0583,0.935,0.000278,0.106,0.391,138.72,4]
linea2=['0ioTTk5l0Zz7Oh48qEocgj','KEEP IT UP',79,'audio_features',False,False,'183000','1','1','7pbDxGE6nQSZVfiFdq9lOL','Rex Orange County','7pbDxGE6nQSZVfiFdq9lOL','Rex Orange County','36IWMZ2DOpKbLb0IrzWc4U','KEEP IT UP','2022-01-26','1','album',['bedroom pop'',' 'pop'],0.708,0.477,8,-7.297,0.0565,0.292,1.75e-06,0.255,0.733,149.929,4]
linea3=['0sTlGEld0h8kIPZaKDYUf4','Notion',91,'audio_features',False,False,'195121','1','1','1QfpRUtH14JLoY6F6AYmwt','The Rare Occasions','1QfpRUtH14JLoY6F6AYmwt','The Rare Occasions','4Uf8BVznefnd2xZm2nRFUx','Notion','2021-12-02','1','album',['la indie', "canzone d'autore"],0.309,0.883,9,-3.825,0.0808,0.0673,0.00111,0.0849,0.312,159.488,4]
dati=[linea1, linea2, linea3]
df=pd.DataFrame(dati, columns=['id','name','popularity','type','is_local','explicit','duration_ms','disc_number','track_number','artist_id','artist_name','album_artist_id','album_artist_name','album_id','album_name','album_release_date','album_tracks','album_type','genres','danceability','energy','key','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo','time_signature'])

generiPreferiti(df['genres'].tolist())
popolaritaMedia(df['popularity'].tolist())
mediaAudioFeautures(df['danceability'].tolist(),df['energy'].tolist(),df['key'].tolist(),df['loudness'].tolist(),df['speechiness'].tolist(),df['acousticness'].tolist(),df['instrumentalness'].tolist(),df['liveness'].tolist(),df['valence'].tolist(),df['tempo'].tolist(),df['time_signature'].tolist())
contaTrue,contaFalse=contaEsplicite(df['explicit'].tolist())
print(contaTrue, contaFalse)
df['album_release_date']=df['album_release_date'].apply(lambda x : x[0:4])
raccoltaAnni(df['album_release_date'].tolist())





linea11=['3hBQ4zniNdQf1cqqo6hzuW','spotify:artist:3hBQ4zniNdQf1cqqo6hzuW','artist','Salmo',['italian hip hop', 'italian underground hip hop', 'rap sardegna']]
linea22=['23TFHmajVfBtlRx5MXqgoz','spotify:artist:23TFHmajVfBtlRx5MXqgoz','artist','Sfera Ebbasta',['italian hip hop', 'italian pop', 'trap italiana']]
linea33=['5AZuEF0feCXMkUCwQiQlW7','spotify:artist:5AZuEF0feCXMkUCwQiQlW7','artist','Marracash',['italian hip hop', 'italian underground hip hop', 'rap napoletano']]
dati=[linea11, linea22, linea33]

df=pd.DataFrame(dati, columns=['id','uri','type','name','genres'])
generiPreferiti(df['genres'].tolist())

