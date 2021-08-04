# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 13:22:49 2021

@author: David Stoneking
"""

# Problem Statement:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

# Courtesy of projecteuler.net

def solution(number):
    temp = 0
    for ea in range(0,number): # check each number b/n 0 and number given
        if ea % 3 == 0 or ea % 5 == 0: # modulus to check divisibility by 3 or 5
            temp += ea # if yes, add to running tally in temp
    return(temp)