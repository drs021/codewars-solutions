# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:42:11 2021

@author: David Stoneking
"""

"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
"""



def is_isogram(string):
    tally = []
    string = string.upper()
    print(string)
    for ea in string:
        if ea in tally:
            return False
        else:
            tally.append(ea)
    return True

is_isogram('Blab')