
S.W.E.A.T.H.E.R  APP


#BOOLEAN TABLE FOR S.W.E.A.T.H.E.R PREDICTION

SkyType = [RAINY: 1, SNOW: 2, CLEARSKY: 3]

Product 	            Min-Max Temp	    WaterProof         Required[SkyType] 
SUN GLASSES                 75-100              FALSE           [CLEARSKY, SUNNY]                  
RAIN JACKET                 62-80               TRUE            [RAINY]                               
SWEATER                     50-68               TRUE            [SNOW]
LIGHT COAT                  35-55               TRUE            [CLEARSKY, RAINY]
COMFORTABLE SHOES           25-90               FALSE           [CLEARSKY]
HEAVY COAT                  0-40                TRUE            [RAINY, SNOW]
SNOW BOOTS                  0-35                TRUE            [SNOW]     