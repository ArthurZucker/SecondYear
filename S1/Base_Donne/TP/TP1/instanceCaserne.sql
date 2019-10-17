/* Remplissage des tables

transaction pour remplir les tables Caserne, Ville, Adresse et Protege.
*/
START TRANSACTION;

/* table Caserne
-- Impossible de donner des informations sur l'adresse des casernes puisque toute adresse a besoin d'avoir
-- des informations sur la caserne la plus proche (reference circulaire).
-- On remplit donc les casernes de facon incomplete puis on complete les casernes une fois les adresses insérées.
*/
 
INSERT INTO Caserne(Id_caserne,Capa_camions,Capa_pompiers,Num_rue,Nom_rue,Nom_ville,CP)
VALUES(1,8,45,NULL,NULL,NULL,NULL);
INSERT INTO Caserne(Id_caserne,Capa_camions,Capa_pompiers,Num_rue,Nom_rue,Nom_ville,CP)
VALUES(2,10,60,NULL,NULL,NULL,NULL);
INSERT INTO Caserne(Id_caserne,Capa_camions,Capa_pompiers,Num_rue,Nom_rue,Nom_ville,CP)
VALUES(3,10,4,NULL,NULL,NULL,NULL);
INSERT INTO Caserne(Id_caserne,Capa_camions,Capa_pompiers,Num_rue,Nom_rue,Nom_ville,CP)
VALUES(4,3,17,NULL,NULL,NULL,NULL);

/*table Ville*/
INSERT INTO Ville(Nom_ville,Nb_hab,CP) VALUES('Draguignan',20000,83240);
INSERT INTO Ville(Nom_ville,Nb_hab,CP) VALUES('Draguignan',300,83242);
INSERT INTO Ville(Nom_ville,Nb_hab,CP) VALUES('Draguignan',2400,83244);
INSERT INTO Ville(Nom_ville,Nb_hab,CP) VALUES('Brignoles',1650,83620);
INSERT INTO Ville(Nom_ville,Nb_hab,CP) VALUES('Le Luc',4580,83620);
INSERT INTO Ville(Nom_ville,Nb_hab,CP) VALUES('Lajoie',25000,83450);
INSERT INTO Ville(Nom_ville,Nb_hab,CP) VALUES('Shadok',14630,83666);
INSERT INTO Ville(Nom_ville,Nb_hab,CP) VALUES('Papou',3655,83220);
INSERT INTO Ville(Nom_ville,Nb_hab,CP) VALUES('Pierrefiques',134,83620);
INSERT INTO Ville(Nom_ville,Nb_hab,CP) VALUES('Montreuil',20400,83100);
INSERT INTO Ville(Nom_ville,Nb_hab,CP) VALUES('Trantown',18500,83220);

/*table Adresse*/
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation,Proche_caserne,Km)
VALUES(23,'Elephant',83240,'Draguignan','HLM',1,1);
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation,Proche_caserne,Km)
VALUES(110,'Mouton',83220,'Papou','Pavillon',2,10);
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation,Proche_caserne,Km)
VALUES(4,'Phoenix',83666,'Shadok','Pavillon',3,25);
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation,Proche_caserne,Km)
VALUES(23,'Lion',83100,'Montreuil','HLM',4,42);
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation,Proche_caserne,Km)
VALUES(6,'Lion',83100,'Montreuil','HLM',4,42);
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation,Proche_caserne,Km)
VALUES(54,'Cuvier',83100,'Montreuil','Pavillon',4,12);
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation,Proche_caserne,Km)
VALUES(36,'Julienne',83220,'Trantown','Pavillon',2,6);
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation,Proche_caserne,Km)
VALUES(18,'Licorne',83240,'Draguignan','Pavillon',2,6);
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation,Proche_caserne,Km)
VALUES(50,'Dragon',83220,'Papou','HLM',1,4);
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation,Proche_caserne,Km)
VALUES(9,'Baleine',83666,'Shadok','Pavillon',3,6);
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation,Proche_caserne,Km)
VALUES(14,'Stupide',83620,'Le Luc','Pavillon',2,9);
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation,Proche_caserne,Km)
VALUES(9,'Baleine',83620,'Le Luc','Pavillon',1,10);
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation)
VALUES(36,'Canard',83240,'Draguignan','Caserne');
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation)
VALUES(136,'Pigeon',83242,'Draguignan','Caserne');
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation)
VALUES(48,'Alouette',83666,'Shadok','Caserne');
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation)
VALUES(1,'Chouette',83666,'Shadok','Caserne');
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation)
VALUES(54,'Hiboux',83620,'Le Luc','Caserne');
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation)
VALUES(23,'Corbeau',83100,'Montreuil','Caserne');
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation)
VALUES(2,'Aigle',83244,'Draguignan','Caserne');
INSERT INTO Adresse(Num_rue,Nom_rue,CP,Nom_ville,Type_habitation)
VALUES(36,'Canard',83620,'Le Luc','Caserne');

