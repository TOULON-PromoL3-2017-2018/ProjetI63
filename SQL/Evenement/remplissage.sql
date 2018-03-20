--Partie remplissage Université
INSERT INTO Universite VALUES (1, 'La Garde', 'La Garde',
                               'Rue université', '13', 'guigui@mail.com');
INSERT INTO Universite VALUES (2, 'ParisCentre', 'Paris',
                               'Rue Sartre', '5', '0600000000');
INSERT INTO Universite VALUES (3, 'Aix-Marseille', 'Marseille',
                               'Rue Pagnol', '6', '0400000000');

--Partie remplissage ParticipantAsso
INSERT INTO ParticipantAsso VALUES (1, 1);
INSERT INTO ParticipantAsso VALUES (2, 1);
INSERT INTO ParticipantAsso VALUES (3, 1);

--Partie remplissage ParticipantAutre
INSERT INTO ParticipantAutre VALUES (4, 2, 'LEBRON', 'James', 'LJ@etu.com',
                                     '0000000011', '56451045');
INSERT INTO ParticipantAutre VALUES (5, 3, 'CURRY', 'Stephen', 'CS@etu.com',
                                     '0000000120', '78754556');
INSERT INTO ParticipantAutre VALUES (6, 2, 'HARDEN', 'James', 'HJ@etu.com',
                                    '00005000110', '62071014');

--Partie remplissage Presse
INSERT INTO Presse VALUES (1, 'VAR MATIN');
INSERT INTO Presse VALUES (2, 'TF1');
INSERT INTO Presse VALUES (3, 'LE MONDE');

--Partie remplissage Personnel
INSERT INTO Personnel VALUES (1, 'CARMELO', 'Anthony');
INSERT INTO Personnel VALUES (2, 'WALL', 'John');
INSERT INTO Personnel VALUES (3, 'BUTTLER', 'Jimmy');

--Partie remplissage Type
INSERT INTO Type VALUES (1, 'Sport');
INSERT INTO Type VALUES (2, 'Musée');
INSERT INTO Type VALUES (3, 'Bricolage');

--Partie remplissage Sport
INSERT INTO Sport VALUES (1, 'Basket', 'Collectif', 10);
INSERT INTO Sport VALUES (2, 'Tennis', 'Individuel', 2);
INSERT INTO Sport VALUES (3, 'Foot', 'Collectif', 22);

--Partie remplissage EvenementSport
--Probleme vainqueur equipe/joueur à resoudre
INSERT INTO EvenementSport VALUES (1, 1, 4, '');
INSERT INTO EvenementSport VALUES (2, 1, 5);
INSERT INTO EvenementSport VALUES (3, 2, 6);
