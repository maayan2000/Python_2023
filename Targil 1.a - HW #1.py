# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:41:40 2023

@author: efrat
"""

def my_func(x1,x2,x3):
    if not isinstance(x1, float) or not isinstance(x2, float) or not isinstance(x3, float):
        if type(x1) == int or type(x2) == int or type(x3) == int:
            print ("Error: parameters should be float")
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

print(my_func(0.0,5.0,8))
#print(type(my_func(0.0,5.0,1.0)))

