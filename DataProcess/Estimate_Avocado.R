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
nontype$type<-'None'

nonprice_new<-nontype$region
nonprice_new<-data.table(nonprice_new)
setnames(nonprice_new, "nonprice_new", "region")
nonprice_new$type<-nontype$type
nonprice_new$SingleAVGPrice<-nontype$SingleAVGPrice

Avocado<-rbind(price, nonprice_new)

attach(Avocado)
Avocado <- Avocado[order(region),] 
detach(Avocado)

fwrite(Avocado, "AvocadoPrice.csv")
