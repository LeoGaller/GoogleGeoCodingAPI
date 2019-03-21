# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 22:45:41 2018

@author: Leonardo Galler

Program to read a csv file get columns and generate a text to be sent to google geocoding
API to retrieve the lat/long data of the address.

steps:
    1 - Read the file
    2 - Create the string to be passed to the API
    3 - Pass the string to the api
    4 - merge the lat/long information to the input data
    5 - generate a new file with the whole data
"""
# Importing libraries and functions
# program that reads excel sheets
import geocoding_readingExcelFiles_function as readExcelF

# program that returns a datafrane with the string of the address
import geocoding_creatingStringWithFields_function as completeAddress

# accessing geocoding API
import geocoding_accessingAPI_function as geo

# import of function responsible to join DFs
import geocoding_merge_df

# importing function to export the data
import geocoding_exporting_file as expo

# Declaring metadata
# Name and location of file
file = 'COMPLETE-NAME-AND-LOCATION-OF-FILE'
local = 'WHERE-THE-OUTPUT-FILE-WILL-BE-LEFT'

# test file with 1 registry
#test_file = 'TEST-LOCATION'
#testfile2 = 'TEST-LOCATION'   
# Number of rows to skip from the header
skip_rows = 9

# Calling the function to read the excel file
excelDF = readExcelF.readExcel(file,skip_rows)

# Calling the function that creates the dataframe that contains the full address
addressDF = completeAddress.createCompleteAddress(excelDF)

# passing the address to the API and handling json
instComLatLong_DF = geo.geocoding(addressDF)

# joining the dataframes
final = geocoding_merge_df.merge_df(excelDF,instComLatLong_DF)

# generating a csv file from the dataframe
expo.output_csv(final,local)

# Ending message
print('Program finished succesfully!')
print('L2 Analytics')
