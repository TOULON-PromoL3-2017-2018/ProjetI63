insert into voyageur values(123);
insert into voyageur values(231, 200);
insert into voyageur values(567);

insert into Organisateur values(1, 'orgnum1', 'toulouse', '11111',
    '32 rue du commerce', '0612532653', 'org1.caramel@orange.fr');
insert into Organisateur values(2, 'arognum2', 'brignoles', '83200',
    '256 rue de la liberté', '0689423135', 'org2.chocolat@gmail.fr');
insert into Organisateur values(3, 'orgnum3', 'Lyon', '56312',
    '3256 boulevard longchamps', '0653213589', 'org3.vanille@orange.fr');
insert into Organisateur values(4, 'orgnum4', 'Toulon', '83100',
    '21 avenue du chemin', '0632359854', 'org4.fraise@hotmail.fr');

insert into Responsable values(1, 'Tomate', 'Persil', '0653254875');
insert into Responsable values(2, 'Poireau', 'Fenouil', '0656847595');
insert into Responsable values(3, 'Courgette', 'Ail', '0621489632');


insert into Voyage values(1, 3, 1, 'culturel', '15 000', 'TGV');
insert into Voyage values(2, 2, 3, 'decouverte', '2 000', 'BUS');
insert into Voyage values(3, 1, 1, 'vacances', '100', 'BUS');
insert into Voyage values(4, 2, 2, 'culturel', '250', 'BUS');

insert into participe values(123, 2, NULL, 2);
insert into participe values(123, 4, NULL, 1);
insert into participe values(231, 2, 8, 1);
insert into participe values(567, 2, NULL, 2);

  insert into trajet values(1, 3, '2018/03/25', '2018/03/26', 'Toulon', 'Reims',
      '06:30', '15:30');
  insert into trajet values(2, 1, '2017/11/15', '2017/11/15', 'Toulon', 'Poitier',
      '06:30', '15:30');
  insert into trajet values(3, 3, '2018/01/11', '2018/01/11', 'Toulon', 'Nantes',
      '06:30', '15:30');


insert into entre_location values(1, 'entrep1', 'Puget', '83390',
  '65 rue de la cooperative', '0635982654', 'myrtille@gmail.com');
insert into entre_location values(2, 'entrep2', 'Sollies', '83253',
  '32 rue de la liberation', '0632598621', 'chausson@orange.fr');
insert into entre_location values(3, 'entrep3', 'Bormes', '83230',
  '89 avenue du pain', '0653894258', 'fondant@hotmail.fr');

insert into Vehicule values('XA-23-FDS', 2, 'BUS', 50);
insert into vehicule values('FTY-235-FDR', 1, 'Voiture', 4);

insert into solicite values(1, 3, 'XA-23-FDS', '0635982654', '56', 3, 45);