/* mettre a jour les valeurs de casernes qui sont NULL*/
UPDATE Caserne SET Num_rue=36,Nom_rue='Canard',Nom_ville='Le Luc', CP=83620 WHERE Id_caserne=1;

UPDATE Caserne SET Num_rue=136,Nom_rue='Pigeon',Nom_ville='Draguignan',CP=83242 WHERE Id_caserne=2;

UPDATE Caserne SET Num_rue=48,Nom_rue='Alouette',Nom_ville='Shadok',CP=83666 WHERE Id_caserne=3;

UPDATE Caserne SET Num_rue=1,Nom_rue='Chouette',Nom_ville='Shadok',CP=83666 WHERE Id_caserne=4;

/*table Protege*/
INSERT INTO Protege(Id_caserne,Nom_ville,CP) VALUES(1,'Draguignan',83240);
INSERT INTO Protege(Id_caserne,Nom_ville,CP) VALUES(1,'Brignoles',83620);
INSERT INTO Protege(Id_caserne,Nom_ville,CP) VALUES(1,'Le Luc',83620);
INSERT INTO Protege(Id_caserne,Nom_ville,CP) VALUES(4,'Le Luc',83620);
INSERT INTO Protege(Id_caserne,Nom_ville,CP) VALUES(2,'Papou',83220);
INSERT INTO Protege(Id_caserne,Nom_ville,CP) VALUES(2,'Draguignan',83240);
INSERT INTO Protege(Id_caserne,Nom_ville,CP) VALUES(3,'Shadok',83666);
INSERT INTO Protege(Id_caserne,Nom_ville,CP) VALUES(3,'Draguignan',83240);
INSERT INTO Protege(Id_caserne,Nom_ville,CP) VALUES(4,'Brignoles',83620);
INSERT INTO Protege(Id_caserne,Nom_ville,CP) VALUES(4,'Draguignan',83240);

COMMIT; /* on insère ces données */
/*END TRANSACTION; fin de transaction*/

/*transaction pour remplir les tables Fabricant, Modele, Pompier, Camion et Citerne*/
START TRANSACTION;

/*table Fabricant*/
INSERT INTO Fabricant(Nom_fabricant,Delai,Num_rue,Nom_rue,CP,Nom_ville) 
VALUES('Peugeot',999,54,'Cuvier',83100,'Montreuil');
INSERT INTO Fabricant(Nom_fabricant,Delai,Num_rue,Nom_rue,CP,Nom_ville) 
VALUES('Mercedes_benz',666,36,'Julienne',83220,'Trantown');

/*table Modele*/
INSERT INTO Modele(Nom_modele,Type_modele,Motorisation,Nom_fabricant)
VALUES ('Daminator','K2000','Top','Peugeot');
INSERT INTO Modele(Nom_modele,Type_modele,Motorisation,Nom_fabricant)
VALUES ('Laignel_vnr','N800','Tip','Mercedes_benz');
INSERT INTO Modele(Nom_modele,Type_modele,Motorisation,Nom_fabricant)
VALUES ('Truite','ARN','Tip','Mercedes_benz');
INSERT INTO Modele(Nom_modele,Type_modele,Motorisation,Nom_fabricant)
VALUES ('GrosColosse','SPQR','Tiptop','Peugeot');

