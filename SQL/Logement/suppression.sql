--DROP TRIGGER verif_logement ON LOGEMENT;
DROP TRIGGER creation_contrat ON CONTRAT_LOGEMENT;
DROP TRIGGER verif_dates_contrat ON CONTRAT_LOGEMENT;
DROP TRIGGER contrat_fini ON CONTRAT_LOGEMENT;
DROP TABLE PROPRIETAIRE,LOGEMENT,DEMANDEUR,CAUTIONNAIRE,SERVICE_LOGEMENT,ASSOCIE,CONTRAT_LOGEMENT CASCADE;

DROP DOMAIN types,prestations_logement,taches CASCADE;
