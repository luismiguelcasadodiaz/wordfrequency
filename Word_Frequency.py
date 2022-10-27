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
    pass
def show_frecuencies(dict):
    pass

if __name__ == "__main__":
    try:
        my_directory = os.getcwd()
        print(my_directory)
        my_file = os.path.join(my_directory, sys.argv[1])
        print(my_file)
        with open(my_file,'r') as f:
            lines = f.readlines()
            frecuencies=process_file(lines)
    except:
        print("File not found")
        
            
