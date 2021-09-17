#!/bin/python3

import math
import os
import random
import re
import sys

#return a STRING.
#input is INTEGER.
year = 1918


def dayOfProgrammer(year):
    allyear = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year >= 1700 and year <= 1917:
        if year %4 == 0:
            allyear[1]=29
    

    elif year >= 1918 and year <= 2700:
        if year == 1918:
            allyear[1]=15
        if year % 400==0 or (year %4 == 0 and year % 100 != 0):
            allyear[1]=29
        
    day =0
    for index,each in enumerate(allyear):
        if (day < 256):
            day += each
        elif day == 256:
            return str(each) + "." + str(index+1)+ "." + str(year)
        else:
            d = 256 -  (day - allyear[index-1])
            if index <10:
                return str(d) + ".0" + str(index) + "." + str(year)
            else:
                return str(d) + "." + str(index) + "." + str(year)
            
print(dayOfProgrammer(year))