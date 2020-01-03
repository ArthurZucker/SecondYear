######################################################################################
## REG SIMPLE
######################################################################################


data=read.csv2("ozone.csv")
> head(data)
  obs maxO3   T9  T12  T15 Ne9 Ne12 Ne15     Vx9    Vx12    Vx15 maxO3v  vent
1 601    87 15.6 18.5 18.4   4    4    8  0.6946 -1.7101 -0.6946     84  Nord
2 602    82 17.0 18.4 17.7   5    5    7 -4.3301 -4.0000 -3.0000     87  Nord
3 603    92 15.3 17.6 19.5   2    5    4  2.9544  1.8794  0.5209     82   Est
4 604   114 16.2 19.7 22.5   1    1    0  0.9848  0.3473 -0.1736     92  Nord
5 605    94 17.4 20.5 20.4   8    8    7 -0.5000 -2.9544 -4.3301    114 Ouest
6 606    80 17.7 19.8 18.3   6    6    7 -5.6382 -5.0000 -6.0000     94 Ouest
  pluie
1   Sec
2   Sec
3   Sec
4   Sec
5   Sec
6 Pluie
> str(data)
'data.frame':	112 obs. of  14 variables:
 $ obs   : int  601 602 603 604 605 606 607 610 611 612 ...
 $ maxO3 : int  87 82 92 114 94 80 79 79 101 106 ...
 $ T9    : num  15.6 17 15.3 16.2 17.4 17.7 16.8 14.9 16.1 18.3 ...
 $ T12   : num  18.5 18.4 17.6 19.7 20.5 19.8 15.6 17.5 19.6 21.9 ...
 $ T15   : num  18.4 17.7 19.5 22.5 20.4 18.3 14.9 18.9 21.4 22.9 ...
 $ Ne9   : int  4 5 2 1 8 6 7 5 2 5 ...
 $ Ne12  : int  4 5 5 1 8 6 8 5 4 6 ...
 $ Ne15  : int  8 7 4 0 7 7 8 4 4 8 ...
 $ Vx9   : num  0.695 -4.33 2.954 0.985 -0.5 ...
 $ Vx12  : num  -1.71 -4 1.879 0.347 -2.954 ...
 $ Vx15  : num  -0.695 -3 0.521 -0.174 -4.33 ...
 $ maxO3v: int  84 87 82 92 114 94 80 99 79 101 ...
 $ vent  : Factor w/ 4 levels "Est","Nord","Ouest",..: 2 2 1 2 3 3 3 2 2 3 ...
 $ pluie : Factor w/ 2 levels "Pluie","Sec": 2 2 2 2 2 1 2 2 2 2 ...
> attach(data)
> names(data)
 [1] "obs"    "maxO3"  "T9"     "T12"    "T15"    "Ne9"    "Ne12"   "Ne15"  
 [9] "Vx9"    "Vx12"   "Vx15"   "maxO3v" "vent"   "pluie" 

plot(T12,maxO3)
res=lm(maxO3~T12, data)
abline(res)


> summary(res)
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) -27.4196     9.0335  -3.035    0.003 ** 
x             5.4687     0.4125  13.258   <2e-16 ***
Residual standard error: 17.57 on 110 degrees of freedom
Multiple R-squared:  0.6151,	Adjusted R-squared:  0.6116 
F-statistic: 175.8 on 1 and 110 DF,  p-value: < 2.2e-16


>   confint(res)
                 2.5 %    97.5 %
(Intercept) -45.321901 -9.517371
x             4.651219  6.286151




ychap19 = -27.4196 +5.4687*19
 
seq.x=seq(10,40, by=0.1)
 
Ipredict=predict(res, newdata=data.frame(T12=seq.x), interval="prediction")
plot(T12, maxO3)
abline(res)
lines(seq.x, Ipredict[,2],col="blue")
lines(seq.x, Ipredict[,3],col="blue")
 
Iconf=predict(res, newdata=data.frame(T12=seq.x), interval="confidence")
lines(seq.x,Iconf[,2],col="green")
lines(seq.x,Iconf[,3],col="green")




