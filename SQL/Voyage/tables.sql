create table voyageur
  (
  num_voyageur integer primary key,
  du integer
  );


create table Organisateur
  (
  num_organisateur serial primary key,
  nom varchar(20) NOT NULL,
  prenom varchar(20),
  ville varchar(20) NOT NULL,
  code_ps char(5) NOT NULL,
  rue varchar(50) NOT NULL,
  tel char(10) NOT NULL,
  mail varchar(30) NOT NULL,
  specialisation varchar(20)
  );



create table Responsable
  (
  num_responsable serial primary key,
  nom_responsable varchar(20) NOT NULL,
  prenom_responsable varchar(20) NOT NULL,
  tel_responsable char(10) NOT NULL
  );

create table Voyage
  (
  num_voyage serial primary key,
  num_responsable integer references Responsable NOT NULL,
  num_organisateur integer references Organisateur NOT NULL,
  destination varchar(20) NOT NULL,
  type varchar(20) NOT NULL,
  prix varchar(6) NOT NULL
  );

create table Participe
  (
  num_voyageur integer references Voyageur NOT NULL,
  num_voyage integer references Voyage NOT NULL,
  satisfaction integer NOT NULL default '1',
  nb_baggages integer,
  primary key (num_voyageur, num_voyage)
  );

create table Trajet
  (
  num_trajet serial primary key,
  lieu_depart varchar(20) NOT NULL, --format 06:32
  lieu_arrive varchar(20) NOT NULL
  );

create table Necessite
  (
  num_trajet integer references Trajet NOT NULL,
  num_voyage integer references Voyage NOT NULL,
  sens varchar(6) NOT NULL,
  date_depart date NOT NULL,
  date_arrive date NOT NULL,
  heure_depart char(5),
  heure_arrive char(5),
  prix_trajet integer NOT NULL,
  primary key (num_voyage, num_trajet)
  );

create table entre_location
  (
  num_entreprise serial primary key,
  nom_entreprise varchar(20) NOT NULL,
  ville_entreprise varchar(20) NOT NULL,
  code_ps_entreprise char(5) NOT NULL,
  rue_entreprise varchar(30) NOT NULL,
  tel_entreprise char(10) NOT NULL,
  mail_entreprise varchar(30) NOT NULL
  );

create table Vehicule
  (
  immatriculation varchar(20) primary key,
  num_entre_location integer references entre_location NOT NULL,
  type_vehicule varchar(10) NOT NULL,
  nb_places integer
  );

create table Solicite
  (
  num_trajet integer NOT NULL,
  immatriculation varchar(50) references Vehicule(immatriculation) NOT NULL,
  tel_chauffeur char(10) NOT NULL,
  nb_passagers integer NOT NULL,
  nb_baggages_max integer,
  poids_baggages_max integer,
  foreign key(num_trajet) references Trajet,
  primary key(num_trajet, immatriculation)
  );


-- create schema Voyage;
-- set search_path to Voyage;
