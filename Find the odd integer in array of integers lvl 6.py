# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:52:14 2021

@author: David Stoneking
"""

"""Find the odd int
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

"""

def find_it(seq):
    for i in seq:  # cycle through each integer
        if seq.count(i) % 2 == 1: # modulus to check if odd
            return(i)
        
        
        