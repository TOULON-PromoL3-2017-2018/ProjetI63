CREATE TABLE PROPRIETAIRE
(
  num_proprio INTEGER PRIMARY KEY,
  nom_proprio VARCHAR(15) NOT NULL,
  prenom_proprio VARCHAR(15) NOT NULL,
  tel_proprio INTEGER NOT NULL,
  adr_proprio VARCHAR(30) NOT NULL

);

CREATE TABLE LOGEMENT
(
  num_logement INTEGER PRIMARY KEY,
  type_logement VARCHAR(15) NOT NULL,
  surface_logement INTEGER NOT NULL,
  nb_pieces INTEGER NOT NULL,
  localisation VARCHAR(30) NOT NULL,
  prestations VARCHAR(20),
  montant_caution INTEGER,
  montant_loyer INTEGER,
  num_proprio INTEGER REFERENCES PROPRIETAIRE(num_proprio)

);

CREATE TABLE DEMANDEUR
(
  num_etudiant INTEGER PRIMARY KEY,
  budget_etudiant INTEGER,
  taches_preferences VARCHAR(20)

);

CREATE TABLE CAUTIONNAIRE
(
  num_cautionnaire INTEGER PRIMARY KEY,
  nom_cautionnaire VARCHAR(15),
  prenom_cautionnaire VARCHAR(15),
  tel_cautionnaire INTEGER,
  adr_cautionnaire VARCHAR(30),
  revenus_cautionnaire INTEGER

);

CREATE TABLE SERVICE
(
  num_service INTEGER PRIMARY KEY,
  aides_souhaitees VARCHAR(20)

);


CREATE TABLE ASSOCIE
(
  num_service INTEGER REFERENCES SERVICE(num_service),
  num_logement INTEGER REFERENCES LOGEMENT(num_logement),
  PRIMARY KEY(num_service,num_logement)
);


CREATE TABLE CONTRAT
(
  num_contrat INTEGER PRIMARY KEY,
  date_sign DATE,
  date_emm DATE,
  date_dep_ant DATE,
  date_fin_prevu DATE,
  caution_rendue BOOLEAN,
  renouvellement BOOLEAN,
  num_etudiant INTEGER REFERENCES DEMANDEUR(num_etudiant),
  num_cautionnaire INTEGER REFERENCES CAUTIONNAIRE(num_cautionnaire),
  num_proprio INTEGER REFERENCES PROPRIETAIRE(num_proprio)

);
