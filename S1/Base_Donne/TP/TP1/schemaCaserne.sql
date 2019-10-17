DROP TABLE IF EXISTS Caserne;
DROP TABLE IF EXISTS Ville;
DROP TABLE IF EXISTS Adresse;
DROP TABLE IF EXISTS Protege;
DROP TABLE IF EXISTS Fabricant;
DROP TABLE IF EXISTS Modele;
DROP TABLE IF EXISTS Pompier;
DROP TABLE IF EXISTS Camion;
DROP TABLE IF EXISTS Citerne;

CREATE TABLE Caserne(
Id_caserne INTEGER,
Capa_camions INTEGER,
Capa_pompiers INTEGER ,
Num_rue  INTEGER ,
Nom_rue  VARCHAR(20) ,
CP   INTEGER ,
Nom_ville  VARCHAR(20) ,

PRIMARY KEY(Id_caserne),
FOREIGN KEY(Nom_rue,Num_rue,Nom_ville,CP) REFERENCES Adresse(Nom_rue,Num_rue,Nom_ville,CP)
);


CREATE TABLE Ville(
Nom_ville  VARCHAR(20) ,
Nb_hab  INTEGER ,
CP   INTEGER ,

PRIMARY KEY(Nom_ville,CP));


CREATE TABLE Adresse(
Num_rue  INTEGER ,
Nom_rue  VARCHAR(20) ,
CP   INTEGER ,
Nom_ville  VARCHAR(20) ,
Type_habitation VARCHAR(20) ,
Proche_caserne INTEGER ,
Km   INTEGER ,

PRIMARY KEY(Nom_rue,Num_rue,Nom_ville,CP),
FOREIGN KEY(Nom_ville,CP) REFERENCES Ville(Nom_ville,CP),
FOREIGN KEY(Proche_caserne) REFERENCES Caserne(Id_caserne)
);


CREATE TABLE Protege(
Id_caserne  INTEGER ,
Nom_ville  VARCHAR(20) ,
CP   INTEGER ,

PRIMARY KEY(Id_caserne,Nom_ville,CP),
FOREIGN KEY(Nom_ville,CP) REFERENCES Ville(Nom_ville,CP),
FOREIGN KEY(Id_caserne) REFERENCES Caserne(Id_caserne)
);
 
CREATE TABLE Fabricant(
Nom_fabricant VARCHAR(20) ,
Delai  INTEGER ,
Num_rue  INTEGER ,
Nom_rue  VARCHAR(20) ,
CP   INTEGER ,
Nom_ville  VARCHAR(20) ,

PRIMARY KEY(Nom_fabricant),
FOREIGN KEY (Nom_rue,Num_rue,Nom_ville,CP) REFERENCES Adresse (Nom_rue, Num_rue, Nom_ville, CP)
);


CREATE TABLE Modele(
Nom_modele  VARCHAR(20) ,         
Type_modele  VARCHAR(20) ,
Motorisation VARCHAR(20) ,
Nom_fabricant VARCHAR(20) ,

PRIMARY KEY(Nom_modele),
FOREIGN KEY(Nom_fabricant) REFERENCES Fabricant(Nom_fabricant));


CREATE TABLE Pompier(
Id_caserne INTEGER ,
Id_pompier INTEGER ,
Nom  VARCHAR(20) ,
Prenom  VARCHAR(20) ,
Nom_rue  VARCHAR(20) ,
Num_rue  INTEGER ,
Nom_ville VARCHAR(20) ,
CP  INTEGER ,

PRIMARY KEY(Id_caserne,Id_pompier),
FOREIGN KEY(Id_caserne) REFERENCES Caserne(Id_caserne),
FOREIGN KEY(Nom_rue,Num_rue,NOM_ville,CP) REFERENCES Adresse(Nom_rue,Num_rue,Nom_ville,CP));


CREATE TABLE Camion(
Id_caserne INTEGER ,
Id_camion INTEGER ,
Nb_places INTEGER ,
Modele  VARCHAR(20) ,

PRIMARY KEY(Id_caserne,Id_camion),
FOREIGN KEY(Id_caserne) REFERENCES Caserne(Id_caserne),
FOREIGN KEY(Modele) REFERENCES Modele(Nom_modele));


CREATE TABLE Citerne(
Id_caserne INTEGER ,
Id_camion INTEGER ,
Contenance INTEGER ,

PRIMARY KEY(Id_caserne,Id_camion),
FOREIGN KEY(Id_caserne,Id_camion) REFERENCES Camion(Id_caserne,Id_camion),
CHECK (Contenance > 0 AND Contenance < 100000)
);
