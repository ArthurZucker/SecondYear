#Exo 1


donnees=read.table("anova2.txt")
# plan complet et equilibre

head(donnees)
str(donnees)
donnees$lux=as.factor(donnees$lux)
attach(donnees)
boxplot(RC ~ variete)
boxplot(RC ~ lux)


On peut modeliser un terme d'interaction entre variete et luminosite car
il y a des repetitions : n_ij=4 plants pour la combinaison (variete i,
luminosite j).

res=lm(RC ~ variete*lux,contrasts=c("contr.treatment", "contr.treatment"),donnees)
par(mfrow=c(2,2))
plot(res)
res=lm(log(RC) ~ variete*lux,contrasts=c("contr.treatment", "contr.treatment"),donnees)
plot(res)
> shapiro.test(res$residuals)
W = 0.96322, p-value = 0.7205
> bartlett.test(res$residuals ~ variete)
Bartlett's K-squared = 0.035368, df = 1, p-value = 0.8508
> bartlett.test(res$residuals ~ lux)
Bartlett's K-squared = 0.077969, df = 1, p-value = 0.7801


> summary(res)
Coefficients:
              Estimate Std. Error t value Pr(>|t|)    
(Intercept)     4.2135     0.2616  16.105 1.72e-09 ***
varieteB        0.9929     0.3700   2.683   0.0199 *  
lux2           -0.4335     0.3700  -1.172   0.2641    
varieteB:lux2  -0.5632     0.5232  -1.076   0.3029    
Residual standard error: 0.5232 on 12 degrees of freedom
Multiple R-squared:  0.5717,	Adjusted R-squared:  0.4647 
F-statistic:  5.34 on 3 and 12 DF,  p-value: 0.01438

On retrouve les estimations des autres parametres grace aux contraintes : tous les autres parametres sont nuls : variete1=0, lux1=0, variete1:lux1=0.


interaction.plot(variete, lux, response=log(RC))
# presque parallele: ne semble pas y avoir d'interaction
interaction.plot(lux, variete, response=log(RC))



library(car)
> Anova(res)                   #semblable a anova(res) car plan equilibré
            Df Sum Sq Mean Sq F value  Pr(>F)  
variete      1 2.0235 2.02352  7.3908 0.01866 *
lux          1 2.0456 2.04556  7.4713 0.01815 *
variete:lux  1 0.3172 0.31724  1.1587 0.30290  
Residuals   12 3.2855 0.27379                  


#pvalue= 0.30290 > 0.05
#Donc il ne semble pas y avoir  d'effet significatif du terme d'interaction. 

#pvalue=  0.01866 < 0.05. Donc il y a un effet significatif du
#facteur variété. 

#pvalue=  0.01815 < 0.05. Donc il y a un effet significatif du
#lux



Modele qui semble le plus pertinent : modele avec effet des facteurs variete et
lux, mais sans terme d'interaction.

resBON=lm(log(RC)~variete + lux,contrasts=c("contr.treatment", "contr.treatment"),donnees)

> summary(resBON)
Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)   4.3543     0.2280  19.102 6.78e-11 ***
varieteB      0.7113     0.2632   2.702   0.0181 *  
lux2         -0.7151     0.2632  -2.717   0.0176 *  
Residual standard error: 0.5264 on 13 degrees of freedom
Multiple R-squared:  0.5304,	Adjusted R-squared:  0.4581 
F-statistic: 7.341 on 2 and 13 DF,  p-value: 0.00735


#H1 : varieteB > varieteA. pvalue_uni=1/2*0.0181 < 0.05. Rejet de H_O : variété B meilleure.

#Si plus de 2 variétés : faire une correction (Bonferonni ou Tukey)

#H1 : lux2 < lux1. pvalue_uni=1/2*0.0176 < 0.05. Rejet de H_O : lux 1 meilleure.



comp.Tukey = TukeyHSD(aov(log(RC)~variete + lux))
comp.Tukey
$variete
         diff       lwr      upr     p adj
B-A 0.7112519 0.1426078 1.279896 0.0181192

$lux
          diff      lwr        upr     p adj
2-1 -0.7151158 -1.28376 -0.1464717 0.0176189



# pairwise.t.test se place en anova 1
#> pairwise.t.test(log(RC), variete, p.adjust="bonf")
#  A    
#B 0.042



############ Non paramétrique
library(rcompanion)
scheirerRayHare(RC~variete + lux, data=donnees)  # permet aussi de tester interaction meme si +
DV:  RC 
Observations:  16 
D:  0.9985294 
MS total:  22.66667 

            Df  Sum Sq      H p.value
variete      1  76.562 3.3827 0.06588
lux          1  81.000 3.5788 0.05852
variete:lux  1  18.063 0.7980 0.37168
Residuals   12 163.875               

#pairwise.wilcox.test en anova 1 (pas d'equivalent en anova 2?)
> pairwise.wilcox.test(RC , variete, p.adjust.method="bonferroni")
  A    
B 0.074
> pairwise.wilcox.test(RC , lux, p.adjust.method="bonferroni")
  1    
