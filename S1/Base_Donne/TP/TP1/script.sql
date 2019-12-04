--_______________________________________-----
---- Initialisation
PRAGMA foreign_keys = ON;
.mode column
.headers ON
--_______________________________________-----
---- Contraintes d'insertion
-- Proposition de contrainte d'insertion :
-- INSERT INTO Citerne(Id_caserne,Id_camion,Contenance)
-- VALUES(1,1,-3);   ## Provoque une erreur puisque la Contenance est négative
-- INSERT INTO Camion(Id_caserne,Id_camion,Nb_places,Modele)
-- VALUES (8,1,51,'Laignel_vnr'); ## Ne fontionne pas puisque la caserne 8 n'est pas initialisée
-- INSERT INTO Ville(Nom_ville,Nb_hab,CP) VALUES(300,20000,83240); ## Provoque une erreur puisque le Nom de la ville est un entier
-- DELETE FROM Camion WHERE modele=="truite"; Puisque caserne est réferencée ailleurs
--_______________________________________-----
---- Requetes de selection
.print --1. Donnez la liste de toutes les villes de la base.
select distinct Nom_ville from Adresse;
.print --2. Donnez le prenom et le nom de chaque pompier.
select nom, prenom from Pompier;
.print --3. Quelles sont les casernes qui se situent dans la ville Shadok ?
select * from Caserne as C  where C.Nom_ville== "Shadok";
.print --4. Quelles sont les villes protegees par la caserne 1 ?
select Nom_ville from Protege as C where C.Id_caserne==1;
.print --5. Donnez la liste des villes classees de la plus peuplee a la moins peuplee. (on ne cherchera
.print --   pas a regrouper les populations des villes apparaissant plusieurs fois)
select Nom_ville, Nb_hab from Ville order by Nb_hab desc;
.print --6. Quel est le modele et le nombre de places des citernes ? (Rappel : une citerne est un
.print --	 camion qui a la particularite d'^etre une citerne, et certains camions n'en sont pas).
select Modele, Nb_places from citerne inner join Camion on citerne.Id_camion == Camion.Id_camion and citerne.Id_caserne == Camion.Id_caserne order by Nb_places desc;
.print --7. Quelles sont les adresses des casernes qui protegent "Draguignan" ?
select * from Caserne inner join protege on caserne.Id_caserne == protege.Id_caserne and protege.Nom_ville == "Draguignan";
.print --8. (a) (COUNT) Combien y a-t-il de camions citernes dans la base ?
select count(*) as 'nombre de citernes' from Citerne;
.print --8. (b) (MAX) Quelle est la plus grande contenance de citerne disponible ?
select MAX(Citerne.Contenance) as 'Contenance maximum' from Citerne;
.print --9. Quelle est la contenance moyenne des citernes pour chaque caserne ?
SELECT AVG(citerne.Contenance) FROM citerne GROUP BY citerne.Id_Caserne;
.print --10. Combien de casernes protegent chaque ville ?
select count(*), Nom_ville from protege group by Nom_ville;
.print --11. Quelles sont les casernes qui cumulent des contenances de citerne de plus de 2000 L ?
select citerne.Id_caserne,SUM(Contenance) contenance_totale from citerne group by citerne.Id_caserne having contenance_totale>2000 order by contenance_totale desc;
.print --12. Quels sont les pompiers dont le nom commence par un M ?
select * from pompier where pompier.Nom LIKE 'M%';
.print --_______________________________________-----
.print ---- Suite
.print --1. Quel est le nombre de casernes ?
select count(*) from Caserne;
.print --2. Quels sont les pompiers des casernes situees a Draguignan ?
select pompier.nom,pompier.prenom from pompier inner join Caserne WHERE Caserne.Nom_ville=="Draguignan";
.print --3. Quelles sont les casernes protegeant a la fois Draguignan et Le Luc ?
select * from protege as A , protege as B where A.Id_Caserne==B.Id_Caserne and A.Nom_ville=="Draguignan" and B.Nom_ville=="Le Luc";
.print --4. Quels sont les pompiers de la caserne 3 habitant a plus de 5 kilometres d'une caserne ?
select distinct Nom,Prenom,A.Km from pompier as P inner join caserne on P.Id_Caserne==3 inner join Adresse as A on P.Nom_rue == A.Nom_rue
and P.Num_rue== A.Num_rue and P.Nom_ville == A.Nom_ville and  P.CP == A.CP where A.Km>5;
.print --5. Quels sont les pompiers habitant Le Luc ou des villes >= 20000 habitants ?
select distinct Nom,Prenom,P.Nom_ville,V.Nb_hab from pompier as P inner join Ville as V on  P.Nom_ville == V.Nom_ville and  P.CP == V.CP where V.Nb_hab>20000;
.print --6. Quel est le delai moyen de livraison pour chaque fabricant de citernes de moins de 1000 litres ?
--(attention, comme indique ci-dessus, le champ Delai de la table Fabricant est deja une valeur
--moyenne !)
select F.Delai as "delai moyen de livraison ",F.Nom_fabricant
	from Fabricant as F inner join  Modele as M on F.Nom_fabricant == M.Nom_fabricant
	inner join Camion as Ca on M.Nom_modele == Ca.Modele
	inner join Citerne as Ci on Ca.Id_Camion == Ci.Id_Camion
	where Ci.Contenance<1000 group by F.Nom_fabricant;
