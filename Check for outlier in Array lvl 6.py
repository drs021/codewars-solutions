# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:54:54 2021

@author: David Stoneking
"""

"""You are given an array (which will have a length of at least 3, 
but could be very large) containing integers. The array is either entirely 
comprised of odd integers or entirely comprised of even integers except for 
a single integer N. Write a method that takes the array as an argument and 
returns this "outlier" N."""


def find_outlier(integers):
    even_count = 0
    odd_count = 0
    
    for each in integers:
        if each % 2 == 0:
            #print('1st Loop found an even:',each)
            even_count += 1
        else:
            odd_count += 1
            #print('1st Loop found an ODD:', each)
    if even_count > odd_count:
        for each in integers:
            if each % 2 != 0:
                #print('2nd Loop found the only ODD:', each)
                return each
    else:
        for each in integers:
            if each % 2 == 0:
                #print('3rd Loop found the only EVEN:',each)
                return each

# Sample Tests
find_outlier([2, 4, 6, 8, 10, 3]) # should be 3
find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) # should be 11
find_outlier([160, 3, 1719, 19, 11, 13, -21]) # should be 160

