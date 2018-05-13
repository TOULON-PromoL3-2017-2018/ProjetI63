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
CREATE OR REPLACE FUNCTION GagnantPers(clsport TEXT) RETURNS
TABLE(NumParticipant INTEGER, NbVictoire BIGINT) AS $$
DECLARE
  numsport INT;
BEGIN
  numsport := (SELECT nosport FROM sport WHERE nomsport = clsport);
  RETURN query
  select novainqueur, count(*)
  from (select noparticipantautre, nouniversite from participantautre union all select * from participantasso) as participant, evenementsport
  where participant.noparticipantautre = evenementsport.novainqueur and nosport = numsport group by novainqueur;

END;
$$ LANGUAGE PLPGSQL;
