#!/bin/python3

import math
import os
import random
import re
import sys
import requests


#
# Complete the 'getPhoneNumbers' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING country
#  2. STRING phoneNumber
# API URL: https://jsonmock.hackerrank.com/api/countries?name=<country>
#

def getPhoneNumbers(country, phoneNumber):
    # Write your code here
    import requests
    import json
    
    url = "https://jsonmock.hackerrank.com/api/countries?name=" + country
    response = requests.get(url)  
    
    codes = []   
    for data in response.json()['data']:  
        codes = (data['callingCodes'])    
        print("codes=",codes)
        x = 0
        ct = len(codes)
        print("len codes=",ct)
        
        #if multiple calling codes returned use the one at highest index 
        if ct > 1:
            codes = codes[ct-1]
 
    strCodes = (str(codes).strip('[]').strip("'"))
    print("codes stripped=",strCodes)

    # Set full output number     
    fullNumber = (str("+" + strCodes + " " + phoneNumber))
    print("fullNumber",fullNumber)

    strOut = (str(fullNumber).strip('[]').strip("'")) 
    print("string Out=",strOut)
    
    # If no data or incomplete return -1
    if strCodes != "" and phoneNumber != "":
        return strOut 
    else:
        return -1   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    country = input()

    phoneNumber = input()

    result = getPhoneNumbers(country, phoneNumber)

    fptr.write(str(result) + '\n')

    fptr.close()