.print --7. Classez par ordre decroissant le temps de livraison de camions moyen par caserne. (ici c'est
--le delai moyen par caserne, il faut donc bien calculer une moyenne...)
select AVG(F.Delai),Ca.Id_Caserne
	from Fabricant as F inner join  Modele as M on F.Nom_fabricant == M.Nom_fabricant
	inner join Camion as Ca on M.Nom_modele == Ca.Modele
	group by Ca.Id_Caserne order by AVG(F.Delai) desc;
.print --8. Quel est le nombre de pompiers par caserne ?
select count(*) as "Nombre de pompier",P.Id_Caserne
	from Caserne as Ca inner join Pompier as P on P.Id_Caserne == Ca.Id_Caserne
	group by Ca.Id_caserne;
.print --9. Quelles sont les casernes n'ayant qu'un seul pompier ?
select * from (select count(*) as "Nombre de pompier",P.Id_Caserne
	from Caserne as Ca inner join Pompier as P on P.Id_Caserne == Ca.Id_Caserne
	group by Ca.Id_caserne) where "Nombre de pompier" ==1;
.print --10. Dans quelle(s) ville(s) trouve-t-on la (les) caserne(s) avec la (les) citerne(s) de plus grosse contenance ?
select V.Nom_ville,V.CP from Ville as V inner join
	Caserne as Ca on V.Nom_ville == Ca.Nom_ville and V.CP==Ca.CP
	inner join Citerne on Ca.Id_caserne == Citerne.Id_Caserne where Citerne.contenance == (select MAX(Citerne.Contenance) as 'Contenance maximum' from Citerne);
.print --11. Quelles sont les casernes ayant atteint leur capacite maximale humaine ?
select Tab.Id_Caserne from (select count(*) as "Nombre de pompier",P.Id_Caserne
	from Caserne as Ca inner join Pompier as P on P.Id_Caserne == Ca.Id_Caserne
	group by Ca.Id_caserne) as Tab inner join Caserne as Ca on Tab.Id_Caserne == Ca.Id_caserne where "Nombre de pompier" == Ca.Capa_pompiers;
.print --12. Quels sont les pompiers qui ne travaillent pas dans la ville ou ils habitent ?
select distinct P.Nom,P.prenom,P.Nom_ville from Pompier as P inner join Caserne as Ca on P.Nom_ville != Ca.Nom_ville;
.print --13. Quelles sont les villes qui partagent leur code postal avec une autre ville ? Quelles sont les villes auxquelles plusieurs codes postaux sont attribues ?
select A.Nom_ville,B.Nom_ville from Ville as A inner join Ville as B on A.CP == B.CP and A.Nom_ville != B.Nom_ville and A.Nom_ville>B.Nom_ville;
.print --14. Quelles sont les marques des camions qui sont utilisees dans toutes les casernes ?
select distinct M.Nom_fabricant from Modele as M inner join (select * from (select Count(Camion.Modele) as nb,Camion.Modele from Camion group by Camion.modele) as LL where LL.nb=4) as moCa on  M.Nom_modele = moCa.Modele;
.print --15. Donnez le nombre de chaque type d'habitation pour chaque ville.

select count(*),A.Nom_ville, A.Type_habitation from Adresse as A group by A.Nom_ville,A.Type_habitation;



.print --16. (a) Listez par ordre decroissant les casernes en fonction du nombre des pompiers y travaillant
.print --16. (b) Quelle est la premiere caserne de la liste precedente ?
.print --17. Donnez pour chaque caserne le volume total d'eau de ses citernes (y compris les casernes ne possedant pas de citerne).
