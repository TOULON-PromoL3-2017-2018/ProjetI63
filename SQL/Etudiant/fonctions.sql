CREATE OR REPLACE FUNCTION Check_Comptes()
RETURNS INTEGER
AS $$
DECLARE Qtt INTEGER;
BEGIN
-- vérifier si l'addition marche
SELECT SUM(montant) + (SELECT SUM(montant) SELECT SUM(montant) FROM Subvention) FROM Subvention INTO Qtt;
RETURN (Qtt);
END;
$$ LANGUAGE PLPGSQL;
