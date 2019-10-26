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
--1. Donnez la liste de toutes les villes de la base.
select distinct Nom_ville from Adresse;
--2. Donnez le prenom et le nom de chaque pompier.
select nom, prenom from Pompier;
--3. Quelles sont les casernes qui se situent dans la ville Shadok ?
select * from Caserne as C  where C.Nom_ville== "Shadok";
--4. Quelles sont les villes protegees par la caserne 1 ?
select Nom_ville from Protege as C where C.Id_caserne==1;
--5. Donnez la liste des villes classees de la plus peuplee a la moins peuplee. (on ne cherchera
--   pas a regrouper les populations des villes apparaissant plusieurs fois)
select Nom_ville, Nb_hab from Ville order by Nb_hab desc;
--6. Quel est le modele et le nombre de places des citernes ? (Rappel : une citerne est un
--	 camion qui a la particularite d'^etre une citerne, et certains camions n'en sont pas).
select Modele, Nb_places from citerne inner join Camion on citerne.Id_camion == Camion.Id_camion and citerne.Id_caserne == Camion.Id_caserne order by Nb_places desc;
--7. Quelles sont les adresses des casernes qui protegent "Draguignan" ?
select * from Caserne inner join protege on caserne.Id_caserne == protege.Id_caserne and protege.Nom_ville == "Draguignan";
--8. (a) (COUNT) Combien y a-t-il de camions citernes dans la base ?
select count(*) from citerne ;
--8. (b) (MAX) Quelle est la plus grande contenance de citerne disponible ?
SELECT MAX(citerne.Contenance) from citerne ;
--9. Quelle est la contenance moyenne des citernes pour chaque caserne ?
SELECT AVG(citerne.Contenance),Nom_rue,Num_rue,Nom_ville,CP FROM citerne inner join caserne on citerne.Id_Caserne == caserne.Id_Caserne GROUP BY citerne.Id_Caserne;
--10. Combien de casernes protegent chaque ville ?
select count(*), Nom_ville from protege group by Nom_ville;
--11. Quelles sont les casernes qui cumulent des contenances de citerne de plus de 2000 L ?
select citerne.Id_caserne,SUM(Contenance) contenance_totale from citerne group by citerne.Id_caserne having contenance_totale>2000 order by contenance_totale desc;
--12. Quels sont les pompiers dont le nom commence par un M ?
select * from pompier where pompier.Nom LIKE 'M%';
--_______________________________________-----
---- Suite
--1. Quel est le nombre de casernes ?
select count(*) from Caserne;
--2. Quels sont les pompiers des casernes situees a Draguignan ?
select pompier.nom,pompier.prenom from pompier inner join Caserne WHERE Caserne.Nom_ville=="Draguignan";
--3. Quelles sont les casernes protegeant a la fois Draguignan et Le Luc ?
select * from protege as A , protege as B where A.Id_Caserne==B.Id_Caserne and A.Nom_ville=="Draguignan" and B.Nom_ville=="Le Luc";
--4. Quels sont les pompiers de la caserne 3 habitant a plus de 5 kilometres d'une caserne ?
select * from pompier inner join caserne on pompier.Id_Caserne==caserne.Id_Caserne==3 
--5. Quels sont les pompiers habitant Le Luc ou des villes  20000 habitants ?
--6. Quel est le delai moyen de livraison pour chaque fabricant de citernes de moins de 1000 litres ?
--(attention, comme indique ci-dessus, le champ Delai de la table Fabricant est deja une valeur
--moyenne !)
--7. Classez par ordre decroissant le temps de livraison de camions moyen par caserne. (ici c'est
--le delai moyen par caserne, il faut donc bien calculer une moyenne...)
--8. Quel est le nombre de pompiers par caserne ?
--9. Quelles sont les casernes n'ayant qu'un seul pompier ?
--10. Dans quelle(s) ville(s) trouve-t-on la (les) caserne(s) avec la (les) citerne(s) de plus grosse
--contenance ?
--11. Quelles sont les casernes ayant atteint leur capacite maximale humaine ?
--12. Quels sont les pompiers qui ne travaillent pas dans la ville ou ils habitent ?
--13. Quelles sont les villes qui partagent leur code postal avec une autre ville ? Quelles sont les
--villes auxquelles plusieurs codes postaux sont attribues ?
--14. Quelles sont les marques des camions qui sont utilisees dans toutes les casernes ?
--15. Donnez le nombre de chaque type d'habitation pour chaque ville.
--16. (a) Listez par ordre decroissant les casernes en fonction du nombre des pompiers y travaillant
--16. (b) Quelle est la premiere caserne de la liste precedente ?
--17. Donnez pour chaque caserne le volume total d'eau de ses citernes (y compris les casernes ne
--possedant pas de citerne).
