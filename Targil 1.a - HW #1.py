# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:41:40 2023

@author: efrat
"""

# The assignment was not clear, so I assumed:
#  1. If the function received Int it will return "Error: parameters should be float",
#  2. In any other situation that the fuction didn't receive only Float numbers - it will return NONE.
#  3. If all the numbers are Float - it will make sure that the denominator is not zero, and return the desired answer

def my_func(x1,x2,x3):
    if not isinstance(x1, float) or not isinstance(x2, float) or not isinstance(x3, float):
        if type(x1) == int or type(x2) == int or type(x3) == int:
            return ("Error: parameters should be float")
        else:
            return None
 
    else:
        numerator = (x1+x2+x3)*(x2+x3)*x3
        denominator = x1+x2+x3
        if denominator == 0:
            print("Not a number – denominator equals zero")
        else: 
            value = numerator/denominator 
            return value

print(my_func(0.0,5.5, "gfdgd"))
