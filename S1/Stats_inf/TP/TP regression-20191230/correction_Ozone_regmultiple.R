data=read.csv2("ozone.csv")
attach(data)
head(data)

data2=data[, -c(1, 13,14)]
res=lm(maxO3 ~., data2)
library(car)
vif(res)

> vif(res)
       T9       T12       T15       Ne9      Ne12      Ne15       Vx9      Vx12 
 6.645125 18.060645 14.477998  3.190681  5.242639  2.944332  3.105152  4.684647 
     Vx15    maxO3v 
 3.564266  1.702196 


data3=data2[, -3]
res=lm(maxO3 ~., data3)
> vif(res)
      T9      T15      Ne9     Ne12     Ne15      Vx9     Vx12     Vx15 
5.078892 6.730541 3.127636 4.024225 2.451119 2.996552 4.492912 3.520511 
  maxO3v 
1.695569 

par(mfrow=c(2,2))
plot(res)
abs(rstudent(res))[abs(rstudent(res))>2]


data4=data3[-58,]
res=lm(maxO3 ~ ., data4)
par(mfrow=c(2,2))
plot(res)
abs(rstudent(res))[abs(rstudent(res))>2]


data5=data3[-c(52,58),]
res=lm(maxO3 ~ ., data5)
par(mfrow=c(2,2))
plot(res)
abs(rstudent(res))[abs(rstudent(res))>2]

data6=data3[-c(34,52,58,79),]
res=lm(maxO3 ~ ., data6)
par(mfrow=c(2,2))
plot(res)
abs(rstudent(res))[abs(rstudent(res))>2]
> shapiro.test(res$residuals)
	Shapiro-Wilk normality test

data:  res$residuals
W = 0.98483, p-value = 0.2593
> abs(rstudent(res))[abs(rstudent(res))>2]
       15       18       46 
2.155459 2.104125 2.272160 
# on peut toujours peaufiner mais on va s'arreter là.  
# RQ : 95% des residus sont entre -2 et 2, donc on peut avoir des résidus plus grand ou plus petit. Juste s'assurer qu'il n'y en a pas trop, et qu'ils ne sont pas trop éloignés de +ou -2.

# Vérfions les leviers : 
attach(data6)
influence=influence.measures(res)
leviers=influence$infmat[,"hat"]
dim(data6)
n=dim(data6)[1]; p= dim(data6)[2]; 
> 2*p/n;
[1] 0.1851852

leviers[leviers > 2*p/n]
       18        23       104 
0.2065235 0.2317875 0.2223805 

influence=influence.measures(res)
leviers=influence$infmat[,"hat"]
n=length(maxO3); p= 10; 2*p/n;

#observation n°23 ? 
par(mfrow=c(3,3))
for (i in 2:10)    
{plot(data6[,i],data6$maxO3,xlab=colnames(data6)[i])
points(data6[23,i], data6$maxO3[23],col=2, pch="+")}
#rien de dramatique : l'observation 23 ne va pas perturber le modele
#On s'arrete là.


summary(res)     
       Estimate Std. Error t value Pr(>|t|)    
(Intercept) 26.69823   10.85734   2.459  0.01569 *  
T9           1.29168    0.83669   1.544  0.12586    
T15          0.99020    0.66599   1.487  0.14028    
Ne9         -2.42016    0.77539  -3.121  0.00237 ** 
Ne12        -2.20404    1.03618  -2.127  0.03592 *   
Ne15         1.08000    0.75504   1.430  0.15579     
Vx9          0.87972    0.74883   1.175  0.24292    
Vx12        -0.18792    0.85310  -0.220  0.82612    
Vx15         0.60358    0.75668   0.798  0.42699    
maxO3v       0.40249    0.05364   7.504 2.86e-11 ***   
Residual standard error: 11.75 on 98 degrees of freedom
Multiple R-squared:  0.8271,	Adjusted R-squared:  0.8113 
F-statistic:  52.1 on 9 and 98 DF,  p-value: < 2.2e-16


