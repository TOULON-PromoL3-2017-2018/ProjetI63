INSERT INTO Etudiant VALUES
(1, 'DIALLO', 'Thierno', '1996-09-12', 'INFO', '0782563131', 'tdiallo@hotmail.fr', '25 avenue de l université', 'La Garde', 83500, '0'),
(2, 'SANCI', 'Enzo', '1995-07-18', 'INFO', '0657429412', 'esanci@free.fr', 'qwertyuiop', 'Computer over the Sea', 83550, '0'),
(3, 'LEMAN', 'Jean-Christophe', '1993-04-27', 'INFO', '0689453251', 'jcleman@wanadoo.fr', '18 rue st catherine', 'Bordeaux', 33100, '0'),
(4, 'COLLOT', 'Kevin', '1994-08-01', 'INFO', '0719654823', 'kcollo@wanadoo.fr', '29 Tiraton', 'Tite Peniche', 83800, '1'),
(5, 'GAITON', 'Cyril', '1995-03-04', 'BIO', '0676362934', 'cgaiton@alice.fr', '404', 'Not Found Sur Yvonne', 13180, '1'),
(6, 'DELALEU', 'Alexandre', '1995-04-24', 'STAPS', '0685483296', 'atobodel174@etud.univ-tln.fr', '8 qzdqzfqef', 'ghkre', 82100, '1'),
(7, 'BOUTEMEUR', 'Kelly', '1997-01-18', 'ECO', '0647329465', 'Kelly-boutemeur@etud.univ-tln.fr', '17 mohqzf', 'qegjsqeiogbedoule', 91000, '1'),
(8, 'NOCITO', 'Marc', '1996-06-09', 'LLCERA', '0789345619', 'marc-nocito@etud.univ-tln.fr', '40 rue du sdf', 'La garde', 83500, '1'),
(9, 'CLAIN', 'Cyril', '1996-03-12', 'COMPTA', '0601241648', 'cyril-clain@etud.univ-tln.fr', '1 rue du bar', 'La Valette', 83210, '1'),
(10, 'RICHARD', 'Xavier', '1992-04-23', 'SOCIO', '0663658624', 'richard-xavier@univ-tln.fr', '95 avenue de valbourdin', 'Toulon', 83200, '1'),
(11, 'CARON', 'Alexandre', '1995-12-24', 'SOCIO', '0422521010', 'caron-alexandre@univ-tln.fr', '17 rue de la serinette', 'Toulon', 83100, '1'),
(12, 'BOULARD', 'Quentin', '1993-11-16', 'EEA', '0751934862', 'boulard-quentin@univ-tln.fr', '86 boulevard du bourebier', 'Menton', 82470, '1'),
(13, 'CALATAYUD', 'Tom', '1993-10-23', 'PC', '0645983281', 'calatayud-tom@univ-tln.fr', '13 rue de mon cul', 'Lyon', 45980, '1'),
(14, 'LERCH', 'Soëlie', '1994-12-25', 'SEGPA', '0481736347', 'lerch-soelie@univ-tln.fr', 'osef', 'osefvraiment', 11111, '1'),
(15, 'PLOW', 'Phil', '1993-04-14', 'MATHS', '0648719642', 'plow-philippe@univ-tln.fr', '154 uqzfjqegh', 'Toulouse', 31000, '1');

INSERT INTO Chef_de_Service VALUES
(1, 6, 1),
(2, 7, 2),
(3, 8, 3),
(4, 9, 4),
(5, 10, 5);

INSERT INTO Sous_Chef_de_Service VALUES
(1, 11, 4),
(2, 12, 3),
(3, 13, 5),
(4, 14, 2),
(5, 15, 1);

INSERT INTO Service VALUES
(1, 'Evenement'),
(2, 'Logement'),
(3, 'Voyage'),
(4, 'Materiel'),
(5, 'Etudiant');

INSERT INTO Subventionneurs VALUES
(1, 'Decathlon', '636 Avenue de Draguignan', 'La Garde', 83130, '0494147950', 'LHERMITE', 'tlhermite@decath.fr'),
(2, 'Go Sport', '1 Rue Murier', 'La Garde', 83000, '0498009730', 'FUNES', 'ldefunes@gosport.fr'),
(3, 'InterSport', '300 avenue de l’Université', 'La Garde', 83160, '0498043980', 'CAUNES', 'adecaunes@isport.fr');

INSERT INTO Financement VALUES
(1, 500, 4, '1'),
(2, 4000, 3 '0'),
(3, 2000, 3, '1'),
(4, 800, 2, '0'),
(5, 40, 2, '1'),
(6, 3000, 1, '0'),
(7, 10000, 5, '0'),
(8, 1000, 1, '1');

INSERT INTO Subvention VALUES
(1, 3000, 1),
(2, 1000, 3),
(3, 2500, 2);

INSERT INTO Contrat VALUES
(1, '1', '2018-04-10', 6),
(2, '1', '2018-04-10', 7),
(3, '1', '2018-04-10', 8),
(4, '1', '2018-04-10', 9),
(5, '1', '2018-04-10', 10),
(6, '1', '2018-04-11', 11),
(7, '1', '2018-04-11', 12),
(8, '1', '2018-04-11', 13),
(9, '1', '2018-04-11', 14),
(10, '1', '2018-04-11', 15);
