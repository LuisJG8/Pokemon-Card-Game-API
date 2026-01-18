

START TRANSACTION;

UPDATE pocket_tcg
SET type_p 		 	 = CASE WHEN type_p 	 	  = 'NaN' THEN NULL ELSE type_p 		  END,
	hp	   	  	 	 = CASE WHEN hp			 	  = 'NaN' THEN NULL ELSE hp 			  END,
	retreat_cost 	 = CASE WHEN retreat_cost 	  = 'NaN' THEN NULL ELSE retreat_cost 	  END,
	sub_type    	 = CASE WHEN sub_type 	  	  = 'NaN' THEN NULL ELSE sub_type 		  END,
	evolves_from	 = CASE WHEN evolves_from 	  = 'NaN' THEN NULL ELSE evolves_from 	  END,
	attacks 	 	 = CASE WHEN attacks 	  	  = 'NaN' THEN NULL ELSE attacks 		  END,
	ex_rule 	 	 = CASE WHEN ex_rule 	 	  = 'NaN' THEN NULL ELSE ex_rule 		  END,
	weaknesses	 	 = CASE WHEN weaknesses 	  = 'NaN' THEN NULL ELSE weaknesses 	  END,
	card_description = CASE WHEN card_description = 'NaN' THEN NULL ELSE card_description END,
	set_p			 = CASE WHEN set_p			  = 'NaN' THEN NULL ELSE set_p 			  END,
	rarity			 = CASE WHEN rarity			  = 'NaN' THEN NULL ELSE rarity			  END,
	pack			 = CASE WHEN pack			  = 'NaN' THEN NULL ELSE pack			  END,
	ability			 = CASE WHEN ability		  = 'NaN' THEN NULL ELSE ability		  END
;

SELECT *
FROM pocket_tcg
;

COMMIT TRANSACTION;
ROLLBACK;

SELECT *
FROM pocket_tcg