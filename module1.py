#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'smashTheBricks' function below.
#
# The function is expected to return a 2D_LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER bigHits
#  2. INTEGER_ARRAY newtons
#

def smashTheBricks(bigHits, newtons):
    # Write your code here
    n = len(newtons)
    
    # Save unsorted array
    unsortedNewtons = newtons[:]
    
    # Sort newtons ascending
    newtons.sort()
    
    # If Equal or GT Big Hits to number of bricks then All Big Hits
    if  bigHits >= n:
        bigHits = n

        selLastNewtons = newtons[:]         
        sum1 = 0     
        # No SmallHits so set array output value to -1
        selFirstIndexNewtons = -1     
        
        # Get position indices for these values
        selLastIndexNewtons = []
        position = 0
        ct = n
        ct1 = len(selLastNewtons)
                
        for i in range(0,ct):
            x = 0
            for x in range(0,ct1):
                if unsortedNewtons[i] == selLastNewtons[x]:
                    position = i + 1                  
                            
                    # Add to output array
                    selLastIndexNewtons.append(position)
                 
    elif bigHits > 0: 
        
        # There are fewer big hits than bricks  
        # Select largest force values in newtons to be used for Big Hits
        selLastNewtons = newtons[-bigHits:]
        
        # Get position indices for these values
        selLastIndexNewtons = []
        position = 0
        ct = n
        ct1 = len(selLastNewtons)
        
        for i in range(0,ct):
            x = 0
            for x in range(0,ct1):
                if unsortedNewtons[i] == selLastNewtons[x]:
                    position = i + 1                  
                    
                    # Add to output array
                    selLastIndexNewtons.append(position)
                             
    else:
        # No big hits
        selLastIndexNewtons = -1
                     
    # Select remaining smaller force values in newtons for Small Hits
    firstNewtons = n - bigHits
    
    # If there are small hits or all small hits
    if firstNewtons != 0 or firstNewtons == newtons_count:
        selFirstNewtons = newtons[:firstNewtons]
        
        # Get position indices for these values
        selFirstIndexNewtons = []
        position = 0
        ct = n
        ct1 = len(selFirstNewtons)
        
        for i in range(0,ct):

            x = 0
            for x in range(0,ct1):

                if unsortedNewtons[i] == selFirstNewtons[x]:
                    position = i + 1                  
                    
                    #Add to output array
                    selFirstIndexNewtons.append(position)
        
        # If small hits because not enough big hits for all bricks then sum the num small hits
        sum1 = 0
        i = 0              
        for i in range(0, firstNewtons):
            # Sum values of remaining Small Hits after Big Hits taken
            sum1 = sum1 + selFirstNewtons[i]

    bigHitsIndex = (str(selLastIndexNewtons).strip('[]').replace(',', ' ').replace('  ', ' '))
    smallHitsIndex = (str(selFirstIndexNewtons).strip('[]').replace(',', ' ').replace('  ', ' '))
    
    totalHits = bigHits + sum1
    return[totalHits],[bigHitsIndex],[smallHitsIndex]    
        
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bigHits = int(input().strip())

    newtons_count = int(input().strip())

    newtons = []

    for _ in range(newtons_count):
        newtons_item = int(input().strip())
        newtons.append(newtons_item)

    result = smashTheBricks(bigHits, newtons)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
