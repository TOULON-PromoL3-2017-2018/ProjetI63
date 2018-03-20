create table voyageur
  (
  num_voyageur integer primary key,
  du integer
  );

  create table Organisateur
    (
    num_organisateur integer primary key,
    nom varchar(20) NOT NULL,
    ville varchar(20) NOT NULL,
    code_ps char(5) NOT NULL,
    rue varchar(50) NOT NULL,
    tel char(10) NOT NULL,
    mail varchar(30) NOT NULL,
    specialisation varchar(20)
    );

create table Voyage
  (
  num_voyage integer primary key,
  num_organisateur integer references Organisateur NOT NULL,
  responsable varchar(20) NOT NULL,
  type varchar(20) NOT NULL,
  prix varchar(6) NOT NULL
  );

create table Participe
  (
  num_voyageur integer,
  num_voyage integer,
  satisfaction integer,
  nb_baggages integer,
  primary key (num_voyageur, num_voyage)
  );


create table entre_location
  (
  num_locataire integer primary key,
  nom varchar(20) NOT NULL,
  ville varchar(20) NOT NULL,
  code_ps char(5) NOT NULL,
  rue varchar(30) NOT NULL,
  tel char(10) NOT NULL,
  mail varchar(30) NOT NULL
  );


create table Trajet
  (
  num_voyage integer,
  num_locataire integer,
  date_depart date NOT NULL,
  date_arrive date,
  lieu_depart varchar(20) NOT NULL,
  lieu_arrive varchar(20) NOT NULL,
  heure_depart char(5) NOT NULL, --format 06:32
  heure_arrive char(5),
  primary key(num_voyage, date_depart, heure_depart)
  );

create table Solicite
  (
  num_voyage integer,
  num_locataire integer,
  immatriculation varchar(10) NOT NULL,
  tel_chauffeur char(10) NOT NULL,
  nb_passagers integer NOT NULL,
  nb_places_disponibles integer NOT NULL,
  nb_baggages_max integer,
  poids_baggages_max integer,
  primary key(num_voyage, num_locataire)
  );




-- create schema Voyage;
-- set search_path to Voyage;
