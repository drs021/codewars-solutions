# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:44:35 2021

@author: David Stoneking
"""

"""Stop gninnipS My sdroW!

Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"

spinWords( "This is a test") => returns "This is a test"

spinWords( "This is another test" )=> returns "This is rehtona test"""



def spin_words(sentence):
    count = 1
    each_word = ''
    final_string = ''
    temp = ''
    for each in sentence:
        
        if each != ' ' and not count == len(sentence):
            count += 1
            #print('not a space and not the end of a sentence: ', each )
            #print('count =', count)
            each_word += each
            
        elif each == ' ':
            count += 1
            if len(each_word) < 5:
                final_string += each_word + ' '
                #print('hit a space... current word less than 5:', final_string)
                each_word = ''
            elif len(each_word) >= 5:
                each_word = each_word[::-1]
                final_string += each_word + ' '
                #print('hit a space... current word greater than 5:', final_string)
                each_word = ''
        else:
            each_word += each
            if len(each_word) < 5:
                final_string += each_word
                #print('end of sentence.. current word less than 5:', final_string)
                
            elif len(each_word) >= 5:
                each_word = each_word[::-1]
                final_string += each_word
                #print('end of sentence... current word greater than 5:', final_string)
                
    
    #print('done', final_string)
    return print(final_string)

#spin_words('bigger big welcome cat')
spin_words('Welcome')
