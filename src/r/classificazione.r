
#importazione dataset
df<-read.csv("READY_ARTISTI_GENERI.csv")
df$genere<-factor(df$genere,
                     levels=c( "rock", "pop", "metal", "rap", "indie", "jazz", "electro", "house", "country",
                               "techno", "classic", "blues", "r&b", "trap", "dance", "hip hop", "edm", "binaural","reggae","punk","lo-fi"))

date<-as.integer(strtrim(df$album_release_date,4))
df$diffy<-2022-date

#librerie necessarie
library(caret)
library(rpart)
library(rpart.plot)

#Zona di test

#split in train e test usando campionamento stratificato
idx<-createDataPartition(df$TopArtista, times=1,p=0.7)
train1<-df[idx$Resample1,]
test1<-df[-idx$Resample1,]
fit1<-rpart(TopArtista ~ danceability+energy+key+loudness+speechiness+acousticness+instrumentalness+liveness+valence+tempo+duration_ms
           +explicit+diffy+genere,
           data    = train1, 
           method  = "class")

pred1 <- predict(fit1,newdata = test1,type="class")

confusionMatrix(pred1,factor(test1$TopArtista), positive="1")
#Fine zona di test

corrplot::corrplot(cor(df[,c("danceability","energy","key","loudness","speechiness","acousticness","instrumentalness","liveness","valence","tempo","duration_ms",
                             "diffy")]))


library(ggplot2)
ggplot(data=df, mapping=aes(x=danceability))+geom_histogram(fill="blue")
ggplot(data=df, mapping=aes(x=danceability))+geom_density(fill="blue")


#stima modello su training set

#classificazione
fit<-rpart(TopArtista ~ danceability+energy+key+loudness+speechiness+acousticness+instrumentalness+liveness+valence+tempo+duration_ms
           +explicit+diffy+genere,
           data    = df, 
           method  = "class")




vip::vip(fit) 

#plot albero
rpart.plot(fit)

plotcp(fit) #grafico errore di cross-validazione

upp<-min(fit$cp[,4])+fit$cp[which.min(fit$cp[,3]),5]
best<-max(fit$cp[fit$cp[,4]<=upp,1])
nf<-prune(fit, cp=best) #tagliare albero (variare cp in base regola one standard error)

rpart.plot(nf) #plot nuovo albero


test<-read.csv("READY_REC.csv")
date<-as.integer(strtrim(test$album_release_date,4))
test$diffy<-2022-date
#predezioni 
pred <- predict(fit,newdata = test,type="prob")
test$p_classificazione<-pred[,2]
pred_class <- predict(fit,newdata = test,type="class")
test$TopArtista<-pred_class


write.table(test,"OutputR.csv", sep=",", col.names=NA, qmethod = "double")


sort(pred,decreasing = T)









