

#########################################
# Jeu de données notes
#########################################

notes=read.table("notes_ACP.txt")


#############
# Question 6b :Représentation des individus
#############

# C : composantes principales
# Représentation des individus dans le premier plan principale
plot(C[,1:2],type="n",xlab='PC1',ylab='PC2')
text(C[,1:2],labels=row.names(notes),cex=1.5)
title(main="Projection sur les 2 premiers axes principaux")
lines(c(min(C[,1]),max(C[,1])),c(0,0),lty=2)
lines(c(0,0),c(min(C[,2]),max(C[,2])),lty=2)




#############
# Question 9 :Représentation des variables
#############
cercle_correlation=cor(X,C)

a=seq(0,2*pi,length=100)
plot(cos(a), sin(a), type='l',lty=3,xlab='comp 1', ylab='comp
2',main="Cercle des corrélations" )
arrows(0,0,cercle_correlation[,1],cercle_correlation[,2],col=2)
text(cercle_correlation[,1],cercle_correlation[,2],labels=colnames(notes))



