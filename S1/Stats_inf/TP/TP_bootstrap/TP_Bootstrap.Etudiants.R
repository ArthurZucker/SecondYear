## EXO 1 : simu

MC.simus <- function(theta, Nsim)
{ sortie =rep(NA, Nsim)
  for (nsim in 1:Nsim)
       {  x=...
          sortie[nsim]=...
        }
return(sortie)
}

n=100
Nsim=1000
theta=0.5
theta.chap=MC.simus(theta, Nsim)

par(mfrow=c(1,2))
hist(theta.chap,prob=T)
xx= seq(0,1,by=0.01)
lines(xx, dnorm(xx, theta, sqrt(theta*(1-theta)/n)), col=2)

plot(density(theta.chap))
xx= seq(0,1,by=0.01)
lines(xx, dnorm(xx, theta, sqrt(theta*(1-theta)/n)), col=2)




######################################
## EXO 2 
# Q.1)
n=100
theta=0.5
set.seed(1)        #fixe l'aléa : vous aurez tous le même jeu de données
x=rbinom(n,1,theta)

theta.chap=...

# Q.2a)


# Q.2b)
mean.bootstrap <- function(x, B)
{ ech_boot_mean =rep(NA,B)
  n=length(x)
  for (b in 1:B)
  { xstar=...
    ech_boot_mean[b]=...  } 
  return(ech_boot_mean)
}
ech_boot_mean=mean.bootstrap(x, B=1000)


# Q.2c)
library(boot)
moyenne <- function(x,i) {return(mean(x[i]))}
bootsample_mean=boot(x,moyenne,R=1000)
names(bootsample_mean)



# Q.3a)
par(mfrow=c(1,2))
hist(bootsample_mean$t)
plot(density(bootsample_mean$t))


# Q.3b)


# Q.3c)
plot(density(sqrt(n)*(bootsample_mean$t-mean(x))))
xx= seq(-2,2,by=0.01)
lines(xx, dnorm(xx,0,sqrt(theta*(1-theta))), col=2)


#Q.4)
quantile(bootsample_mean$t, c(0.025,0.975)) 
 
ICboot_perc<-boot.ci( bootsample_mean,conf=0.95,type="perc")
ICboot_perc
 
ICboot_bca <-boot.ci(bootsample_mean,conf=0.95,type="bca")
ICboot_bca


#D'apres TCL :
Binf=mean(x)-1.96*sd(x)/sqrt(n)
Bsup=mean(x)+1.96*sd(x)/sqrt(n)
Binf
Bsup



######################################
## EXO 3 
n=1000
set.seed(1)
x<-rcauchy(n,location=1)
true.mediane = 1               #médiane théorique




#####################################
## EXO 4
goudron=c(0.45,0.77,1.07,1.03,1.34,1.14,1.15,0.9,0.55,1.15)
nicotine=c(11,13,14,15,17,18,14.5,13.5,8.5,16.5)
tabac=cbind(goudron,nicotine)
n=length(nicotine)





