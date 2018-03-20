insert into voyageur values(123);
insert into voyageur values(231);
insert into voyageur values(567);

insert into Organisateur values(1, 'orgnum1', 'toulouse', '11111',
    '32 rue du commerce', '0612532653', 'org1.caramel@orange.fr');
insert into Organisateur values(2, 'arognum2', 'brignoles', '83200',
    '256 rue de la liberté', '0689423135', 'org2.chocolat@gmail.fr');
insert into Organisateur values(3, 'orgnum3', 'Lyon', '56312',
    '3256 boulevard longchamps', '0653213589', 'org3.vanille@orange.fr');
insert into Organisateur values(4, 'orgnum4', 'Toulon', '83100',
    '21 avenue du chemin', '0632359854', 'org4.fraise@hotmail.fr');


insert into Voyage values(1, 3, '52', 'culturel', '15 000');
insert into Voyage values(2, 2, '45', 'decouverte', '2 000');
insert into Voyage values(3, 1, '12', 'vacances', '100');
insert into Voyage values(4, 2, '28', 'culturel', '250');

insert into participe values(123, 2, NULL, 2);
insert into participe values(123, 4, NULL, 1);
insert into participe values(231, 2, 8, 1);
insert into participe values(567, 2, NULL, 2);

insert into entre_location values(1, 'entrep1', 'Puget', '83390',
  '65 rue de la cooperative', '0635982654', 'myrtille@gmail.com');
insert into entre_location values(2, 'entrep2', 'Sollies', '83253',
  '32 rue de la liberation', '0632598621', 'chausson@orange.fr');
insert into entre_location values(3, 'entrep3', 'Bormes', '83230',
  '89 avenue du pain', '0653894258', 'fondant@hotmail.fr');


insert into trajet values(1, 3, '2018/03/25', '2018/03/26', 'Toulon', 'Reims',
    '06:30', '15:30');
insert into trajet values(2, 1, '2017/11/15', '2017/11/15', 'Toulon', 'Poitier',
    '06:30', '15:30');
insert into trajet values(1, 3, '2018/01/11', '2018/01/11', 'Toulon', 'Nantes',
    '06:30', '15:30');


insert into solicite values(1, 3, 'AX-321-TH', '0635982654', '56', '86',
    3, 45);
