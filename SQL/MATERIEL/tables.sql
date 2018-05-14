-- clain cyril

--creation d'un domaine BOOL :
create domain BOOL
as char
check(value in('T','F'));

--creation d'un domaine ETAT :
create domain ETAT
as varchar(3)
check(value in('AB','B','TB'));

--creation d'un domaine Filiere (xavier l'a écris ):
CREATE DOMAIN Filiere AS VARCHAR(6) CHECK (VALUE IN ('INFO', 'EEA', 'BIO', 'PC',
  'MATHS', 'LEA', 'STAPS', 'LLCERA', 'LLCERE', 'COMPTA', 'ECO', 'SOCIO', 'SEGPA',
  'info', 'eea', 'bio', 'pc', 'maths', 'lea', 'staps', 'llcera', 'llcere',
  'compta', 'eco', 'socio', 'segpa'));

create table Forfait(--
  Ref_Forfait INTEGER,
  Prix_Forfait INTEGER,
  primary key (Ref_Forfait));

--
-- CREATE TABLE Etudiant(-- base de la table écrite par xavier
--   Num_Etudiant SERIAL NOT NULL,
--   nom_etudiant VARCHAR(25) NOT NULL,
--   prenom_etudiant VARCHAR(25) NOT NULL,
--   date_naissance_etudiant DATE NOT NULL,
--   filiere_etudiant Filiere NOT NULL,
--   tel_etudiant VARCHAR(12) NOT NULL,
--   mail_etudiant VARCHAR(40) NOT NULL,
--   rue_etudiant VARCHAR(30) NOT NULL,
--   ville_etudiant VARCHAR(25) NOT NULL,
--   code_postal_etudiant INTEGER NOT NULL,
--   membre_asso BOOLEAN NOT NULL,
--   PRIMARY KEY (Num_Etudiant));



create table Location(--
  Num_Location INTEGER,
  Duree_Location INTEGER,
  Date_debut_Location DATE,
  Num_Etudiant INTEGER,
  foreign key (Num_Etudiant) REFERENCES Etudiant,
  primary key (Num_Location)
);

create table Type_Materiel(--
  Intitule_Type_Materiel VARCHAR(20),
  Ref_Type_Materiel INTEGER,
  Prix_unite_hf INTEGER,
  primary key (Ref_type_Materiel)
);

create table Materiel_stock(--
  Ref_Materiel INTEGER,
  Intitule_Materiel VARCHAR(20),
  Ref_Type_Materiel INTEGER,
  Etat_Materiel ETAT,
  quantite INTEGER,
  foreign key (Ref_Type_Materiel) REFERENCES Type_Materiel,
  primary key (Ref_Materiel)
);

create table Caution(--
  Num_Caution SERIAL NOT NULL,
  Prix_Caution INTEGER,
  Num_Etudiant INTEGER,
  foreign key (Num_Etudiant) REFERENCES Etudiant,
  primary key (Num_Caution));


create table Entreprise(--
  Num_Entreprise INTEGER,
  Nom_Entreprise VARCHAR(20),
  Adresse_rue_Entreprise VARCHAR(50),
  Ville_Entreprise VARCHAR(15),
  Nom_contact_Entreprise VARCHAR(15),
  Mail_contact_Entreprise VARCHAR(30),
  primary key (Num_Entreprise));


create table Facture(--
  Num_Facture INTEGER,
  Date_Facture DATE,
  Prix_Facture INTEGER,
  Num_Entreprise INTEGER,
  foreign key (Num_Entreprise) REFERENCES Entreprise,
  primary key (Num_Facture)
);

create table Devis(--
  Num_Devis INTEGER,
  Prix_estime INTEGER,
  Date_Devis DATE,
  Num_Entreprise INTEGER,
  foreign key(Num_Entreprise) REFERENCES Entreprise,
  primary key (Num_Devis)
);

create table Materiel_Entreprise(--trigger
  Num_Entreprise INTEGER,
  Ref_type_Materiel INTEGER,
  Quantité INTEGER,
  foreign key(Num_Entreprise) REFERENCES Entreprise,
  foreign key(Ref_type_Materiel) REFERENCES Type_Materiel,
  primary key (Num_Entreprise,Ref_type_Materiel)
);
--
-- create table ParticipantAsso(--
--   Num_ParticipantAsso INTEGER,
--   Num_Etudiant INTEGER,
--   foreign key(Num_Etudiant) REFERENCES Etudiant,
--   primary key (Num_ParticipantAsso)
-- );
-- 
-- create table Evenement(--
--   Num_Evenement INTEGER,
--   primary key (Num_Evenement)
-- );
--
-- create table Responsable_de_service(--
--   Num_Responsable_de_service INTEGER,
--   primary key (Num_Responsable_de_service)
-- );

create table matériel_retour(--trigger
  Ref_Materiel INTEGER,
  Num_Location INTEGER,
  etat_materiel_retour ETAT,
  foreign key (Ref_Materiel) REFERENCES Materiel_stock,
  primary key (Ref_Materiel,Num_Location)
);

-- en commentaire pour les tables caution_encaisser et inscrit
-- ligne apportant l'erreur :
--psql:tables.sql:145: ERROR:  syntax error at or near "Num_Etudiant"
-- LINE 5:   foreign key Num_Etudiant REFERENCES Etudiant,
-- erreur corigé par : "Num_Etudiant INTEGER REFERENCES Etudiant,"

-- table caution encaisser concerne les caution que l'asso encaisse
-- car le matériel est en mauvais état
create table Caution_encaisser(--trigger
  Num_Caution INTEGER,
  Num_Etudiant INTEGER NOT NULL REFERENCES Etudiant,
  Caution_encaisser BOOL,
  --foreign key Num_Etudiant REFERENCES Etudiant,
  primary key(Num_Etudiant,Num_Caution)
);

create table inscrit(
  pseudo VARCHAR(20),
  mdp VARCHAR(20),
  Num_Etudiant INTEGER NOT NULL REFERENCES Etudiant,
  --foreign key Num_Etudiant REFERENCES Etudiant,
  primary key (pseudo)
);