# Test de Fisher : p-value: < 2.2e-16  < 5% donc on rejette H0 donc au moins 1 variable explicative significative

# Test de Student pour chaque variable : 
# T9 
    # H0 : maxO3 ~    T15+Ne9+Ne12+ Ne15+Vx9+Vx12+Vx15+maxO3v
    # H1 : maxO3 ~ T9+T15+Ne9+Ne12+ Ne15+Vx9+Vx12+Vx15+maxO3v
    # pvalue= 0.12586 > 5% donc on ne rejette H0, donc T9 ne semble pas significative
# Ne9 : pvalue=0.00237 < 5% donc on rejette H0 donc Ne9 est significative 
# Donc sont significatives : Ne9, Ne12, max03v

# Test de Student unilatéral : 
#  positive ou négative en fonction signe de Estimate. 
#  influence significative si pvalue_uni = 1/2 * pvalue_bi < 0.05
# On trouve : Ne9 et Ne12 influence négative, maxO3v influence positive


# En se basant sur ce critère test de Student, on a envie de garder le modèle : 
resBON = lm(maxO3 ~ Ne9+Ne12+maxO3v, data6)
> anova(resBON, res)
Model 1: maxO3 ~ Ne9 + Ne12 + maxO3v
Model 2: maxO3 ~ T9 + T15 + Ne9 + Ne12 + Ne15 + Vx9 + Vx12 + Vx15 + maxO3v
  Res.Df   RSS Df Sum of Sq      F    Pr(>F)    
1    104 17404                                  
2     98 13526  6    3877.5 4.6821 0.0003147 ***
# au sens critère de Fisher, le sous modèle ne suffit pas. 
# Ca arrive, on a regardé des critères différents, donc on peut ne pas avoir les mêmes résultats. En fait dans le test de student, on teste les variables 1 par 1, les autres variables étant incluses dans le modèle. En fait dans summary(res) certaines pvalues sont proches de 10% (T9) donc il vaut peut être mieux les inclure dans le sous modèle. Si 
> resBON = lm(maxO3 ~ T9+ Ne9+Ne12+maxO3v, data6)
> anova(resBON, res)
Model 1: maxO3 ~ Ne9 + Ne12 + maxO3v + T9
Model 2: maxO3 ~ T9 + T15 + Ne9 + Ne12 + Ne15 + Vx9 + Vx12 + Vx15 + maxO3v
  Res.Df   RSS Df Sum of Sq      F Pr(>F)  
1    103 14945                             
2     98 13526  5    1419.1 2.0563 0.0774 .


#En pratique, il vaut mieux utiliser les procédures de choix de modele :
res0=lm(maxO3 ~1, data6)
modele_Stepwise=step(res0,scope=formula(res),direction="both")
>summary(modele_Stepwise)
Call:
lm(formula = maxO3 ~ maxO3v + Ne9 + Vx9 + T9 + Ne12)
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) 34.86073    9.56301   3.645 0.000422 ***
maxO3v       0.39595    0.05309   7.458 3.00e-11 ***
Ne9         -2.53943    0.75498  -3.364 0.001085 ** 
Vx9          1.36839    0.52434   2.610 0.010425 *  
T9           2.29984    0.49625   4.634 1.06e-05 ***
Ne12        -1.82331    0.87564  -2.082 0.039822 *  
Residual standard error: 11.72 on 102 degrees of freedom
Multiple R-squared:  0.821,	Adjusted R-squared:  0.8122 
F-statistic: 93.54 on 5 and 102 DF,  p-value: < 2.2e-16


# on trouve un autre modèle, ce qui est normal car ici critère AIC. Si on lance algo forward ou backward, on peut aussi trouver d'autres modèles.


# prediction ? par exemple pour ces données : 
newdata=data.frame(T9=15, maxO3v=100,  Ne9=5,  Vx9=0,  Ne12=6) 
predict(modele_Stepwise, newdata, interval="prediction")
      fit      lwr      upr
   85.31672 61.59854 109.0349





