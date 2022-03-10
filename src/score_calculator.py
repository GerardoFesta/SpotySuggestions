from doctest import ELLIPSIS_MARKER
import pandas as pd
import ast
import numpy as np
from score_assigner import creaPunteggioGenere

SC_TOP30_SONGS=1.9
SC_TOP60_SONGS=1.7
SC_TOP90_SONGS=1.5
SC_PREFERITI=0.75
SC_PLAYLIST=0.7

def scoreGeneriTopSongs(songs):
    dict={}
    dict2={}
    dict3={}
    dict4={}
    score_temp=0
    i=0
    while i<30 :
        song=songs[i]
        if (song['genere'] not in dict.values()):
            dict[song['values']]=1
        else:
            dict[song['values']]+=1
        i+=1
    
    while i<60 :
        song=songs[i]
        if (song['genre'] not in dict2.values()):
            dict2[song['values']]=1
        else:
            dict2[song['values']]+=1
        i+=1

    while i<90 :
        song=songs[i]
        if (song['genre'] not in dict3.values()):
            dict3[song['values']]=1
        else:
            dict3[song['values']]+=1
        i+=1

    
    
    for k in dict:

        if (k not in dict4.values()):
            dict4[k]=0
        if(k in dict2.values()):
            if(k in dict3.values()):
                score_temp=dict[k]*SC_TOP30_SONGS+dict2[k]*SC_TOP60_SONGS+dict3[k]*SC_TOP90_SONGS
                del dict2[k]
                del dict3[k]
                dict4[k]+=score_temp
            else:
                score_temp=dict[k]*SC_TOP30_SONGS+dict2[k]*SC_TOP60_SONGS
                del dict2[k]
                    
                dict4[k]+=score_temp
        else:
            if(k in dict3.values()):
                score_temp=dict[k]*SC_TOP30_SONGS+dict2[k]*SC_TOP90_SONGS
                del dict3[k]
                    
                dict4[k]+=score_temp
            else:
                score_temp=dict[k]*SC_TOP30_SONGS
                dict4[k]+=score_temp


    for k in dict2:

        if (k not in dict4.values()):
            dict4[k]=0
            if(k in dict3.values()):

                score_temp=dict2[k]*SC_TOP60_SONGS+dict3[k]*SC_TOP90_SONGS
                
                del dict3[k]
                dict4[k]+=score_temp
            else:
                score_temp=dict2[k]*SC_TOP60_SONGS
                
                    
                dict4[k]+=score_temp
            
    for k in dict3:
         if (k not in dict4.values()):
            dict4[k]=0
            score_temp=dict2[k]*SC_TOP90_SONGS
                
                    
            dict4[k]+=score_temp
    

    return dict4


def scoreGeneriPreferiti(listaTop, listaPref):
    dict = creaPunteggioGenere(listaTop)
    dict1 ={}
    dict2 ={}

    for song in listaPref:
        if (song['genere'] not in dict1.values()):
            dict1[song['genere']]=1
        else:
            dict1[song['genere']]+=1

    for genere in dict1:
        if (genere in dict.values()):
            dict2[genere]=dict1[genere]*dict[genere]*SC_PREFERITI
        else:
            dict2[genere]=dict1[genere]
    

    return dict2

def scoreGeneriPlaylist(listaTop, listaPlaylist):
    dict = creaPunteggioGenere(listaTop)
    dict1 ={}
    dict2 ={}

    for song in listaPlaylist:
        if (song['genere'] not in dict1.values()):
            dict1[song['genere']]=1
        else:
            dict1[song['genere']]+=1

    for genere in dict1:
        if (genere in dict.values()):
            dict2[genere]=dict1[genere]*dict[genere]*SC_PLAYLIST
        else:
            dict2[genere]=dict1[genere]
    

    return dict2



    
 














     
