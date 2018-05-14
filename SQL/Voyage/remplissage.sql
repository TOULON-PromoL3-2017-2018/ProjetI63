insert into voyageur values(123);
insert into voyageur values(231, 200);
insert into voyageur values(567);

insert into Organisateur (nom, prenom, ville, code_ps, rue, tel, mail) values(
  'orgnum1', 'preorgnum1', 'toulouse', '11111', '32 rue du commerce',
  '0612532653', 'org1.caramel@orange.fr');
insert into Organisateur (nom, prenom, ville, code_ps, rue, tel, mail) values(
  'orgnum2', 'preorgnum2', 'brignoles', '83200', '256 rue de la liberté',
  '0689423135', 'org2.chocolat@gmail.fr');
insert into Organisateur (nom, prenom, ville, code_ps, rue, tel, mail) values(
  'orgnum3', 'preorgnum1', 'Lyon', '56312', '3256 boulevard longchamps',
  '0653213589', 'org3.vanille@orange.fr');
insert into Organisateur (nom, prenom, ville, code_ps, rue, tel, mail) values(
  'orgnum4', 'preorgnum1', 'Toulon', '83100', '21 avenue du chemin',
  '0632359854', 'org4.fraise@hotmail.fr');

insert into Responsable (nom_responsable, prenom_responsable, tel_responsable)
  values('Tomate', 'Persil', '0653254875');
insert into Responsable (nom_responsable, prenom_responsable, tel_responsable)
  values('Poireau', 'Fenouil', '0656847595');
insert into Responsable (nom_responsable, prenom_responsable, tel_responsable)
  values('Courgette', 'Ail', '0621489632');


insert into Voyage (num_responsable, num_organisateur, destination, type, prix)
  values(3, 1, 'Moscou', 'culturel', '1000');
insert into Voyage (num_responsable, num_organisateur, destination, type, prix)
  values(2, 3, 'Paris', 'decouverte', '250');
insert into Voyage (num_responsable, num_organisateur, destination, type, prix)
  values(1, 1, 'Londres', 'vacances', '300');
insert into Voyage (num_responsable, num_organisateur, destination, type, prix)
  values(2, 2, 'Moscou', 'culturel', '1200');

insert into participe (num_voyageur, num_voyage, satisfaction, nb_baggages)
  values(123, 2, DEFAULT, 2);
insert into participe (num_voyageur, num_voyage, satisfaction, nb_baggages)
  values(123, 4, DEFAULT, 1);
insert into participe (num_voyageur, num_voyage, satisfaction, nb_baggages)
  values(231, 2, 8, 1);
insert into participe (num_voyageur, num_voyage, satisfaction, nb_baggages)
  values(567, 2, DEFAULT, 2);


insert into trajet (lieu_depart, lieu_arrive) values('Toulon', 'Moscou');
insert into trajet (lieu_depart, lieu_arrive) values('Moscou', 'Paris');
insert into trajet (lieu_depart, lieu_arrive) values('Toulon', 'Paris');
insert into trajet (lieu_depart, lieu_arrive) values('Paris', 'Toulon');


insert into necessite (num_trajet, num_voyage, sens, date_depart, date_arrive,
  heure_depart, heure_arrive, prix_trajet) values(1, 2, 'aller', '2018/03/25',
  '2018/03/26', '06:50', '13:30', 50);
insert into necessite (num_trajet, num_voyage, sens, date_depart, date_arrive,
  heure_depart, heure_arrive, prix_trajet) values(2, 3, 'retour', '2017/11/15',
  '2017/11/15', '06:30', '15:30', 100);
insert into necessite (num_trajet, num_voyage, sens, date_depart, date_arrive,
  heure_depart, heure_arrive, prix_trajet) values(3, 2, 'aller', '2018/01/11',
  '2018/01/11', '09:22', '15:18', 75);
insert into necessite (num_trajet, num_voyage, sens, date_depart, date_arrive,
  heure_depart, heure_arrive, prix_trajet) values(2, 2, 'retour', '2018/03/25',
  '2018/03/26', '15:50', '11:00', 25);


insert into entre_location (nom_entreprise, ville_entreprise,
  code_ps_entreprise, rue_entreprise, tel_entreprise, mail_entreprise)
  values('entrep1', 'Puget', '83390', '65 rue de la cooperative',
  '0635982654', 'myrtille@gmail.com');
insert into entre_location (nom_entreprise, ville_entreprise,
  code_ps_entreprise, rue_entreprise, tel_entreprise, mail_entreprise)
  values('entrep2', 'Sollies', '83253', '32 rue de la liberation',
  '0632598621', 'chausson@orange.fr');
insert into entre_location (nom_entreprise, ville_entreprise,
  code_ps_entreprise, rue_entreprise, tel_entreprise, mail_entreprise)
  values('entrep3', 'Bormes', '83230', '89 avenue du pain', '0653894258',
  'fondant@hotmail.fr');

insert into Vehicule values('XA-23-FDS', 2, 'BUS', 50);
insert into vehicule values('FTY-235-FDR', 1, 'Voiture', 4);

insert into solicite values(1, 'XA-23-FDS', '0635982654', 56, 3, 45);
