#------------------------------------------
#
# (c) Hacene Ouzia, Polytech'Paris UPMC
#
#------------------------------------------
# Exemple de modele avec gmpl
#------------------------------------------

#--- Nombre de variables
param N, integer, > 0;
param M, integer, > 0;

#--- Indices des colonnes
set I := 1..M;

#--- Indices des lignes
set J := 1..N;

#--- Coefficients de la fonc. objectif
param c{i in I, j in J};

#--- Second membre des contraintes
#--- param b{i in I,j in J};

#--- Coefficients de la matrice des contraintes
param a{i in I, j in J};

#--- Variables de decision
var x{i in I,j in J} binary;

#--- Contraintes du probleme
s.t. capacity{i in I}: sum{j in J}x[i,j] = 1;
s.t. capacity2{j in J}: sum{i in I}x[i,j] = 1;

#--- Critere a optimiser
maximize profit: sum{j in J,i in I}c[i,j]*x[i,j];

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
for{i in I, j in J}{
 printf '%5s x(%s,%s) = %.2f',' ', i,j, x[i,j];
 printf "\n";
}

printf "\n";
printf "##\n";
printf "##########################################";
printf "\n\n";

end;
