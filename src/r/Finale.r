#importazione dataset

df<-read.csv("READY_DATASET.csv")
df$genere<-factor(df$genere,
                  levels=c( "rock", "pop", "metal", "rap", "indie", "jazz", "electro", "house", "country",
                            "techno", "classic", "blues", "r&b", "trap", "dance", "hip hop", "edm", "binaural","reggae","punk","lo-fi"))

df$like<-factor(df$like)
levels(df$like)<-c("No","Yes")
date<-as.integer(strtrim(df$album_release_date,4))
df$diffy<-2022-date


library(caret)
library(rpart)
library(rpart.plot)
library(randomForest)
library(ggplot2)
library(vip)
library(corrplot)
library(dplyr)



## EDA score
num<-df[,c("score","danceability","energy","key","loudness","speechiness","acousticness","instrumentalness","liveness","valence"
           ,"tempo","duration_ms")]

corrplot(cor(num))

ggplot(data=df,mapping = aes(x=genere,y=score))+geom_boxplot()
ggplot(data=df,mapping = aes(x=explicit,y=score))+geom_boxplot()

df$int<-cut(df$diffy,breaks = 4,labels=c("[0,15]","(15,30]","(30,45]","(45,61]"))


sco_int<-df%>%
  group_by(int)%>%
  summarise(media=mean(score))

ggplot(data=sco_int,aes(x=int,y=media))+geom_col(fill="red",col="black")+xlab("Anni dall'Uscita")+ylab("Media Score")


## EDA Top
df_top<-df%>%
  select(like,score, danceability , energy , key , loudness , speechiness , acousticness , instrumentalness , liveness , valence 
         , tempo , duration_ms )


df_gg<-df_top%>%
  group_by(like)%>%
  summarise(Danceability=mean(danceability),Energy=mean(energy), Loudness=mean(loudness), Speechiness=mean(speechiness)
            ,Acousticness=mean(acousticness), Instrumentalness=mean(instrumentalness), Liveness=mean(liveness), Duration_ms=mean(duration_ms))


df_gg

ggplot(data=df,aes(genere,fill=like))+geom_bar(position="dodge")
ggplot(data=df,aes(explicit,fill=like))+geom_bar(position="dodge")
ggplot(data=df,aes(y=score,x=like))+geom_boxplot() 

ggplot(df,aes(danceability,fill=like))+geom_density(alpha=0.5) #per cambiare cambiate danceability con altre variabili numeriche!!



idx<-createDataPartition(df$like, times=1,p=0.7)
train<-df[idx$Resample1,]
test<-df[-idx$Resample1,]



# REGRESSIONE

reg_tree<-rpart(score ~ danceability+energy+key+loudness+speechiness+acousticness+instrumentalness+liveness+valence+tempo+duration_ms
           +explicit+diffy+genere,
           data    = train, 
           method  = "anova")


#tagliare albero
upp<-min(reg_tree$cp[,4])+reg_tree$cp[which.min(reg_tree$cp[,3]),5]
best<-max(reg_tree$cp[reg_tree$cp[,4]<=upp,1])
nf<-prune(reg_tree, cp=best) #tagliare albero (variare cp in base regola one standard error)
rpart.plot(nf) #albero tagliato




pred<-predict(reg_tree,test) # se vuoi utilizzare albero tagliato sostituisci reg_tree con nf
MPE<-100*mean((test$score-pred)/test$score) #mean percentage error
MAPE<-100*mean(abs(pred-test$score)/test$score) #mean absolute percentage error

rpart.plot(reg_tree)
plotcp(reg_tree)
vip(reg_tree)




ris_reg<-cbind(RMSE=RMSE(pred,test$score),MAE=MAE(pred,test$score),MPE=MPE,MAPE=MAPE)


reg_lm<-lm(score ~ danceability+energy+key+loudness+speechiness+acousticness+instrumentalness+liveness+valence+tempo+duration_ms
           +explicit+diffy,
           data    = train)


coef_lm<-coef(reg_lm)[2:length(coef(reg_lm))]
df_parametri<-data.frame(Parametri=names(coef_lm)[2:length(coef_lm)], Stima=coef_lm[2:length(coef_lm)])
rownames(df_parametri)<-NULL
col<-ifelse(df_parametri$Stima>=0,"blue","red")
ggplot(df_parametri,aes(x=Parametri,y=Stima))+geom_col(fill=col,col="black")+coord_flip()





pred<-predict(reg_lm,test)
MPE<-100*mean((test$score-pred)/test$score) #mean percentage error
MAPE<-100*mean(abs(pred-test$score)/test$score) #mean absolute percentage error

ris_reg<-rbind(ris_reg,cbind(RMSE=RMSE(pred,test$score),MAE=MAE(pred,test$score),MPE=MPE,MAPE=MAPE))




rf<-randomForest(score ~ danceability+energy+key+loudness+speechiness+acousticness+instrumentalness+liveness+valence+tempo+duration_ms
                 +explicit+diffy+genere,
                 data    = train)


vip(rf)
plot(rf)


pred<-predict(rf,test)
MPE<-100*mean((test$score-pred)/test$score) #mean percentage error
MAPE<-100*mean(abs(pred-test$score)/test$score) #mean absolute percentage error

ris_reg<-rbind(ris_reg,cbind(RMSE=RMSE(pred,test$score),MAE=MAE(pred,test$score),MPE=MPE,MAPE=MAPE))

rownames(ris_reg)<-c("Regression Tree","Linear Regression","Random Forest")

ris_reg