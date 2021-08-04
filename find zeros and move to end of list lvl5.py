# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:29:59 2021

@author: David Stoneking
"""
# Check out: https://careerkarma.com/blog/python-isalpha-isnumeric-isalnum/

#INSTRUCTIONS:
# """Write an algorithm that takes an array and moves all of the zeros 
# to the end, preserving the order of the other elements."""

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(array):
    #count = 0
    temp_list = []
    zero_list = []
    for each in array: # loop through the array
        if each != 0: # is it not equal to 0
            temp_list.append(each) # then add it to a temp list
        if each == 0: # if it is equal to zero
            if str(each) == 'False': # first check to make sure it isn't a False which technically equals 0
                temp_list.append(each) # add any False values to the temp list
            else: 
                zero_list.append(0) # otherwise it must be a 0, so add a 0 to the zero_list
                
    temp_list.extend(zero_list) # merge the two temp lists 
    #print(temp_list)
    return(temp_list)
        
        
#move_zeros([False,1,0,1,2,0,1,3,"a"])
move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9])
#move_zeros([1,2,0,1,0,1,0,3,0,1])