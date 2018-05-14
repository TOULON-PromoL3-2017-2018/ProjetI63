Create function nb_baggages()
returns TRIGGER AS $$
DECLARE

nb_bag_max integer;
nb_bagg integer;

BEGIN
nb_bag_max := (select nb_baggages_max from participe natural join necessite
  natural join solicite where participe.num_voyageur=new.num_voyageur and
  necessite.num_voyage=new.num_voyage and solicite.num_trajet=new.num_trajet);
nb_bagg := (SELECT nb_baggages from participe where participe.num_voyageur=new.num_voyageur
  and num_voyage=participe.num_voyage);

raise notice 'le nombre de baggage maximum est %d', nb_bag_max;
raise notice 'le nombre de baggage est %d', nb_bagg;

if (nb_bagg <= nb_bag_max) THEN
  UPDATE Participe SET nb_baggages = nb_bagg WHERE num_voyageur=new.num_voyageur
    and num_voyage=new.num_voyage;
else
  raise notice 'le nombre de baggage maximum est %d', nb_bag_max;
END IF;
return new;
END;
$$ LANGUAGE PLPGSQL;

Create TRIGGER nb_baggages
before Insert on PARTICIPE
for each row
execute procedure nb_baggages();
