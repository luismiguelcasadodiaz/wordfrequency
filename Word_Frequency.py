# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:48:14 2022

@author: luism

This script identifies the frecuency of words in a text

This Script receives a parameter the text file to analyse


"""
import sys

def process_file(lines):
    pass
def show_frecuencies(dict):
    pass

if __name__ == "__main__":
    try:
        with open(sys.argv[1]) as f:
            lines = f.readlines()
            frecuencies=process_file(lines)
    except:
        print("File not found")
        
            
