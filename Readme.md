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


![Capture](https://user-images.githubusercontent.com/30177434/114344866-3b6b3b80-9b7e-11eb-810a-d9188c4bd736.PNG)
