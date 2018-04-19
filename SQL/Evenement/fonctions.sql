--Retourne les équipes gagnantes pour ce sport (chaque vainqueur evenementsport)
--Sport collectif uniquement
CREATE OR REPLACE FUNCTION GagnantEq(clsport TEXT) RETURNS
TABLE(NomEq VARCHAR(30), NbVictoire BIGINT) AS $$
BEGIN
  RETURN query
  SELECT equipe.nomequipe, count(equipe.nomequipe) as NbVictoire
  FROM Evenementsport NATURAL JOIN sport, equipe
  WHERE novainqueur = equipe.numequipe AND nomsport = clsport
  GROUP BY nomequipe;
END;
$$ LANGUAGE PLPGSQL;

--Retourne les personnes gagnantes pour ce sport
--Sport individuel uniquement
--Retourne le NoParticipantAsso en attendant fusion avec table Etudiant
--Faire test natural join avec evenement et InscritAsso et InscritAutre
--et voir ce qui en sort.
--CREATE OR REPLACE FUNCTION GagnantPers(clsport TEXT) RETURNS
--TABLE(NumParticipant INTEGER, NbVictoire INTEGER) AS $$
--BEGIN
  --en attente
--END;
--$$ LANGUAGE PLPGSQL;
