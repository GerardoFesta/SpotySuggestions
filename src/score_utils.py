import pandas as pd
import ast
import numpy as np

SC_GENRE1=1.8
SC_GENRE2=1.6
SC_GENRE3=1.3
SC_GENRE4=1.1
SC_POPULARITY1=1.4
SC_POPULARITY2=1.3
SC_POPULARITY3=1.2
SC_POPULARITY4=1.1
SC_ARTIST1=2
SC_ARTIST2=1.8
SC_ARTIST3=1.5
SC_ARTIST4=1.4
SC_ARTIST5=1.3
SC_ARTIST6=1.2
SC_ARTIST7=1.1

#Nella chiamata passare a tuttigeneri tuttigeneri=dati['genres'].tolist()
def generiPreferiti(tuttigeneri):

    '''
    La funzione restituisce un dizionario contenente le occorrenze dei generi
    delle canzoni in input

    :param tuttigeneri: lista contente tutti i generi delle canzoni
    :return generi: dizionario contenente le occorrenze
    '''
    generi={}
    for listaGeneri in tuttigeneri:
        for genere in listaGeneri:
            if(generi.get(genere)==None):
                generi[genere]=1
            else:
                generi[genere]+=1
    return generi

#Nella chiamata passare a listapop listapop=dati['popularity'].tolist()
def popolaritaMedia(listapop):
    '''
    La funzione restituisce la popolarità media delle canzoni passate in input

    :param listapop: lista contenente la popolarità delle canzoni passate
    :return round(tot/i): viene ritornata la media delle popolarità passate in input
    '''
    tot=0
    i=0
    for pop in listapop:
        tot+=pop
        i+=1
    print(round(tot/i))
    return round(tot/i)

def popolaritaFasce(listapop):
    '''
    La funzione restituisce un dizionario contenente le occorrenze delle fasce
    di popolarità, stabilito all'interno della funzione, della lista di popolarità
    delle canzoni passate in input

    :param listapop: lista contenente la popolarità delle canzoni passate
    :return dict: dizionario contenente le occorrenze delle fasce di popolarità
    '''
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
    return dict



def contaEsplicite(listaexplicit):
    '''
    La funzione ritorna il numero di canzoni esplicite e il numero di canzoni non esplicite
    nell'insieme di canzoni in input

    :param listaexplicit: lista contenente canzoni da verificare se sono esplicite
    :return listaexplicit.count(True),listaexplicit.count(False): lista dove in corrispondenza di ogni canzone abbiamo valore
    1 se la canzone è esplicita
    0 altrimenti
    '''
    return listaexplicit.count(True),listaexplicit.count(False)
    

#Applica lambda per prendere solo anno prima di richiamare
#df['album_release_date']=df['album_release_date'].apply(lambda x : x[0:4])
def raccoltaAnni(listaAnni):
    '''
    La funzione calcola un dizionario contenente le occorrenze degli anni 
    delle canzoni passate come input

    :param listaAnni: lista contenente gli anni di uscita delle canzoni
    '''
    anni={}
    for anno in listaAnni:
        if(anni.get(anno)==None):
            anni[anno]=1
        else:
            anni[anno]+=1
    print(anni)


'''
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
'''
def creaPunteggioGenere(lista):
    '''
    La funzione restituisce un dizionario contenente il punteggio in base alle
    occerrenze dei generi

    :param lista: lista di generi
    :return punteggio: un dizionario contenente il punteggio relativo ad ogni genere
    '''
    punteggio={}
    generiFinali=(sorted(lista.items(),key=lambda x: x[1],reverse=True))
    for genere in generiFinali:
        if(genere[1]>30):
            punteggio[genere[0]]=SC_GENRE1
        else:
            if(genere[1]>20 and genere[1]<=30):
                punteggio[genere[0]]=SC_GENRE2
            else:
                if(genere[1]>10 and genere[1]<=20):
                    punteggio[genere[0]]=SC_GENRE3
                else:
                    if(genere[1]>0 and genere[1]<=10):
                        punteggio[genere[0]]=SC_GENRE4
    return punteggio



def creaPunteggioPopolarita(popolarita):
    '''
    La funzione restituisce un dizionario contenente il punteggio in base alle 
    occorrenze delle fasce di popolarità

    :param popolarita: lista di popolarità
    :return punteggio: un dizionario contenente il punteggio relativo alla popolarità
    '''
    punteggio={}
    popolaritaFinale=(sorted(popolarita.items(),key=lambda x:x[1],reverse=True))
    for popolarita in popolaritaFinale:
        if(popolarita[1]>30):
            punteggio[popolarita[0]]=SC_POPULARITY1
        else:
            if(popolarita[1]>20 and popolarita[1]<=30):
                punteggio[popolarita[0]]=SC_POPULARITY2
            else:
                if(popolarita[1]>10 and popolarita[1]<=20):
                    punteggio[popolarita[0]]=SC_POPULARITY3
                else:
                    if(popolarita[1]>0 and popolarita[1]<=10):
                        punteggio[popolarita[0]]=SC_POPULARITY4
    return punteggio

