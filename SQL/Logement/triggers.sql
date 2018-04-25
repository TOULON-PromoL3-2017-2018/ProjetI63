/*Trigger de verification de donnees pour la table logement*/
-- CREATE OR REPLACE FUNCTION verif_logement()
-- RETURNS TRIGGER
-- AS $$
--
-- BEGIN
-- 	-- IF new.nb_pieces IS NULL THEN
-- 	-- 	RAISE EXCEPTION 'Le nombre de pièces du logement % ne peut pas être nul',new.num_logement;
-- 	-- END IF;
--
-- 	-- IF new.surface_logement IS NULL THEN
-- 	-- 	RAISE EXCEPTION 'La surface du logement % ne peut pas être nulle', new.num_logement;
-- 	-- END IF;
-- 	RETURN NULL;
-- END;
--
-- $$ LANGUAGE plpgsql;
--
-- CREATE TRIGGER verif_logement BEFORE INSERT OR UPDATE ON LOGEMENT
-- 	FOR EACH ROW EXECUTE PROCEDURE verif_logement();


/* trigger permettant d'initialiser la date du contrat à la date du jour*/
CREATE OR REPLACE FUNCTION creation_contrat()
RETURNS TRIGGER
AS $$
BEGIN
	IF new.date_sign IS NULL THEN
		UPDATE CONTRAT_LOGEMENT SET date_sign = '2018-01-18';--current_timestamp;
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER creation_contrat AFTER INSERT OR UPDATE ON CONTRAT_LOGEMENT
	FOR EACH ROW EXECUTE PROCEDURE creation_contrat();



/* Verifications de la cohérence des dates*/
CREATE OR REPLACE FUNCTION verif_dates_contrat()
RETURNS TRIGGER
AS $$

BEGIN

	IF new.date_emm < new.date_sign THEN
		RAISE EXCEPTION 'Vous ne pouvez pas emménager avant que le contrat % soit signé',new.num_contrat;

	END IF;

	IF new.date_dep_ant < new.date_sign THEN
		RAISE EXCEPTION 'Vous ne pouvez pas avoir une date de départ anticipée si aucun contrat';
	END IF;

	IF new.date_dep_ant < new.date_emm THEN
		RAISE EXCEPTION 'Vous ne pouvez pas faire un depart anticipé avant de vous être installé';
	END IF;

	IF new.date_dep_ant > new.date_fin_prevu THEN
		RAISE EXCEPTION 'Vous ne pouvez pas avoir une date de départ anticipée si votre contrat est terminé';
	END IF;

	IF new.date_fin_prevu < new.date_emm THEN
		RAISE EXCEPTION 'Vous ne pouvez pas partir si vous ne vous êtes pas installés';
	END IF;

	IF new.date_fin_prevu < new.date_sign THEN
		RAISE EXCEPTION 'Vous ne pouvez pas avoir une date de fin de contrat si aucun contrat';
	END IF;
	RETURN NULL;
END;

$$ LANGUAGE plpgsql;

CREATE TRIGGER verif_dates_contrat AFTER INSERT OR UPDATE ON CONTRAT_LOGEMENT
	FOR EACH ROW EXECUTE PROCEDURE verif_dates_contrat();



/*Trigger permettant de mettre à jour la validité du contrat*/
CREATE OR REPLACE FUNCTION contrat_fini()
RETURNS TRIGGER
AS $$
BEGIN

	IF new.date_fin_prevu<NOW() AND new.renouvellement='0' THEN
		UPDATE CONTRAT_LOGEMENT SET contrat_termine ='1';

	END IF;


	IF new.date_dep_ant<NOW() AND new.renouvellement='0' THEN
		UPDATE CONTRAT_LOGEMENT SET contrat_termine ='1';

	END IF;

	IF new.date_fin_prevu=NOW() AND new.renouvellement='1' THEN
		UPDATE CONTRAT_LOGEMENT SET contrat_termine ='0';

	END IF;
	RETURN NEW;
	--RETURN NULL;

END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER contrat_fini AFTER INSERT ON CONTRAT_LOGEMENT
	FOR EACH ROW EXECUTE PROCEDURE contrat_fini();
