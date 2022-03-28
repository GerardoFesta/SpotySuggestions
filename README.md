# SpotySuggestions
Progetto FIA 2021/2022

L'obiettivo del progetto è quello di eseguire un raffinamento dei consigli che Spotify fornisce al singolo utente, basandoci sulle sue abitudini d'ascolto.

Questi dati vengono ottenuti grazie all'interazione con l'API web di Spotify, per mezzo della libreria Spotipy.

L'obiettivo viene perseguito tramite strumenti di intelligenza artificiale, operando sia classificazione che regressione su due variabili create appositamente per questo scopo, sulla base proprio dei dati che vengono ricavati tramite Spotipy.

Nella cartella 'src' troviamo:

  -<b>data_extractor.py</b>: Contiene le funzioni necessarie per estrarre i dati relativi a canzoni preferite e più ascoltate, artisti preferiti, playlist e canzoni  consigliate da Spotify per l'utente. Le informazioni vengono salvate sotto forma di dataframe in file .csv
  
  -<b>data_utils.py</b>: Funzioni di utilità per l'estrazione dei dati. Principalmente permettono di ricevere risposte complete e permettono di manipolare i dati in modo da ottenere dataframe da risposte JSON
  
  -<b>main.py</b>: Contiene il flusso di autenticazione ed esecuzione dell'intero progetto
  
  -<b>score_assigner.py</b>: Contiene le funzioni in grado di assegnare lo score (variabile su cui viene effettuata la regressione) al dataset formato da canzoni preferite, playlist e canzoni più ascoltate dall'utente
  
  -<b>score_utils.py</b>: Contiene funzioni che permettono di stabilire il punteggio relativo a ogni categoria presa in analisi (artista, genere, provenienza della canzone, popolarità della canzone), in modo da permettere a score_assigner di associare il punteggio alle canzoni in base alle caratteristiche di queste ultime
  
  -<b>post_score_editor.py</b>: Contiene le funzioni che permettono di associare la variabile 'like' (usata per la classificazione) ad ogni canzone. Like sarà stabilita a partire dall'artista della canzone, solo se questo rientra tra uno degli artisti preferiti o tra gli artisti che hanno creato una canzone preferita dall'utente, allora avrà valore 1
  
  -<b>recom_preparation.py</b>: Contiene funzioni atte a preparare il dataset delle canzoni che Spotify consiglia all'utente per le operazioni di classificazione e regressione.
  
  -<b>rec_to_playlist.py</b>: Opera sul dataset dei consigliati di spotify su cui sono già state applicate le operazioni di predizione. Inserisce le migliori 30 canzoni in una nuova playlist dell'utente.
  
  -<b>r_scripts_loader.py</b>: Richiama lo script R da python
  
  -La cartella r, contenente <b>Finale.r</b>: Contiene tutte le operazioni di ML svolte, oltre alle operaziozioni di esplorazione del dataset. Si applica la classificazione con albero, random forest e knn, e la regressione con albero, random forest e regressione lineare.