2 0.066
tout est moins puissant que anova 2 : rien de significatif au niveau 5% (en bilatéral)

# pb si pas de répétitions : 
> donnees2=donnees[c(1,5,9,13),]
> donnees2
    RC variete lux
1   78       A   1
5   64       A   2
9  137       B   1
13  64       B   2
> scheirerRayHare(RC~variete + lux, data=donnees2)

DV:  RC 
Observations:  4 
D:  0.9 
MS total:  1.666667 

            Df Sum Sq       H p.value
variete      1   0.25 0.16667 0.68309
lux          1   4.00 2.66667 0.10247
variete:lux  1   0.25 0.16667 0.68309
Residuals    0   0.00                
Warning message:
In anova.lm(Model) :
  ANOVA F-tests on an essentially perfect fit are unreliable

# mais ok si plan pas equilibre.


############
# Exo 2

donnees = read.table("fertilisation.rotation.txt")
head(donnees)
str(donnees)
donnees$fertilisation=as.factor(donnees$fertilisation)
attach(donnees)
res=lm(rendement ~ fertilisation*rotation,donnees)


# il y a des repetitions :
# table(fertilisation,rotation)
#             rotation
#fertilisation A B C D
#            1 3 3 2 3
#            2 2 5 2 5
# et le plan est complet mais non équilibré

par(mfrow=c(2,2))
plot(res)
#pas top
# on essaye transformation log
res=lm(log(rendement) ~ fertilisation*rotation)
#pas mieux. Donc on va essayer de supprimer des donnees. Lesquels ? Etude des residus.

res=lm(rendement ~ fertilisation*rotation,donnees)
abs(rstudent(res))[abs(rstudent(res))>2]
       6       15 
2.798171 2.022097 

donnees2=donnees[-c(6,15),]
attach(donnees2)
res=lm(rendement ~ fertilisation*rotation, donnees2)
par(mfrow=c(2,2))
plot(res)
> bartlett.test(res$residuals ~ fertilisation)
Bartlett's K-squared = 0.0034291, df = 1, p-value = 0.9533
> bartlett.test(res$residuals ~ rotation)
Bartlett's K-squared = 4.7037, df = 3, p-value = 0.1948
> shapiro.test(res$residuals)
W = 0.95906, p-value = 0.4447



#Ok, on travaille avec ces donnees.

interaction.plot(fertilisation,rotation, response=rendement)
interaction.plot(rotation,fertilisation response=rendement)
# semble se croiser légérement : légère intéraction ?




library(car)
>  Anova(res)  # car plan non equilibré
Anova Table (Type II tests)

Response: rendement
                       Sum Sq Df F value    Pr(>F)    
fertilisation          52.269  1 23.3280 0.0002206 ***
rotation               73.900  3 10.9941 0.0004500 ***
fertilisation:rotation 20.775  3  3.0906 0.0590256 .  
Residuals              33.609 15                      

#pas terme interaction ; effet fertilisation; effet rotation

res=lm(rendement ~ fertilisation+rotation,contrasts=c("contr.treatment", "contr.treatment"), donnees2)
summary(res)
Coefficients:
               Estimate Std. Error t value Pr(>|t|)    
(Intercept)    100.4165     0.8329 120.569  < 2e-16 ***
fertilisation2   3.1088     0.7474   4.159 0.000589 ***
rotationB        2.7777     1.0712   2.593 0.018370 *  
rotationC        4.9041     1.1684   4.197 0.000542 ***
rotationD        4.3905     1.0051   4.368 0.000371 ***

Residual standard error: 1.738 on 18 degrees of freedom
Multiple R-squared:  0.7276,	Adjusted R-squared:  0.6671 
F-statistic: 12.02 on 4 and 18 DF,  p-value: 6.235e-05



# comparaison 2 à 2 des fertilisations et rotations :

TukeyHSD(aov(rendement ~ fertilisation+rotation))
  Tukey multiple comparisons of means
    95% family-wise confidence level

Fit: aov(formula = rendement ~ fertilisation + rotation)

$fertilisation
        diff      lwr      upr     p adj
2-1 3.553077 2.017043 5.089111 0.0001259

$rotation
          diff        lwr      upr     p adj
B-A  2.6591795 -0.3155748 5.633934 0.0893219
C-A  4.8596923  1.5641899 8.155195 0.0029567
D-A  4.2905577  1.4899192 7.091196 0.0020822
C-B  2.2005128 -0.9705859 5.371612 0.2388997
D-B  1.6313782 -1.0217533 4.284510 0.3341182
D-C -0.5691346 -3.5775030 2.439234 0.9494360


#On compare pvalue_uni = p.adj/2 à 0.05 

#on trouve 
#fertilisation 2> fertilisation 1
#rotation B> rotation A (limite)
#rotation C> rotation A
#rotation D> rotation A
#et les autres rotations ne semblent pas différer entres-elles.
 
# commode : le graphe des intervalles de confiance (meme si ce sont des intervalles bilatères alors qu'on en voudrait des intervalles de confiance unilatéraux)

plot(TukeyHSD(aov(rendement ~ fertilisation+rotation)))













