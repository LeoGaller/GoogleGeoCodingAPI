# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 22:45:37 2018

@author: Leonardo Galler


Function to access the Geocoding API from Google Maps Services.

input: dataframe or list with the string of the address to search
output: lat/long of the address

basic url structure:
https://maps.googleapis.com/maps/api/geocode/json?address=YOUR_ADDRESS_HERE&components=country:COUNTRY_CODE_HERE&key=YOUR_API_KEY
Example:
    https://maps.googleapis.com/maps/api/geocode/json?address=AVENIDA+INTERNACIONAL,+1806+CENTRO+17780-000+LUCELIA+SP&key=AIzaSyDeXudwJeccDE5ibOZtjxL1PaK_j4wItAY

    *** For filtering the URL you can use components por estado, for example:
    If we use        administrative_area:DF , it will look for states

        
"""
def geocoding(dataframe):
    # pandas
    import pandas as pd
    
    # Library to handle web requests
    import requests 

    # library to make the program wait a few time to ask again for more data
    import time
    
    print('Starting the process to access the API')
    
    # parameters for the web request

    GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    # metadata for the operation
    API_KEY = 'AIzaSyDeXudwJeccDE5ibOZtjxL1PaK_j4wItAY'

    # creating a new dataframe with the lat/long information
    latLong_DF = pd.DataFrame({'NOME INSTITUIÇÃO': dataframe['NOME INSTITUIÇÃO']})
    latLong_DF['lat']=0
    latLong_DF['lng']=0
    
    
    # Controlling the index
    print('Sending data to google!')
    index = 0
    for item in dataframe['ENDERECO']:
        # create the URL
        URL = GOOGLE_MAPS_API_URL+item+'&key='+API_KEY
        
        # calling the API

        try:
            req = requests.get(URL,headers={'User-Agent':'L2_bots_GeocodingAPI (leolacerdagaller@live.com)'})
            res = req.json()
        except:
            print('ERROR: It was not possible to make the request!')
         
        try:
            # Use the first result
            result = res['results'][0]
         
            # inserting data to the new df
            latLong_DF.loc[index:,'lat'] = str(result['geometry']['location']['lat'])
            latLong_DF.loc[index:,'lng'] = str(result['geometry']['location']['lng'])
        except:
            # If it cant find the lat/long give zero to anyone
            latLong_DF.loc[index:,'lat'] = 0
            latLong_DF.loc[index:,'lng'] = 0
            
        
        # iterating
        index += 1
        
        # wait before making the new request
        time.sleep(0.10)
        
    print('Sending data to google! Done!\n')
    
    return latLong_DF