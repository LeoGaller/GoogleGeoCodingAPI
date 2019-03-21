# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 23:10:41 2018

@author: Leonardo Galler

Function to receive two dataframes and merge/join them to present the institution with lat/long

input: 2 dataframes without lat/long
output: 1 dataframe with lat/long

"""
def merge_df(data_complete,data_latLong):
    import pandas as pd
            
    print('Merging data!')
    # merging dfs
    merged = data_complete.merge(data_latLong,on='NOME INSTITUIÇÃO')
    print('Merging data! Done!\n')
    return merged