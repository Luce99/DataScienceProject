import pandas as pd
import json

import urllib.request

def better_mun_to_visit(df,departments,column):
    
    df_5_best = pd.DataFrame(columns=['NOM_MPIO', 'NOM_DPTO','COD_DANE','Longitud','Latitud',column])
    for i in departments :
        new_df = df.query("NOM_DPTO== @i")
        new_df1 = new_df.groupby(['NOM_MPIO','NOM_DPTO','COD_DANE','LONGITUDE','LATITUDE'])[column].sum().sort_values(ascending = False).reset_index()
        new_df1 = pd.DataFrame(new_df1)
        new_df1 = new_df1.drop_duplicates(subset = "NOM_MPIO")
        
        new_df1 = new_df1[0:5]
        
        df_5_best = pd.concat([df_5_best, new_df1], axis=0)
   
    return df_5_best

def get_location(COD_DANE, df):
        row = df[df["COD_DANE"] == COD_DANE]
        lat = row.iloc[0]['LATITUDE']
        lon = row.iloc[0]['LONGITUDE']
        
        return lat, lon

def map_locations(listOfMunicipalities, df):
    coordinates = []
    list25 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    contador = 1
    Coordinates2 = ""
    Coordinates3 = ""
    newCoordinatesList = []
    newCoordinatesList2 = []
    newCoordinatesList3 = []

    
    while contador < len(listOfMunicipalities):
    
        if contador <= 24 :
            lat, lon = get_location(listOfMunicipalities[contador-1], df)
            if (lat != 0.0) & (lon != 0.0):
                Coordinates2 += str(lon)+","
                Coordinates2 += str(lat)+"; "
            contador+= 1
        elif contador % 25 == 0:
            newCoordinates = ""
            for a in list25:
                lat, lon = get_location(listOfMunicipalities[contador-2], df)
                if (lat != 0.0) & (lon != 0.0):
                    newCoordinates += str(lon)+","
                    newCoordinates += str(lat)+"; "
                contador += 1
                
            newCoordinates = newCoordinates[:-2] 
            newCoordinatesList=newCoordinates.split(' ')    
            coordinates.append(newCoordinatesList)
            
        else :
            lat, lon = get_location(listOfMunicipalities[contador-2], df)
            if (lat != 0.0) & (lon != 0.0):
                    Coordinates3 += str(lon)+","
                    Coordinates3 += str(lat)+"; "
            contador += 1
        
        
    if (len(Coordinates2)!= 0):
        Coordinates2 = Coordinates2[:-2]
        newCoordinatesList2=Coordinates2.split(" ")
        coordinates.append(newCoordinatesList2) 
    
    if (len(Coordinates3)!= 0):
        Coordinates3 = Coordinates3[:-2]
        newCoordinatesList3=Coordinates3.split(" ")
        coordinates.append(newCoordinatesList3) 
    return coordinates

def get_route(lisOfMunicipalities, travelling_mode, df):
    coordinates = map_locations(lisOfMunicipalities, df)
    lons = []
    lats = []
    CurrentCoordinates = ""
    for fila in coordinates:
        for i in fila:
            CurrentCoordinates += i
                    
        mapurl = 'https://api.mapbox.com/directions/v5/mapbox/' + str(travelling_mode) + '/' + str(CurrentCoordinates) + '?alternatives=true&continue_straight=true&geometries=geojson&language=en&overview=full&steps=true&access_token=' + str("pk.eyJ1IjoibHVjZXJvbW9qaWNhOTkiLCJhIjoiY2w0em9tMXEyM2FvbTNkcGF0OWV5cTczZiJ9.BJ1jmbnaVcb36xG-PiKgKg")
        openmap = urllib.request.urlopen(mapurl)
        mapjs = json.load(openmap)
              
                
        for ks in mapjs['routes']:
            for k, v in ks.items():
                if k == 'geometry':
                    for eachk, eachv in v.items():
                        if eachk == 'coordinates':
                            for eachloc in eachv:
                                lons.append(eachloc[0])
                                lats.append(eachloc[1])
        lats.sort()
        lons.sort()
            
        return lats,lons
