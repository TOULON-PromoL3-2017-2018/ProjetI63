INSERT INTO PROPRIETAIRE(nom_proprio,prenom_proprio,tel_proprio,adr_proprio) VALUES('Jean','Jacques',0612121212,'impasse des cotons');
INSERT INTO PROPRIETAIRE(nom_proprio,prenom_proprio,tel_proprio,adr_proprio) VALUES('Marie','Anne',0651515151,'rue des guimauves');
INSERT INTO PROPRIETAIRE(nom_proprio,prenom_proprio,tel_proprio,adr_proprio) VALUES('Dupont','Giles',0641414141,'impasse des chocolats');
INSERT INTO PROPRIETAIRE(nom_proprio,prenom_proprio,tel_proprio,adr_proprio) VALUES('Tintin','Jules',0632323232,'rue de la tisane');
INSERT INTO PROPRIETAIRE(nom_proprio,prenom_proprio,tel_proprio,adr_proprio) VALUES('Pat','Tom',0698989898,'rue des oliviers');

INSERT INTO LOGEMENT(type_logement,surface_logement,nb_pieces,localisation,prestations,montant_caution,montant_loyer)  VALUES('Maison',98,4,'Rue de la tarte au fraises','Meublé',1200,1200);
INSERT INTO LOGEMENT(type_logement,surface_logement,nb_pieces,localisation,prestations,montant_caution,montant_loyer) VALUES('Appartement',45,2,'Rue de la crêperie','Non meublé',500,500);
INSERT INTO LOGEMENT(type_logement,surface_logement,nb_pieces,localisation,prestations,montant_caution,montant_loyer) VALUES('Studio',30,2,'Avenue des cerisiers','Parking privé',400,400);
INSERT INTO LOGEMENT(type_logement,surface_logement,nb_pieces,localisation,prestations,montant_caution,montant_loyer) VALUES('Maison',80,3,'impasse des citrons',NULL,1000,1000);
INSERT INTO LOGEMENT(type_logement,surface_logement,nb_pieces,localisation,prestations,montant_caution,montant_loyer) VALUES('Appartement',70,3,'Rue de la vanille',NULL,900,900);

INSERT INTO DEMANDEUR(budget_etudiant,taches_preferences) VALUES(1200,NULL);
INSERT INTO DEMANDEUR(budget_etudiant,taches_preferences) VALUES(800,NULL);
INSERT INTO DEMANDEUR(budget_etudiant,taches_preferences) VALUES(500,'Repassage');
INSERT INTO DEMANDEUR(budget_etudiant,taches_preferences) VALUES(700,'Cuisine');
INSERT INTO DEMANDEUR(budget_etudiant,taches_preferences) VALUES(1000,'Ménage');

INSERT INTO CAUTIONNAIRE(nom_cautionnaire,prenom_cautionnaire,tel_cautionnaire,adr_cautionnaire,revenus_cautionnaire) VALUES('Bourbon','Didier',0614141414,'chemin des pivoines',1600);
INSERT INTO CAUTIONNAIRE(nom_cautionnaire,prenom_cautionnaire,tel_cautionnaire,adr_cautionnaire,revenus_cautionnaire) VALUES('Abeille','Maya',0616161616,'rue des champignons',1900);
INSERT INTO CAUTIONNAIRE(nom_cautionnaire,prenom_cautionnaire,tel_cautionnaire,adr_cautionnaire,revenus_cautionnaire) VALUES('Chocolat','Charly',0678787878,'avenue des kiwis',2100);
INSERT INTO CAUTIONNAIRE(nom_cautionnaire,prenom_cautionnaire,tel_cautionnaire,adr_cautionnaire,revenus_cautionnaire) VALUES('Mouse','Mickey',0656565656,'chemin des guimauves',1500);
INSERT INTO CAUTIONNAIRE(nom_cautionnaire,prenom_cautionnaire,tel_cautionnaire,adr_cautionnaire,revenus_cautionnaire) VALUES('Duck','Donald',0621212121,'rue des papayes',1480);

INSERT INTO SERVICE_LOGEMENT(aides_souhaitees) VALUES('Repassage');
INSERT INTO SERVICE_LOGEMENT(aides_souhaitees) VALUES('Jardinage');
INSERT INTO SERVICE_LOGEMENT(aides_souhaitees) VALUES('Cuisine');
INSERT INTO SERVICE_LOGEMENT(aides_souhaitees) VALUES('Ménage');
INSERT INTO SERVICE_LOGEMENT(aides_souhaitees) VALUES('Ménage');



INSERT INTO CONTRAT(date_emm,date_dep_ant,date_fin_prevu,caution_rendue,renouvellement) VALUES('2018/02/12',NULL,'2018/04/07','0','0');
INSERT INTO CONTRAT(date_emm,date_dep_ant,date_fin_prevu,caution_rendue,renouvellement) VALUES('2018/11/11','2018/12/05','2018/12/08','1','0');
INSERT INTO CONTRAT(date_emm,date_dep_ant,date_fin_prevu,caution_rendue,renouvellement) VALUES('2018/04/19',NULL,'2018/05/16','0','0');
INSERT INTO CONTRAT(date_emm,date_dep_ant,date_fin_prevu,caution_rendue,renouvellement) VALUES('2018/05/14',NULL,'2018/07/15','0','0');
INSERT INTO CONTRAT(date_emm,date_dep_ant,date_fin_prevu,caution_rendue,renouvellement) VALUES('2018/06/15',NULL,'2018/08/15','0','0');
