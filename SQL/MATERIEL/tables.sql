-- clain cyril

create schema asso;
SET search_path to asso;

--creation d'un domaine BOOL :
create domain BOOL
as char
check(value in('T','F'));

--creation d'un domaine ETAT :
create domain ETAT
as char
check(value in('AB','B','TB'));


create table Forfait(
  Ref_Forfait INTEGER,
  Prix_Forfait INTEGER,
  primary key (ref_Forfait));

create table Caution(
  Num_Caution INTEGER,
  Prix_Caution INTEGER,
  Caution_encaisser BOOL,
  primary key (Num_Caution));

create table Location(
  Num_Location INTEGER,
  Duree_Location DATE,
  Date_debut_Location DATE,
  primary key (Num_Location)
);

create table Materiel(
  Ref_Materiel INTEGER,
  Intitule_Materiel VARCHAR(20),
  Etat_Materiel ETAT,
  primary key (Ref_Materiel)
);

create table Type_Materiel(
  Intitule_Type_Materiel VARCHAR(20),
  Ref_Type_Materiel INTEGER,
  Prix_unite_hf INTEGER,
  primary key (Ref_type_Materiel)
);

create table Facture(
  Num_Facture INTEGER,
  Date_Facture DATE,
  Prix_Facture INTEGER,
  primary key (Num_Facture)
);

create table Entreprise(
  Num_Entreprise INTEGER,
  Nom_Entreprise VARCHAR(20),
  Adresse_(rue)_Entreprise VARCHAR(50),
  Ville_Entreprise VARCHAR(15),
  Nom_contact_Entreprise VARCHAR(15),
  Mail_contact_Entreprise VARCHAR(30),
  primary key (Num_Entreprise)
);

create table Devis(
  Num_Devis INTEGER,
  Prix_estime INTEGER,
  Date_Devis INTEGER,
  primary key (Num_Devis)
);

create table Materiel_Entreprise(
  Num_Entreprise INTEGER,
  Ref_type_Materiel INTEGER,
  Quantité INTEGER,
  primary key (Num_Entreprise,Ref_type_Materiel)
);

create table Etudiant(
  Num_Etudiant INTEGER,
  primary key (Num_Etudiant)
);

create table ParticipantAsso(
  Num_ParticipantAsso INTEGER,
  primary key (Num_ParticipantAsso)
);

create table Evenement(
  Num_Evenement INTEGER,
  primary key (Num_Evenement)
);

create table Responsable_de_service(
  Num_Responsable_de_service INTEGER,
  primary key (Num_Responsable_de_service)
);
