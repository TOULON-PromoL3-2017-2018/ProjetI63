INSERT INTO Type_Materiel VALUES
('hiver',1, 120),
('montagne',2, 100),
('route',3, 80),
('eau',4, 30),
('plein air',5, 60);


INSERT INTO Etudiant VALUES
(DEFAULT,'DIALLO', 'Thierno', '1996-09-12', 'INFO', '0782563131', 'tdiallo@hotmail.fr', '25 avenue de l université', 'La Garde', 83500, '0'),
(DEFAULT, 'SANCI', 'Enzo', '1995-07-18', 'INFO', '0657429412', 'esanci@free.fr', 'qwertyuiop', 'Computer over the Sea', 83550, '0'),
(DEFAULT, 'LEMAN', 'Jean-Christophe', '1993-04-27', 'INFO', '0689453251', 'jcleman@wanadoo.fr', '18 rue st catherine', 'Bordeaux', 33100, '0');



INSERT INTO Materiel_stock VALUES
(1,'chaussure de ski',1, 'TB', 30),
(2,'baton de ski',1, 'TB', 30),
(3,'combi de ski',1, 'TB', 30),
(4,'ski',1, 'TB', 30);



INSERT INTO Entreprise VALUES
(1,'DECAT','32 rue de azrea','la garde','henri','henri@henri.mail'),
(2,'go sport' ,'32 rue de zretzert','la garde','henri','marc@marc.mail'),
(3,'INTER SPORT','32 rue dezertzert','la garde','henri','titouan@titouan.mail');

INSERT INTO Forfait VALUES
(1,40),
(2,30),
(3,60),
(4,80);

INSERT INTO Caution VALUES
(1,30,1,1),
(2,30,2,1),
(3,30,3,4),
(4,30,3,2);

INSERT INTO Location VALUES
(1,5,'2018-03-04',1),
(2,5,'2018-03-04',2),
(3,5,'2018-03-04',3),
(4,5,'2018-03-04',3);

INSERT INTO Facture VALUES
(1,'2017-02-01',60,1),
(2,'2017-02-17',120,2),
(3,'2017-02-23',80,2);

INSERT INTO Devis VALUES
(1,65,'2017-01-17',1),
(2,120,'2017-01-29',2),
(3,70,'2017-02-15',2);

INSERT INTO Materiel_Entreprise VALUES
(1,1,120);

INSERT INTO ParticipantAsso VALUES
(1,1),
(2,2),
(3,3);

INSERT INTO Evenement VALUES
(1);

INSERT INTO matériel_retour VALUES
(1,1,'TB'),
(2,2,'B'),
(3,3,'B'),
(4,4,'AB');

INSERT INTO Caution_encaisser VALUES
(1,'T',1),
(1,'T',2),
(2,'T',3),
(3,'T',3);
