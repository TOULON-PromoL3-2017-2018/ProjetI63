--Retourne les équipes gagnantes pour ce sport (chaque vainqueur evenementsport)
--Sport collectif uniquement
CREATE OR REPLACE FUNCTION GagnantEq(clsport TEXT) RETURNS
TABLE(NomEq TEXT, NbVictoire INTEGER) AS $$
BEGIN
  SELECT NomEquipe, count(NomEquipe)
  FROM Sport NATURAL JOIN  EvenementSport NATURAL JOIN Evenement
  NATURAL JOIN InscritEquipe NATURAL JOIN Equipe
  WHERE NomSport = clsport AND NoVainqueur = NumEquipe
END;
$$ LANGUAGE PLPGSQL;

--Retourne les personnes gagnantes pour ce sport
--Sport individuel uniquement
--Retourne le NoParticipantAsso en attendant fusion avec table Etudiant
--Faire test natural join avec evenement et InscritAsso et InscritAutre
--et voir ce qui en sort.
CREATE OR REPLACE FUNCTION GagnantPers(clsport TEXT) RETURNS
TABLE(NumParticipant INTEGER, NbVictoire INTEGER) AS $$
BEGIN
  --en attente
END;
$$ LANGUAGE PLPGSQL;
