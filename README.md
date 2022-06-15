## SMASH THE BRICKS
------------------
#### You have a given number of bricks - each can be smashed completely in one hit of a big hammer or several hits of a small hammer. 

#### The input array "newtons" equals the force needed to smash the brick with the small hammer so that if the newtons for a particular brick is equal to 3 it would take 3 hits of the small hammer to completely smash the brick. Only a given number of hits with the big hammer are allowed - this is defined by the input variable BigHits. There can be zero big hammer hits or zero small hammer hits in some cases.

#### Work out the minimum number of hits needed to smash all the bricks.

#### Return the total hits needed to smash all the bricks, the index values of the bricks that were smashed by the big hammer in ascending order and then index values of the bricks smashed by the small hammer in ascending order.
 
* Example inputs: 3, [3, 6, 8, 9, 11, 24, 25]

* Example outputs: Sort to 3, 6, 8, 9, 11, 24, 25 - smash 25, 24, 11 with 3 big hits, smash rest ie: 3, 6, 8, 9 with small hits therefore total small hits = 26 and total hits = 26 + 3 = 29. 

* Output = 29, [11, 24, 25], [3, 6, 8, 9]
