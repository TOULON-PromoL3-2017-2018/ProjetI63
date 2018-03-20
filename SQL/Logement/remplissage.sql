INSERT INTO PROPRIETAIRE VALUES(0,'Jean','Jacques',0612121212,'impasse des cotons');
INSERT INTO PROPRIETAIRE VALUES(1,'Marie','Anne',0651515151,'rue des guimauves');
INSERT INTO PROPRIETAIRE VALUES(2,'Dupont','Giles',0641414141,'impasse des chocolats');
INSERT INTO PROPRIETAIRE VALUES(3,'Tintin','Jules',0632323232,'rue de la tisane');
INSERT INTO PROPRIETAIRE VALUES(4,'Pat','Tom',0698989898,'rue des oliviers');

INSERT INTO LOGEMENT VALUES(1212,'Maison',98,4,'Rue de la tarte au fraises','meublé',1200,1200,0);
INSERT INTO LOGEMENT VALUES(1414,'T2',45,2,'Rue de la crêperie','non meublé',500,500,1);
INSERT INTO LOGEMENT VALUES(1515,'Studio',30,2,'Avenue des cerisiers','rdc',400,400,2);
INSERT INTO LOGEMENT VALUES(1616,'Maison',80,3,'impasse des citrons',NULL,1000,1000,3);
INSERT INTO LOGEMENT VALUES(1111,'T3',70,3,'Rue de la vanille',NULL,900,900,4);

INSERT INTO DEMANDEUR VALUES(1212,1200,NULL);
INSERT INTO DEMANDEUR VALUES(1213,800,NULL);
INSERT INTO DEMANDEUR VALUES(1214,500,'repassage');
INSERT INTO DEMANDEUR VALUES(1215,700,'cuisine');
INSERT INTO DEMANDEUR VALUES(1216,1000,'repassage');

INSERT INTO CAUTIONNAIRE VALUES(5454,'Bourbon','Didier',0614141414,'chemin des pivoines',1600);
INSERT INTO CAUTIONNAIRE VALUES(3454,'Abeille','Maya',0616161616,'rue des champignons',1900);
INSERT INTO CAUTIONNAIRE VALUES(2454,'Chocolat','Charly',0678787878,'avenue des kiwis',2100);
INSERT INTO CAUTIONNAIRE VALUES(1454,'Mouse','Mickey',0656565656,'chemin des guimauves',1500);
INSERT INTO CAUTIONNAIRE VALUES(454,'Duck','Donald',0621212121,'rue des papayes',1480);

INSERT INTO SERVICE VALUES(7894,'repassage');
INSERT INTO SERVICE VALUES(5894,'jardinage');
INSERT INTO SERVICE VALUES(6894,'cuisine');
INSERT INTO SERVICE VALUES(4894,'ménage');
INSERT INTO SERVICE VALUES(3894,'ménage');

INSERT INTO ASSOCIE VALUES(7894,1212);
INSERT INTO ASSOCIE VALUES(5894,1414);
INSERT INTO ASSOCIE VALUES(6894,1515);
INSERT INTO ASSOCIE VALUES(4894,1616);
INSERT INTO ASSOCIE VALUES(3894,1111);

INSERT INTO CONTRAT VALUES(14141,'2018/01/12','2018/12/12',548,'0',1212,5454,0);
INSERT INTO CONTRAT VALUES(14142,'2017/12/10','2018/01/11',30,'1',1213,3454,1);
INSERT INTO CONTRAT VALUES(14143,'2018/01/11','2018/04/13',550,'0',1214,2454,2);
INSERT INTO CONTRAT VALUES(14144,'2018/01/04','2018/05/14',555,'0',1215,1454,3);
INSERT INTO CONTRAT VALUES(14145,'2018/01/08','2018/06/15',557,'0',1216,454,4);
