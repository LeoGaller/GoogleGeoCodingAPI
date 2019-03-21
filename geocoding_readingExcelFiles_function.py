# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 23:24:38 2018

@author: Leonardo Galler

Program: Google Geocoding API

Function to read a excel file to a dataframe

input: name of file(string), number of rowa to skip of the header
output: Dataframe

"""
import pandas as pd

def readExcel(file,rows):
    print('Reading excel file...\n')
    try:    
        # Reading and saving the data in a dataframe
        excelData = pd.read_excel(file,skiprows=rows)
    except:
        print('It was not possible to read the file!')
        raise
    
    print('Reading excel file...Done!\n')
    return excelData