def creaPunteggioArtisti(nameArtisti):
    '''
    La funzione restituisce il punteggio in base alla posizione
    dell'artista all'interno della lista(nameArtisti)

    :param nameArtisti: lista di artista
    :return punteggio: un dizionario contenente il punteggio relativo agli artisti
    '''
    punteggio={}
    i=0
    for name in nameArtisti:
        i+=1
        if(i>=0 and i<=3):
            punteggio[name]=SC_ARTIST1
        else:
            if(i>3 and i<=10):
                punteggio[name]=SC_ARTIST2
            else:
                if(i>10 and i<=20):
                    punteggio[name]=SC_ARTIST3
                else:
                    if(i>20 and i<=30):
                        punteggio[name]=SC_ARTIST4
                    else:
                        if(i>30 and i<=40):
                            punteggio[name]=SC_ARTIST5
                        else:
                            if(i>40 and i<=50):
                                punteggio[name]=SC_ARTIST6
                            else:
                                if(i>50 and i<=60):
                                    punteggio[name ]=SC_ARTIST7

    return punteggio

def getSingleGenre(song):
    '''
    La funzione restituisce un singolo genere dalla lista di generi 
    contenuti nella canzone passata in input

    :param song: canzone passata in input
    :return maxvalue: genere con più occorrenze contenuto all'interno della lista dei generi di song
    '''
    macro={"rock":0, "pop":0, "metal":0, "rap":0, "indie":0, "jazz":0, "electro":0, "house":0, "country":0, "techno":0, "classic":0, "blues":0, "r&b":0, "trap":0, "dance":0, "hip hop":0, "edm":0, "binaural":0,"reggae":0,"punk":0,"lo-fi":0} 
    listaGeneri=song['genres']
    

    for genere in listaGeneri:
        for chiave in macro:
            if chiave in genere:
                macro[chiave]+=1
    maxvalue=max(macro, key=macro.get)
    return maxvalue



def dataSongsClean(df):
    '''
    La funzione pulisce il dataframe e restituisce il dataframe privo di impurità e leggibile per altre funzioni

    :param df: dataframe passato in input
    :return df: dataframe restituito privo di impurità
    '''
    df = df[df.genres != '[]']
    df = df[df.energy != np.NaN]
    df = df[df.energy != ""]
    df = df[df.id != np.NaN]
    df = df[df.id != ""]
    df['genres'] = df['genres'].str.replace('"\[','\[')
    df['genres'] = df['genres'].str.replace('\]"','\]')
    df['genres']=df['genres'].str.replace('""','"')
    df['genres']=df['genres'].apply(lambda x:ast.literal_eval(x))
    df = df[df.popularity != 0]
    df['album_release_date']=df['album_release_date'].astype('str')
    nan_value = float("NaN")
    df['id'].replace("", nan_value, inplace=True)
    df.dropna(subset = ["id"], inplace=True)
    return df



def assignSingleGenre(fulldf):
    '''
    La funzione assegna nella colonna genere contenuta in fulldf (DataFrame) passato in input
    un singolo genere sulla base della lista genres associata alle canzoni

    :param fulldf: dataframe passato in input
    :return fulldf: dataframe con singolo genere nella colonna "genere"
    '''
    fulldf["genere"]=""
    for idx in fulldf.index:
        genere=getSingleGenre(fulldf.loc[idx])
        fulldf.at[idx,"genere"]=genere
    
    return fulldf

def one_to_all_fav_artists(fulldf,dict_artisti):
    '''
    La funzione restituisce un dataframe contenete una nuova colonna
    "like" dove in ogni riga contiene il valore
    1 se l'artista è uno dei preferiti dell'utente o se ha prodotto una delle canzoni preferite dall'utente
    0 altrimenti

    :param fulldf: dataframe passato in input
    :dict_artisti: dizionario contenente gli artisti preferiti
    :return fulldf: dataframe contenente i nuovi dati
    '''
    for idx in fulldf.index:
        artista=fulldf.loc[idx]['artist_name']
        if(not dict_artisti.get(artista)==None):
            fulldf.at[idx, 'like']=1
    return fulldf
#Prende il 30% delle canzoni con punteggio più alto
def topScoreRow(df):
    '''
    La funzione restituisce un dataframe contenente in testa
    le migliori canzoni(nello specifico caso della funzione 30%)
    aggiungendo una nuova colonna al dataframe 'topScore' la quale avrà valore
    1 se rientra nella top 30%
    0 altrimenti

    :param df: dataframe passato in input
    :return df: nuovo dataframe contenente in testa le top canzoni e la nuova colonna 'topScore'
    '''
    df['topScore']=0
    count=len(df.index)
    percentuale=(count*30)/100
    topRow=df.nlargest(round(percentuale),['score'])
    for idx in topRow.index:
        df.at[idx,'topScore']=1
    print(topRow)
    return df
    

