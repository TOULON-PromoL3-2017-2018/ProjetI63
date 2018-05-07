--Partie remplissage Université
INSERT INTO Universite (NomUniversite, Ville, Rue, Arrondissement, Contact)
                      VALUES ('La Garde', 'La Garde',
                               'Rue universite', '13', 'guigui@mail.com');
INSERT INTO Universite (NomUniversite, Ville, Rue, Arrondissement, Contact)
                      VALUES ('ParisCentre', 'Paris',
                               'Rue Sartre', '5', '0600000000');
INSERT INTO Universite (NomUniversite, Ville, Rue, Arrondissement, Contact)
                      VALUES ('Aix-Marseille', 'Marseille',
                               'Rue Pagnol', '6', '0400000000');

--Partie remplissage ParticipantAsso
INSERT INTO ParticipantAsso VALUES (1, 1);
INSERT INTO ParticipantAsso VALUES (2, 1);
INSERT INTO ParticipantAsso VALUES (3, 1);
INSERT INTO ParticipantAsso VALUES (7, 1);
INSERT INTO ParticipantAsso VALUES (8, 1);


--Partie remplissage ParticipantAutre
INSERT INTO ParticipantAutre VALUES (4, 2, 'LEBRON', 'James', 'LJ@etu.com',
                                     '0000000011', '56451045');
INSERT INTO ParticipantAutre VALUES (5, 3, 'CURRY', 'Stephen', 'CS@etu.com',
                                     '0000000120', '78754556');
INSERT INTO ParticipantAutre VALUES (6, 2, 'HARDEN', 'James', 'HJ@etu.com',
                                    '00005000110', '62071014');
INSERT INTO ParticipantAutre VALUES (9, 2, 'DAVIS', 'Anthony', 'DA@etu.com',
                                    '00040000217', '82024053');
INSERT INTO ParticipantAutre VALUES (10, 3, 'PARKER', 'Tony', 'PT@etu.com',
                                    '00000200054', '12476081');


--Partie remplissage Equipe
INSERT INTO Equipe (NomEquipe) VALUES ('GOLDEN STATE');
INSERT INTO Equipe (NomEquipe) VALUES ('CAVALIERS');

--Partie remplissage Presse
INSERT INTO Presse (Organisme) VALUES ('VAR MATIN');
INSERT INTO Presse (Organisme) VALUES ('TF1');
INSERT INTO Presse (Organisme) VALUES ('LE MONDE');

--Partie remplissage Personnel
INSERT INTO Personnel (NomPersonnel, PrenomPersonnel) VALUES ('CARMELO', 'Anthony');
INSERT INTO Personnel (NomPersonnel, PrenomPersonnel) VALUES ('WALL', 'John');
INSERT INTO Personnel (NomPersonnel, PrenomPersonnel) VALUES ('BUTTLER', 'Jimmy');

--Partie remplissage Type
INSERT INTO Type (TypeEvenement) VALUES ('Sport');
INSERT INTO Type (TypeEvenement) VALUES ('Musee');
INSERT INTO Type (TypeEvenement) VALUES ('Bricolage');

--Partie remplissage Sport
INSERT INTO Sport (NomSport, TypeSport, NbJoueursEquipe) VALUES ('Basket', 'Collectif', 5);
INSERT INTO Sport (NomSport, TypeSport, NbJoueursEquipe) VALUES ('Tennis', 'Individuel', 1);
INSERT INTO Sport (NomSport, TypeSport, NbJoueursEquipe) VALUES ('Foot', 'Collectif', 11);

--Partie remplissage EvenementSport
INSERT INTO EvenementSport (NoSport, NoVainqueur, Score, RecompenseVainqueur, NombreSpectateur)
            VALUES (1, 1, '112 - 94', 20, 1000);
INSERT INTO EvenementSport (NoSport, NoVainqueur, Score, RecompenseVainqueur, NombreSpectateur)
            VALUES (1, 2, '120 - 103', 20, 1500);
INSERT INTO EvenementSport (NoSport, NoVainqueur, Score, RecompenseVainqueur, NombreSpectateur)
            VALUES (1, 2, '125 - 106', 20, 2000);
INSERT INTO EvenementSport (NoSport, NoVainqueur, Score, RecompenseVainqueur, NombreSpectateur)
            VALUES (2, 6, '3 - 2', 30, 500);

--Partie remplissage Evenement
INSERT INTO Evenement (NoPersonnel, NoTypeEvenement, NoPresse, NoEvenementSport,
                       DateEvenement, VilleEvenement, PrixEvenement,
                       PrixPlace, Notation)
                      VALUES (3, 1, 2, 1, '2018/03/30', 'Marseille',
                              4500, 10, 15.4);
INSERT INTO Evenement (NoPersonnel, NoTypeEvenement, NoPresse, NoEvenementSport,
                       DateEvenement, VilleEvenement, PrixEvenement,
                       PrixPlace, Notation)
                      VALUES (2, 1, 2, 2, '2018/03/31', 'Paris',
                              6000, 20, 16.8);
INSERT INTO Evenement (NoPersonnel, NoTypeEvenement, NoPresse, NoEvenementSport,
                       DateEvenement, VilleEvenement, PrixEvenement,
                       PrixPlace, Notation)
                      VALUES (1, 1, 1, 3, '2018/04/06', 'Toulon',
                              1500, 15, 13.2);
INSERT INTO Evenement (NoPersonnel, NoTypeEvenement, NoPresse, NoEvenementSport,
                       DateEvenement, VilleEvenement, PrixEvenement,
                       PrixPlace, Notation)
                      VALUES (2, 2, 3, NULL, '2018/06/15', 'Paris',
                              0, 0, NULL);

--Partie remplissage InscritAsso
INSERT INTO InscritAsso VALUES (3, 3);
INSERT INTO InscritAsso VALUES (1, 4);
INSERT INTO InscritAsso VALUES (2, 4);

--Partie remplissage InscritAutre
INSERT INTO InscritAutre VALUES (10, 3);

--Partie remplissage InscritEquipeAsso
INSERT INTO InscritEquipeAsso VALUES (1, 1);
INSERT INTO InscritEquipeAsso VALUES (2, 1);
INSERT INTO InscritEquipeAsso VALUES (3, 1);
INSERT INTO InscritEquipeAsso VALUES (7, 1);
INSERT INTO InscritEquipeAsso VALUES (8, 1);

--Partie remplissage InscritEquipeAutre
INSERT INTO InscritEquipeAutre VALUES (4, 2);
INSERT INTO InscritEquipeAutre VALUES (5, 2);
INSERT INTO InscritEquipeAutre VALUES (6, 2);
INSERT INTO InscritEquipeAutre VALUES (9, 2);
INSERT INTO InscritEquipeAutre VALUES (10, 2);

--Partie remplissage InscritEquipe
INSERT INTO InscritEquipe VALUES (1, 1);
INSERT INTO InscritEquipe VALUES (2, 1);
INSERT INTO InscritEquipe VALUES (1, 2);
INSERT INTO InscritEquipe VALUES (2, 2);
