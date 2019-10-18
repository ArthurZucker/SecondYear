###################################################
## Mise oeuvre exo TD 
###################################################

#exo3 TD2 
x=c(3.7,3.4,4.2,3.8,3.9,4,3.5,3.6,4.3,3.3)
?shapiro.test
shapiro.test(x)

?t.test
t.test(x,mu=4, alternative="less")


n=length(x)
#borne sup IC :
mean(x)+qt(0.95,n-1)*sd(x)/sqrt(n)



#exo1 TD2 
?prop.test
prop.test(...)

# si test exact :
?binom.test
binom.test(13,55,0.25,alternative="less")


#courbe puissance à la main
n=55
theta1=0.23
puissance=pnorm((-1.65*sqrt(0.25*0.75/n)+0.25-theta1)/sqrt(theta1*(1-theta1)/n))


puissance=function(theta1,n)
{ power=pnorm((-1.65*sqrt(0.25*0.75/n)+0.25-theta1)/sqrt(theta1*(1-theta1)/n))
 return(power)
}
vect_theta1=seq(?, ?, by=0.001)
vect_power_n55=puissance(vect_theta1,n=55)
vect_power_n3000=puissance(vect_theta1,n=3000)
plot(vect_theta1,vect_power_n55,type="l")
lines(vect_theta1,vect_power_n3000,type="l",col=2)




#exo2 TD2
?power.t.test
power.t.test(...)


#courbe puissance avec la fonction power.t.test :
mu1=seq(6,8,by=0.01)
delta=mu1-6
toto=power.t.test(...)
plot(mu1,toto$power, type='l',main="n=40")


# n tel que puissance soit au moins de 90%
?power.t.test

###################################################
## Tests Ajustement
###################################################

#exo 4
# échantillon de variables aléatoires de loi uniforme sur [0,1] :
x= 
  
# fonction de répartition empirique :  
fn=ecdf(x)
plot(fn, verticals=TRUE, do.points=FALSE)
  
# superposer la fonctin de répartition de la loi  uniforme sur [0,1]

# test de Kolmagorov Smirnov
?ks.test


A relancer pour plusieurs échantillons x.

#exo 5
# simulation des échantillons :
x=
y=

# Droites de Henry :
?qqnorm
par(mfrow=c(1,2))

# test de Kolmagorov Smirnov : 

# test de Shapiro :

# un peu de stat descriptive :
hist(x,prob=TRUE)
abscisses=seq(min(x)-10,max(x)+10,0.1)
lines(abscisses,dnorm(abscisses,mean(x),sd(x)),col=2)

hist(y,prob=TRUE)
abscisses=seq(min(y)-10,max(y)+10,0.1)
lines(abscisses,dnorm(abscisses,mean(x),sd(x)),col=2)

###################################################
## Choix du test
###################################################

#exo 6
x=c(602,464,483,506,497,544,486,531,496,501)
y=c(487,489,470,482,494,500,504,537,482,550)
# un peu de stat descriptive :
boxplot(x,y)



#exo 7
x=c(750,860,950,830,750,680,720,810,820)
y=c(850,880,930,860,800,740,760,790,825)


# exo 8 :
x <- c(1.83,  0.50,  1.62,  2.48, 1.68, 1.88, 1.55,1.2, 0.7)
y <- c(0.878, 0.647, 0.598, 2.05, 1.06, 1.29, 1.06, 3.14, 1.29)




#exo 9
presence=c(4,18,10)
absence=c(36,52,80)
tab=rbind(presence, absence)
colnames(tab)=c('zone1','zone2','zone3')
rownames(tab)=c('presence','absence')
tab
 


#exo 10



