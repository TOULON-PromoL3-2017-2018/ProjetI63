CREATE SCHEMA projeti63;
SET search_path to projeti63;
CREATE DOMAIN Filiere AS VARCHAR(6) CHECK (VALUE IN ('INFO', 'EEA', 'BIO', 'PC',
  'MATHS', 'LEA', 'STAPS', 'LLCERA', 'LLCERE', 'COMPTA', 'ECO', 'SOCIO', 'SEGPA',
  'info', 'eea', 'bio', 'pc', 'maths', 'lea', 'staps', 'llcera', 'llcere',
  'compta', 'eco', 'socio', 'segpa'));

CREATE TABLE Etudiant(num_etudiant SERIAL NOT NULL,
                      nom_etudiant VARCHAR(25) NOT NULL,
                      prenom_etudiant VARCHAR(25) NOT NULL,
                      date_naissance_etudiant DATE NOT NULL,
                      filiere_etudiant Filiere NOT NULL,
                      tel_etudiant VARCHAR(12) NOT NULL,
                      mail_etudiant VARCHAR(40) NOT NULL,
                      rue_etudiant VARCHAR(30) NOT NULL,
                      ville_etudiant VARCHAR(25) NOT NULL,
                      code_postal_etudiant INTEGER NOT NULL,
                      membre_asso BOOLEAN NOT NULL,
                      PRIMARY KEY (num_etudiant));

CREATE TABLE Service_asso(num_service SERIAL NOT NULL,
                          nom_service VARCHAR(20) NOT NULL,
                          PRIMARY KEY (num_service));

CREATE TABLE Chef_de_Service(num_chef_de_service SERIAL NOT NULL,
                             num_etudiant INTEGER NOT NULL,
                             num_service INTEGER NOT NULL,
                             PRIMARY KEY (num_chef_de_service),
                             FOREIGN KEY (num_etudiant) REFERENCES Etudiant(num_etudiant),
                             FOREIGN KEY (num_service) REFERENCES Service_asso(num_service));

CREATE TABLE Sous_Chef_de_Service(num_sous_chef_de_service SERIAL NOT NULL,
                                  num_etudiant INTEGER NOT NULL,
                                  num_service INTEGER NOT NULL,
                                  PRIMARY KEY (num_sous_chef_de_service),
                                  FOREIGN KEY (num_etudiant) REFERENCES Etudiant(num_etudiant),
                                  FOREIGN KEY (num_service) REFERENCES Service_asso(num_service));

CREATE TABLE Subventionneurs(num_subventionneur SERIAL NOT NULL,
                             nom_subventionneur VARCHAR(25) NOT NULL,
                             rue_subventionneur VARCHAR(40) NOT NULL,
                             ville_subventionneur VARCHAR(30) NOT NULL,
                             code_postal_subventionneur INTEGER NOT NULL,
                             tel_subventionneur VARCHAR(12) NOT NULL,
                             nom_représentant VARCHAR(20) NOT NULL,
                             mail_représentant VARCHAR(30) NOT NULL,
                             PRIMARY KEY (num_subventionneur));

CREATE TABLE Financement(num_demande_argent SERIAL NOT NULL,
                         montant INTEGER NOT NULL,
                         source INTEGER NOT NULL,
                         validation BOOLEAN NOT NULL DEFAULT '0',
                         traitement BOOLEAN NOT NULL DEFAULT '0',
                         PRIMARY KEY (num_demande_argent),
                         FOREIGN KEY (source) REFERENCES Service_asso(num_service));

CREATE TABLE Subvention(num_subvention SERIAL NOT NULL,
                        montant REAL NOT NULL,
                        num_subventionneur INTEGER NOT NULL,
                        PRIMARY KEY (num_subvention),
                        FOREIGN KEY (num_subventionneur) REFERENCES Subventionneurs(num_subventionneur));

CREATE TABLE Contrat_asso(num_contrat SERIAL NOT NULL,
                          cotisation BOOLEAN NOT NULL,
                          date_signature DATE NOT NULL,
                          num_etudiant INTEGER NOT NULL,
                          PRIMARY KEY (num_contrat),
                          FOREIGN KEY (num_etudiant) REFERENCES Etudiant(num_etudiant));

CREATE TABLE Comptes_membres(num_compte SERIAL NOT NULL,
                             login varchar(30) NOT NULL,
                             mdp varchar(30) NOT NULL,
                             num_etudiant INTEGER NOT NULL,
                             PRIMARY KEY (num_compte),
                             FOREIGN KEY (num_etudiant) REFERENCES Etudiant(num_etudiant));
