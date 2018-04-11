insert into voyageur values(123);
insert into voyageur values(231, 200);
insert into voyageur values(567);

insert into Organisateur (nom, ville, code_ps, rue, tel, mail) values('orgnum1',
   'toulouse', '11111', '32 rue du commerce', '0612532653', 'org1.caramel@orange.fr');
insert into Organisateur (nom, ville, code_ps, rue, tel, mail) values('orgnum2',
   'brignoles', '83200', '256 rue de la liberté', '0689423135', 'org2.chocolat@gmail.fr');
insert into Organisateur (nom, ville, code_ps, rue, tel, mail) values('orgnum3',
   'Lyon', '56312', '3256 boulevard longchamps', '0653213589', 'org3.vanille@orange.fr');
insert into Organisateur (nom, ville, code_ps, rue, tel, mail) values('orgnum4',
   'Toulon', '83100', '21 avenue du chemin', '0632359854', 'org4.fraise@hotmail.fr');

insert into Responsable (nom_responsable, prenom_responsable, tel_responsable)
  values('Tomate', 'Persil', '0653254875');
insert into Responsable (nom_responsable, prenom_responsable, tel_responsable)
  values('Poireau', 'Fenouil', '0656847595');
insert into Responsable (nom_responsable, prenom_responsable, tel_responsable)
  values('Courgette', 'Ail', '0621489632');


insert into Voyage (num_responsable, num_organisateur, type, prix,
  type_transport) values(3, 1, 'culturel', '15 000', 'TGV');
insert into Voyage (num_responsable, num_organisateur, type, prix,
  type_transport) values(2, 3, 'decouverte', '2 000', 'BUS');
insert into Voyage (num_responsable, num_organisateur, type, prix,
  type_transport) values(1, 1, 'vacances', '100', 'BUS');
insert into Voyage (num_responsable, num_organisateur, type, prix,
  type_transport) values(2, 2, 'culturel', '250', 'BUS');

insert into participe values(123, 2, NULL, 2);
insert into participe values(123, 4, NULL, 1);
insert into participe values(231, 2, 8, 1);
insert into participe values(567, 2, NULL, 2);

insert into trajet (num_voyage, date_depart, date_arrive, lieu_depart,
  lieu_arrive, heure_depart, heure_arrive) values(3, '2018/03/25',
  '2018/03/26', 'Toulon', 'Reims', '06:30', '15:30');
insert into trajet (num_voyage, date_depart, date_arrive, lieu_depart,
  lieu_arrive, heure_depart, heure_arrive) values(1, '2017/11/15',
    '2017/11/15', 'Toulon', 'Poitier', '06:30', '15:30');
insert into trajet (num_voyage, date_depart, date_arrive, lieu_depart,
  lieu_arrive, heure_depart, heure_arrive) values(3, '2018/01/11',
    '2018/01/11', 'Toulon', 'Nantes', '06:30', '15:30');


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

insert into solicite values(1, 3, 'XA-23-FDS', '0635982654', '56', 3, 45);
