#------------------------------------------
#
# (c) Hacene Ouzia, Polytech'Paris UPMC
#
#------------------------------------------
# Exemple de modele avec gmpl
#------------------------------------------

#--- Nombre de variables
param N, integer, > 0;


#--- Indices des colonnes
set I := 1..N;

#--- Indices des lignes
set J := 1..N;

#--- Coefficients de la fonc. objectif
#--- param c{j in J};

#--- Second membre des contraintes
param b{j in J};

#--- Coefficients de la matrice des contraintes
param a{i in I, j in J};

#--- Second membre des contraintes
param a1{j in J};

#--- Variables de decision
var x{j in J}>=0;
var t >=0;
#--- Contraintes du probleme
s.t. capacity3{i in I}: t >= x[i]-a1[i];
s.t. capacity{i in I}: sum{j in J}a[i,j]*x[j] <= b[i];
s.t. capacity2{i in I}: x[i]-a1[i] <=t;
s.t. capacity4{i in I}: x[i]-a1[i] >=-t;
#--- Critere a optimiser
minimize profit: t;

#--- Commande pour lancer la resolution du probleme ...
solve;

##------------------------------------
## Section pour generer un rapport apres resolution
##-------------------------------------------------

printf '\n\n';
printf '#########################################\n';
printf '##  REPORTING \n';
printf '##\n';

printf "   Optimium objective value : %.2f \n", profit;
printf "   Optimal solution found:\n\n";
for{i in I}{
 printf '%5s x(%s) = %.2f',' ', i, x[i];
 printf "\n";
}

printf "\n";
printf "##\n";
printf "##########################################";
printf "\n\n";

end;
