# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 23:41:40 2018

@author: Leonardo Galler

TO create a string based on some columns from the DF

input: dataframe
return: tuples with 'NOME INSTITUIÇÃO' and 'ENDERECO_COMPL'
"""
import pandas as pd
def createCompleteAddress(dataframe):
    print('Creating complete address!\n')
    # trimming the text objects
        # Step 1: locate the text objects of the dataframe
    df_text = dataframe.select_dtypes(['object'])
    
    print('Treating the text!')
        # Step 2: Applying the function to trim the columns
    dataframe[df_text.columns] = df_text.apply(lambda x: x.str.strip())
    dataframe2 = dataframe.copy()
        # now, to replace spaces by plus signs
    df_text = dataframe2.select_dtypes(['object'])
    dataframe2[df_text.columns] = df_text.apply(lambda x: x.str.replace(' ','+'))
    
    print('Treating the text! Done!\n')
    
    # slicing the DF
    print('Creating the new dataframe with the address')
    try:
        # creating a new dataframe with the needed info
        part1_df = pd.DataFrame({'ENDERECO': dataframe2['ENDEREÇO'].map(str)+'+'+dataframe2['BAIRRO'].map(str)+'+'+dataframe2['CEP'].map(str)+'+'+dataframe2['MUNICÍPIO'].map(str)+'+'+dataframe2['UF'].map(str),'NOME INSTITUIÇÃO': dataframe['NOME INSTITUIÇÃO']})
        
        # droping NaN values
        part1_df.dropna()
        
        # return dataframe with no NaN values
        print('Creating the new dataframe with the address! Done!\n')
        print('Creating complete address! Done!\n')
        return part1_df
    
    except ValueError:
        print('Error when trying to create the dataframe! \n please verify if the name of the columns are like these: CNPJ,NOME INSTITUIÇÃO, ENDEREÇO, COMPLEMENTO, BAIRRO, CEP,MUNICÍPIO, UF')