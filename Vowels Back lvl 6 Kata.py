# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:29:59 2021

@author: David Stoneking
"""

"""Vowels Back
You need to play around with the provided string (s).

Move consonants forward 9 places through the alphabet. If they pass 'z', start again at 'a'.

Move vowels back 5 places through the alphabet. If they pass 'a', start again at 'z'. For our Polish friends this kata does not count 'y' as a vowel.

Exceptions:

If the character is 'c' or 'o', move it back 1 place. For 'd' move it back 3, and for 'e', move it back 4.

If a moved letter becomes 'c', 'o', 'd' or 'e', revert it back to it's original value.

Provided string will always be lower case, won't be empty and will have no special characters.
"""


def vowel_back(st):
    temp = ''
    abcs_3times = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    # use abc's three times and then use the middle as a substring - then cycling through a/z is no problem
    vowels_code = 'aeioucd'# vowels plus cd to account for 'code'
    #print(abcs_3times[26:52].index('a')) # check that substring is correctly indexed a-z
    for ea in st:
        if ea == 'c': # based on rules: if 'c', convert to 'b'
            #print('letter is c, move back 1 to b')
            temp += 'b'
            #print('current temp:',temp)
        elif ea == 'o': # based on rules: if 'o', convert to 'n'
            #print('letter is o, move back 1 to n')
            temp += 'n'
            #print('current temp:',temp)
        elif ea == 'd' or ea == 'e': # if d or e, convert to a
            #print('letter is d or e, move back to a')
            temp += 'a'
            #print('current temp:',temp)
        elif ea not in vowels_code: # if the letters aren't in aeiou or code
            #print(ea,'letter is not in aeiou or code')
            if abcs_3times[abcs_3times[26:52].index(ea)+9] in 'code': # if new letter is in 'code', don't convert, leave the same
                #print('new letter',abcs_3times[abcs_3times[26:52].index(ea)+9],'is in code, revert to',ea)
                temp += ea
                #print('current temp is:',temp)
            else: #otherwise, convert to new letter 9 spaces ahead
                #print(ea,'current ea is in aeiou or code')
                temp += abcs_3times[abcs_3times[26:52].index(ea)+9]
                #print('current temp is:',temp)
        elif abcs_3times[abcs_3times[26:52].index(ea)-5] in 'code': # if new letter is in 'code', don't convert, leave the same
            #print('new letter ',abcs_3times[abcs_3times[26:52].index(ea)-5],' is in code - revert to original ea')
            temp += ea
            #print('current temp is:',temp)
        else:
            temp += abcs_3times[abcs_3times[26:52].index(ea)-5]
    
        
    print(temp)
    
        return(temp)

vowel_back("testcase")
vowel_back("codewars")
vowel_back("exampletesthere")



