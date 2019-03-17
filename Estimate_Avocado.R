#Data is provided by kaggle.com: 
#https://www.kaggle.com/neuromusic/avocado-prices#avocado.csv

#library
library(data.table)

avoc_org<-fread("avocado.csv")
avoc_new<-avoc_org[,2:14]
avoc_new<-avoc_new[year==2017|year==2018]

price<-dcast(avoc_new,region+type~ .,mean,value.var=c('AveragePrice'))
setnames(price, ".", "SingleAVGPrice")

nontype<-dcast(avoc_new,region~ .,mean,value.var=c('AveragePrice'))
setnames(nontype, ".", "NonTypeAvgPrice")

setkey(nontype, region)
setkey(price, region)
new_price<-merge(price, nontype)

fwrite(new_price, "AvocadoPrice.csv")
