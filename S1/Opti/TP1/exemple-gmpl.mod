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
param c{ j in J};

#--- Second membre des contraintes 
param b{j in J};

#--- Coefficients de la matrice des contraintes 
param a{i in I, j in J};

#--- Variables de decision
var x{j in J} >= 0;

#--- Contraintes du probleme
s.t. capacity{i in I}: sum{j in J}a[i,j]*x[j] <= b[i];

#--- Critere a optimiser 
maximize profit: sum{j in J} c[j]*x[j];

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
for{j in J}{
 printf '%5s x(%s) = %.2f',' ', j, x[j];
 printf "\n";  
}

printf "\n"; 
printf "##\n"; 
printf "##########################################";
printf "\n\n"; 

end;	 
