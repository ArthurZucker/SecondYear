PRAGMA foreign_keys = ON;
.mode column
.headers ON
select prenomAut,nomAut from auteur;
select count(*) from auteur;
select urlAuteur from auteur where prenomAut = "Peter" and nomAut ="Buneman";
select adresse from laboratoire where sigle=="LRI";
select titre from annot where email = "peter@cis.upenn.edu";
select titre from aecrit inner join auteur on aecrit.email = auteur.email where auteur.prenomAut = "Susan" and auteur.nomAut ="Davidson";
.print Question 6
select titre,count(*) as nb from aecrit inner join auteur on aecrit.email = auteur.email group by titre having nb>1;
select distinct nomAut from APourNote inner join auteur on APourNote.email = auteur.email where note<3;
.print  nombre de notes par articles
select article.titre,count(*) from article inner join APourNote A on A.titre 
= article.titre group by article.titre;
select nomAut,prenomAut,count(*) from auteur inner join aecrit on aecrit.email = auteur.email group by  nomAut,prenomAut order by count(*);
select article.titre, count(*) as co from article inner join APourNote as A on A.titre =
article.titre group by article.titre having co= 1 ;
select nomAut,prenomAut from auteur where nomAut like 'J%';
select annot.titre
  from annot
  join auteur on annot.email = auteur.email
  where auteur.nomAut = "Jolie" and auteur.prenomAut = "Lucie"
;
select auteur.nomAut,auteur.prenomAut from auteur inner join APourNote on APourNote.email = auteur.email join aecrit on aecrit.email = auteur.email where aecrit.titre = APourNote.titre;
select AVG(A.note)
  from APourNote as A 
  join auteur as au on A.email = au.email
  where au.nomAut = "Segoufin" and au.prenomAut = "Luc";

select A.titre,AVG(A.note)
  from APourNote as A 
  join aecrit as ae on ae.email = A.email and ae.titre = A.titre
  group by A.titre
;

select email,count(*) nb from aecrit
group by email
having nb = 
(select MAX(nb2) from
(select count(*) as nb2 
from aecrit group by email) 
)
;

select distinct count(*) "Nombre d'articles" from article;

select A.email from APourNote as A 
group by A.email
having count(*) = (select distinct count(*) from article);


select (select email from auteur where auteur.nomAut = "Dupont" and auteur.prenomAut = "Christiane"),
titre,5 
from aecrit as A join auteur as B on A.email = B.email where B.nomAut = "Segoufin" and B.prenomAut = "Luc";

.print _________\nAuteurs n''ayant annoté aucun de leur propre articles\n________

select * from auteur where email not in (select distinct apn.email "mail" from APourNote as apn 
join auteur as a on apn.email = a.email 
join aecrit on aecrit.email = a.email and aecrit.titre=apn.titre);

.print _________\nCo auteurs de susanne \n________

select auteur.email from auteur join aecrit on auteur.email = aecrit.email 
where aecrit.titre in (select ae.titre from aecrit as ae join auteur as a on ae.email=a.email 
where a.nomAut = "Davidson" and a.prenomAut ="Susan")
and auteur.nomAut <> "Davidson" and auteur.prenomAut <>"Susan"
;

select article.titre,count(*)  from article 
join aecrit as ae on ae.titre = article.titre group by article.titre;

select article.titre,count(*) cp from article 
join aecrit as ae on ae.titre = article.titre group by article.titre 
order by cp desc limit 1;

select aecrit.email,count(*) cp from aecrit group by aecrit.email order by cp desc;

select aecrit.email,count(*) cp from aecrit 
group by aecrit.email
having cp = (select MAX(cp1) from 
(select aecrit.email,count(*) cp1 from aecrit group by aecrit.email order by cp1 desc
));