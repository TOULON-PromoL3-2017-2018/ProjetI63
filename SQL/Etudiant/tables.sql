CREATE TABLE Etudiant(num_etudiant INTEGER NOT NULL,
                      nom_etudiant VARCHAR(20) NOT NULL, 
                      prenom_etudiant VARCHAR(20) NOT NULL, 
                      date_naissance_etudiant DATE NOT NULL, 
                      filiere_etudiant VARCHAR(20) NOT NULL, 
                      tel_etudiant VARCHAR(12) NOT NULL, 
                      mail_etudiant VARCHAR(30) NOT NULL, 
                      rue_etudiant VARCHAR(30) NOT NULL, 
                      ville_etudiant VARCHAR(20) NOT NULL, 
                      code_postal_etudiant INTEGER NOT NULL, 
                      membre_asso BOOLEAN NOT NULL, 
                      PRIMARY KEY (num_etudiant));
                      
CREATE TABLE Chef_de_Service(num_chef_de_service INTEGER NOT NULL, 
                             num_etudiant INTEGER NOT NULL, 
                             PRIMARY KEY (num_chef_de_service), 
                             FOREIGN KEY (num_etudiant) REFERENCES Etudiant(num_etudiant));
                             
CREATE TABLE Sous_Chef_de_Service(num_sous_chef_de_service INTEGER NOT NULL, 
                                  num_etudiant INTEGER NOT NULL, 
                                  PRIMARY KEY (num_sous_chef_de_service), 
                                  FOREIGN KEY (num_etudiant) REFERENCES Etudiant(num_etudiant));
                                  
CREATE TABLE Service(num_service INTEGER NOT NULL, 
                     nom_service VARCHAR(20) NOT NULL, 
                     num_responsable_service INTEGER NOT NULL, 
                     PRIMARY KEY (num_service), 
                     FOREIGN KEY (num_responsable_service) REFERENCES Chef_de_Service(num_chef_de_service));
                     
CREATE TABLE Subventionneurs(num_subventionneur INTEGER NOT NULL, 
                             nom_subventionneur VARCHAR(20) NOT NULL, 
                             prenom_subventionneur VARCHAR(20) NOT NULL, 
                             rue_subventionneur VARCHAR(20) NOT NULL, 
                             ville_subventionneur VARCHAR(20) NOT NULL, 
                             code_postal_subventionneur INTEGER NOT NULL, 
                             tel_subventionneur VARCHAR(12) NOT NULL, 
                             nom_représentant VARCHAR(20) NOT NULL, 
                             mail_représentant VARCHAR(30) NOT NULL, 
                             PRIMARY KEY(num_subventionneur));
                             
CREATE TABLE Financement(num_demande_argent INTEGER NOT NULL, 
                         montant INTEGER NOT NULL, 
                         source INTEGER NOT NULL, 
                         validation BOOLEAN NOT NULL, 
                         PRIMARY KEY(num_demande_argent), 
                         FOREIGN KEY(source) REFERENCES Service(num_service));
                         
CREATE TABLE Subvention(num_subvention INTEGER NOT NULL, 
                        montant REAL NOT NULL, 
                        PRIMARY KEY(num_subvention));
                        
CREATE TABLE Contrat(num_contrat INTEGER NOT NULL, 
                     cotisation BOOLEAN NOT NULL, 
                     date_signature DATE NOT NULL, 
                     PRIMARY KEY(num_contrat));
