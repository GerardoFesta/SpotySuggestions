library(ggplot2)
library(reshape2)

dati <- read.csv("LeaveOneProjectOut results path", sep = ",", header = TRUE, stringsAsFactors=FALSE)

                                                                          
paper <- read.csv("paper results_path", sep=";")
paper <- paper[paper$Dataset == "Full dataset",]
extratrees <- paper[paper$Model == "ExtraTrees",]
svm <- paper[paper$Model == "SVM",]
knn <- paper[paper$Model == "KNN",]
if_ <- paper[paper$Model == "IF",]
ocsvm <- paper[paper$Model == "OCSVM",]
lof <- paper[paper$Model == "LOF",]

auc_df <- data.frame(
  
  MLP = dati$Auc,
  extratrees = extratrees$AUC,
  svm = svm$AUC,
  knn = knn$AUC,
  if_ = if_$AUC,
  ocsvm = ocsvm$AUC,
  lof = lof$AUC

)

F1_df <- data.frame(
  
  MLP = dati$F1,
  extratrees = extratrees$F.measure,
  svm = svm$F.measure,
  knn = knn$F.measure,
  if_ = if_$F.measure,
  ocsvm = ocsvm$F.measure,
  lof = lof$F.measure
  
)

precision_df <- data.frame(
  
  MLP = dati$Precision,
  extratrees = extratrees$Precision,
  svm = svm$Precision,
  knn = knn$Precision,
  if_ = if_$Precision,
  ocsvm = ocsvm$Precision,
  lof = lof$Precision
  
)

recall_df <- data.frame(
  
  MLP = dati$Recall,
  extratrees = extratrees$Recall,
  svm = svm$Recall,
  knn = knn$Recall,
  if_ = if_$Recall,
  ocsvm = ocsvm$Recall,
  lof = lof$Recall
  
)

data_mod_auc <- melt(auc_df, id.vars='MLP', 
                  measure.vars=c('MLP', 'svm', 'knn', 'extratrees', 'if_', 'ocsvm', 'lof'))

data_mod_f1 <- melt(F1_df, id.vars='MLP', 
                    measure.vars=c('MLP', 'svm', 'knn', 'extratrees', 'if_', 'ocsvm', 'lof'))

data_mod_prec <- melt(precision_df, id.vars='MLP', 
                    measure.vars=c('MLP', 'svm', 'knn', 'extratrees', 'if_', 'ocsvm', 'lof'))
data_mod_recall <- melt(recall_df, id.vars='MLP', 
                      measure.vars=c('MLP', 'svm', 'knn', 'extratrees', 'if_', 'ocsvm', 'lof'))


ggplot(data=data_mod_auc,mapping = aes(x="Auc",y=value, color=variable))+geom_boxplot()+scale_y_continuous(
  breaks = seq(0, 1, by = 0.1),
  limits= c(0.0, 1))+theme(axis.text=element_text(size=14,face="bold"),
                           axis.title=element_text(size=14,face="bold"),
                           legend.title = element_text(color = "blue", size = 14),
                           legend.text = element_text(size = 16))

ggplot(data=data_mod_f1,mapping = aes(x="F1",y=value, color=variable))+geom_boxplot()+scale_y_continuous(
  breaks = seq(0, 1, by = 0.1),
  limits= c(0.0, 1))+theme(axis.text=element_text(size=14,face="bold"),
                           axis.title=element_text(size=14,face="bold"),
                           legend.title = element_text(color = "blue", size = 14),
                           legend.text = element_text(size = 16))

ggplot(data=data_mod_prec,mapping = aes(x="Precision",y=value, color=variable))+geom_boxplot()+scale_y_continuous(
  breaks = seq(0, 1, by = 0.1),
  limits= c(0.0, 1))+theme(axis.text=element_text(size=14,face="bold"),
                           axis.title=element_text(size=14,face="bold"),
                           legend.title = element_text(color = "blue", size = 14),
                           legend.text = element_text(size = 16))

ggplot(data=data_mod_recall,mapping = aes(x="Recall",y=value, color=variable))+geom_boxplot()+scale_y_continuous(
  breaks = seq(0, 1, by = 0.1),
  limits= c(0.0, 1))+theme(axis.text=element_text(size=14,face="bold"),
                           axis.title=element_text(size=14,face="bold"),
                           legend.title = element_text(color = "blue", size = 14),
                           legend.text = element_text(size = 16))

