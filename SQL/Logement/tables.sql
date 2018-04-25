CREATE TABLE PROPRIETAIRE
(
  num_proprio SERIAL PRIMARY KEY,
  nom_proprio VARCHAR(15) NOT NULL,
  prenom_proprio VARCHAR(15) NOT NULL,
  tel_proprio INTEGER NOT NULL,
  adr_proprio VARCHAR(30) NOT NULL
);

CREATE DOMAIN types AS VARCHAR(15)
CHECK(VALUE IN ('Maison','Studio','Appartement','Loft','duplex'));

CREATE DOMAIN prestations_logement AS VARCHAR(20)
CHECK(VALUE IN('Meublé','Non meublé','Garage','Parking privé'));

CREATE TABLE LOGEMENT
(
  num_logement SERIAL PRIMARY KEY,
  type_logement types NOT NULL,
  surface_logement INTEGER,-- NOT NULL,
  nb_pieces INTEGER NOT NULL,
  localisation VARCHAR(30) NOT NULL,
  prestations prestations_logement,
  montant_caution INTEGER,
  montant_loyer INTEGER,
  num_proprio SERIAL REFERENCES PROPRIETAIRE(num_proprio)

);


CREATE DOMAIN taches AS VARCHAR(20)
CHECK(VALUE IN ('Cuisine','Repassage','Ménage','Jardinage','Courses','Bricolage'));


CREATE TABLE DEMANDEUR
(
  num_etudiant SERIAL PRIMARY KEY,
  budget_etudiant INTEGER,
  taches_preferences taches

);

CREATE TABLE CAUTIONNAIRE
(
  num_cautionnaire SERIAL PRIMARY KEY,
  nom_cautionnaire VARCHAR(15),
  prenom_cautionnaire VARCHAR(15),
  tel_cautionnaire INTEGER,
  adr_cautionnaire VARCHAR(30),
  revenus_cautionnaire INTEGER

);

CREATE TABLE SERVICE_LOGEMENT
(
  num_service SERIAL PRIMARY KEY,
  aides_souhaitees taches

);


CREATE TABLE ASSOCIE
(
  num_service SERIAL REFERENCES SERVICE_LOGEMENT(num_service),
  num_logement SERIAL REFERENCES LOGEMENT(num_logement),
  PRIMARY KEY(num_service,num_logement)
);


CREATE TABLE CONTRAT_LOGEMENT
(
  num_contrat SERIAL PRIMARY KEY,
  date_sign DATE,
  date_emm DATE,
  date_dep_ant DATE,
  date_fin_prevu DATE,
  caution_rendue BOOLEAN,
  renouvellement BOOLEAN,
  contrat_termine BOOLEAN DEFAULT '0',
  num_etudiant SERIAL REFERENCES DEMANDEUR(num_etudiant),
  num_cautionnaire SERIAL REFERENCES CAUTIONNAIRE(num_cautionnaire),
  num_proprio SERIAL REFERENCES PROPRIETAIRE(num_proprio)

);
