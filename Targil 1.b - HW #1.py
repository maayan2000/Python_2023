# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:23:23 2023

@author: efrat
"""

name = "C:\\Users\\efrat\\OneDrive\\שולחן העבודה\\Python_HWs\\text.txt"
handle = open(name)

def revword(word:str):
    rev_word = word.lower()[::-1] 
    return rev_word
      

def count_word():   
    counter = 0
    l=list()
    for line in handle:
        new_line = line.rstrip()
        l.append(new_line) #l is a list of the lines in the text file
        word = l[0] #the word "first"
        for w in new_line.split():
            if w==word:
                 counter = counter+1
            else:
                the_word = revword(w)
                if the_word == word:
                    counter = counter+1
                
    print("Number of repetitions of the word first is:",counter)
count_word()            

    

    

    