/*table Pompier*/
INSERT INTO Pompier(Id_caserne,Id_pompier,Nom,Prenom,Nom_rue,Num_rue,Nom_ville,CP)
VALUES (1,1,'Marchand','Louis','Licorne',18,'Draguignan',83240);
INSERT INTO Pompier(Id_caserne,Id_pompier,Nom,Prenom,Nom_rue,Num_rue,Nom_ville,CP)
VALUES (2,1,'Valjean','Jean','Dragon',50,'Papou',83220);
INSERT INTO Pompier(Id_caserne,Id_pompier,Nom,Prenom,Nom_rue,Num_rue,Nom_ville,CP)
VALUES (4,1,'Antoinette','Marie','Lion',6,'Montreuil',83100);
INSERT INTO Pompier(Id_caserne,Id_pompier,Nom,Prenom,Nom_rue,Num_rue,Nom_ville,CP)
VALUES (3,1,'Montant','Yves','Baleine',9,'Shadok',83666);
INSERT INTO Pompier(Id_caserne,Id_pompier,Nom,Prenom,Nom_rue,Num_rue,Nom_ville,CP)
VALUES (3,2,'Montant','Sylvain','Dragon',50,'Papou',83220);
INSERT INTO Pompier(Id_caserne,Id_pompier,Nom,Prenom,Nom_rue,Num_rue,Nom_ville,CP)
VALUES (3,3,'Savairien','Jean','Dragon',50,'Papou',83220);
INSERT INTO Pompier(Id_caserne,Id_pompier,Nom,Prenom,Nom_rue,Num_rue,Nom_ville,CP)
VALUES (2,2,'Conchon','Sylvain','Stupide',14,'Le Luc',83620);
INSERT INTO Pompier(Id_caserne,Id_pompier,Nom,Prenom,Nom_rue,Num_rue,Nom_ville,CP)
VALUES (3,4,'Jumper','Jolly','Baleine',9,'Le Luc',83620);

/*table Camion*/
INSERT INTO Camion(Id_caserne,Id_camion,Nb_places,Modele)
VALUES (1,1,38,'Daminator');
INSERT INTO Camion(Id_caserne,Id_camion,Nb_places,Modele)
VALUES (1,2,52,'Laignel_vnr');
INSERT INTO Camion(Id_caserne,Id_camion,Nb_places,Modele)
VALUES (1,3,152,'Truite');
INSERT INTO Camion(Id_caserne,Id_camion,Nb_places,Modele)
VALUES (1,4,72,'GrosColosse');
INSERT INTO Camion(Id_caserne,Id_camion,Nb_places,Modele)
VALUES (2,1,95,'Laignel_vnr');
INSERT INTO Camion(Id_caserne,Id_camion,Nb_places,Modele)
VALUES (2,2,87,'Truite');
INSERT INTO Camion(Id_caserne,Id_camion,Nb_places,Modele)
VALUES (2,3,39,'Laignel_vnr');
INSERT INTO Camion(Id_caserne,Id_camion,Nb_places,Modele)
VALUES (2,4,95,'GrosColosse');
INSERT INTO Camion(Id_caserne,Id_camion,Nb_places,Modele)
VALUES (3,1,55,'Daminator');
INSERT INTO Camion(Id_caserne,Id_camion,Nb_places,Modele)
VALUES (3,2,35,'Truite');
INSERT INTO Camion(Id_caserne,Id_camion,Nb_places,Modele)
VALUES (3,3,58,'Daminator');
INSERT INTO Camion(Id_caserne,Id_camion,Nb_places,Modele)
VALUES (4,1,51,'Laignel_vnr');

/*table Citerne*/
INSERT INTO Citerne(Id_caserne,Id_camion,Contenance)
VALUES(1,1,800);
INSERT INTO Citerne(Id_caserne,Id_camion,Contenance)
VALUES(1,2,600);
INSERT INTO Citerne(Id_caserne,Id_camion,Contenance)
VALUES(1,3,900);
INSERT INTO Citerne(Id_caserne,Id_camion,Contenance)
VALUES(2,1,2000);
INSERT INTO Citerne(Id_caserne,Id_camion,Contenance)
VALUES(2,2,500);
INSERT INTO Citerne(Id_caserne,Id_camion,Contenance)
VALUES(2,4,450);
INSERT INTO Citerne(Id_caserne,Id_camion,Contenance)
VALUES(3,1,1200);

COMMIT; /*on insère ces données*/
/*END TRANSACTION; fin de transaction*/
