from pickle import FALSE
import pandas as pd
from score_utils import dataSongsClean, assignSingleGenre

rec_df=pd.read_csv("Rec_songs.csv")
rec_df=dataSongsClean(rec_df)
rec_df=rec_df.drop_duplicates(subset=['id'], inplace=False)
rec_df["score"]=""
rec_df["TopArtista"]=""
rec_df["genere"]=""
rec_df=assignSingleGenre(rec_df)

rec_df.to_csv("READY_REC.csv", index=False)
