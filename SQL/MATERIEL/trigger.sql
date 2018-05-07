--CREATE OR REPLACE FUNCTION VerifStockmateriel()
--RETURNS TRIGGER
--AS $$
--DECLARE etat_stock INTEGER;
--BEGIN
  -- SELECT new.quantite FROM produit INTO etat_stock;
   --IF (etat_stock = 0) THEN  RAISE INFO 'Produit indisponible.' ; RETURN NULL;
    --ELSE RETURN new;
--END IF;
--END;
--$$ LANGUAGE PLPGSQL;



--CREATE TRIGGER Materiel_stok
--BEFORE UPDATE
--ON Materiel_stok
--FOR EACH ROW
--EXECUTE PROCEDURE VerifStockProduit();

-- trigger: si facture alors stock +
--        : si location alors stock -
-- si retour location alors stock +
-- si retour location mais matériel etat = ab alors Materiel_Entreprise
