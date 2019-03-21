# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 23:49:18 2018

@author: Leonardo Galler

Receives a dataframe and the local where the original excel file is and export the new data there.

input: dataframe and location
output: csv file at the same location

"""
from datetime import date
today = date.today()

def output_csv(dataframe, local):
    print('Exporting the dataframe to csv!')
    # Defining the name of the file
    file_name = local+str(today)+'COOPERATIVAS.csv'
    
    # Exporting the dataframe to csv
    dataframe.to_csv(file_name, sep=';', encoding='cp1252')
    print('Exporting the dataframe to csv! Done!')