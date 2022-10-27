# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:48:14 2022

@author: luism

This script identifies the frecuency of words in a text

This Script receives a parameter the text file to analyse


"""
import sys
import os

def process_file(lines):
    word_frecuency = {}
    for line in lines:
        for palabra in line.strip().split():
           if palabra not in word_frecuency:
               word_frecuency.setdefault(palabra,1)
           else:
               word_frecuency[palabra] += 1

    return word_frecuency        
            
def show_frecuencies(mydict):
    res = {val[0] : val[1] for val in sorted(mydict.items(), key = lambda x: (x[0], x[1]))}

    for k,v in res.items():
        print (k,":",v)
    

if __name__ == "__main__":
    my_directory = os.getcwd()
    print(my_directory)
    my_file = os.path.join(my_directory, sys.argv[1])
    print(my_file)
    with open(my_file,encoding='utf-8') as f:
         lines = f.readlines()
         frecuencies=process_file(lines)
         show_frecuencies(frecuencies)

        
            
