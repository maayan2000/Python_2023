# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:23:23 2023

@author: efrat
"""

def revword(word:str):
    rev_word = word.lower()[::-1] 
    return rev_word
      

def count_word():
    name = "C:\\Users\\efrat\\OneDrive\\שולחן העבודה\\Python_HWs\\text.txt"
    handle = open(name)
    counter = 1
    l=list()
    for line in handle:
        new_line = line.rstrip().split()
        for j in new_line:    
            l.append(j) #l is a list of all the words in the text file
        word = l[0] #the word "first"
    for w in l[1:]:
        the_word = revword(w)
        if the_word == word:
            counter = counter+1
            
    return counter

print("Number of repetitions of the word first is:" , count_word())



                
            

    

    

    









