#bibliotheques utilisees 
library(FactoMineR)
library(Factoshiny)
library(factoextra)
library(ade4)
#chargement des donnees
data <- read.table(file.choose(),header=T,sep=",")
data
#Caclcul des fréquences 
i=0
while(i <ncol(data)){
	i=i+1
	data[,i]=as.factor(data[,i])
}
summary(data$view)
#histogramme des donnees 
barplot(table(data$DonaldT), ylab = "Count", col="blue", las = 2)
#Creation du tableau disjonctif complet 
disj <-acm.disjonctif(data)
disj
#calcul des pondérations 
matX<-as.matrix(disj)
apply(matX,2,sum)
#Lancement de l'AFCm
afcm <- MCA(data, quali.sup=(7:10))
#Valeurs propres 
get_eigenvalue(afcm)
#Percentage of explained variances
fviz_eig(afcm, addlabels = TRUE, col="blue")
get_mca_ind(afcm)
#Representation du biplot variable-individus 
fviz_mca_biplot (afcm, repel = TRUE,ggtheme = theme_minimal())
#Representation des variables
fviz_mca_var (afcm, choice = "mca.cor",repel = TRUE, ggtheme = theme_minimal ())
#Categorie des variables selon la qualite de representation cos^2
fviz_mca_var(afcm, col.var = "cos2", gradient.cols = c("#00AFBB", "#E7B800", "#FC4E07"),repel = TRUE, ggtheme = theme_minimal())
#MCA map factor
fviz_ellipses(afcm, c("view", "DonaldT"),geom = "point")

#Utilisation de la librairie graphique factoshiny 
res <- Factoshiny(data)
#Creation du tableau de contingence 
tableau<-table(data$view,data$DonaldT) 
tableau
#marge PL
margin.table(tableau,1)
#Marge PC 
margin.table(tableau,2)
#effectif total 
margin.table(tableau)
#le tableau disjonctif 
addmargins(tableau)
#Realisation de l'AFC
afc<- CA(tableau)