# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:59:02 2021

@author: David Stoneking
"""

"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""



def sum_two_smallest_numbers(numbers):
    numbers.sort() # sorts the list ascending
    #print(numbers) # test print
    return numbers[0] + numbers[1] # the first two numbers will be the lowest.. sum up.. DONE