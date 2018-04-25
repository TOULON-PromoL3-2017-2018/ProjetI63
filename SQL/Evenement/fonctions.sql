--Retourne les équipes gagnantes pour ce sport (chaque vainqueur evenementsport)
--Sport collectif uniquement
CREATE OR REPLACE FUNCTION GagnantEq(clsport TEXT) RETURNS
TABLE(NomEq VARCHAR(30), NbVictoire BIGINT) AS $$
BEGIN
  RETURN query
  SELECT equipe.nomequipe, count(equipe.nomequipe) as NbVictoire
  FROM Evenementsport NATURAL JOIN sport, equipe
  WHERE novainqueur = equipe.numequipe AND nomsport = clsport
  GROUP BY nomequipe
  ORDER BY 1;
END;
$$ LANGUAGE PLPGSQL;

--Retourne les personnes gagnantes pour ce sport
--Sport individuel uniquement
--Retourne le NoParticipantAsso en attendant fusion avec table Etudiant
--Faire test natural join avec evenement et InscritAsso et InscritAutre
--et voir ce qui en sort.
--CREATE OR REPLACE FUNCTION GagnantPers(clsport TEXT) RETURNS
--TABLE(NumParticipant INTEGER, NbVictoire BIGINT) AS $$
--BEGIN
  --en attente
--END;
--$$ LANGUAGE PLPGSQL;
--un truc  dans le genre mais prob de doublon et manque le compte
--select distinct noevenementsport, novainqueur from participantasso, participantautre, evenementsport natural join sport where (noparticipantasso = novainqueur or noparticipantautre = novainqueur) and nomsport = 'Tennis';
