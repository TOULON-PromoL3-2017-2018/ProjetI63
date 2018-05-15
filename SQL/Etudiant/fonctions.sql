-- --test de fonction :
-- CREATE OR REPLACE FUNCTION Check_Comptes()
-- RETURNS INTEGER
-- AS $$
-- DECLARE Qtt INTEGER;
-- BEGIN
-- -- vérifier si l'addition marche
-- SELECT SUM(montant) + (SELECT SUM(montant) SELECT SUM(montant) FROM Subvention) FROM Subvention INTO Qtt;
-- RETURN (Qtt);
-- END;
-- $$ LANGUAGE PLPGSQL;

-- trigger ici :
CREATE OR REPLACE FUNCTION Update_Financement()
RETURNS trigger
AS $$
BEGIN
IF new.traitement = '0' THEN
  UPDATE Financement SET traitement = '1';
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER Update_Financement AFTER UPDATE ON Financement
FOR EACH ROW EXECUTE PROCEDURE Update_Financement();
