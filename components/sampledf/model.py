import pandas as pd
from components.sampledf.functions import *


#import dataframes
df_mun = pd.read_excel('data\dfsample\species_by_municipality.xlsx', engine='openpyxl')
df_consolidated = pd.read_excel('data\dfsample\consolidated_table_byyear.xlsx', engine='openpyxl')
df_eb = pd.read_excel('data\dfsample\ebd_summary_visits.xlsx', engine='openpyxl')
clusters = pd.read_csv('data\dfsample\Clusters_CSV.csv')

#We update the dataframes to make some new we will use

#creating a dataframe with latitude and longitude
coordinates= clusters[['LONGITUDE','LATITUDE','NOM_MPIO']]
df_lat_lon= pd.merge(df_mun, coordinates, how="right", on="NOM_MPIO")




#We sum the observations per department
df_visitors = df_eb.merge(df_mun, how='left', on='NOM_MPIO')
df_eb_new = df_visitors.groupby('NOM_DPTO')['visitors'].sum()
df_copy3 = pd.DataFrame(df_eb_new).reset_index()

#Creating a count of species per municipality
df_copy1 = df_mun.groupby(['NOM_MPIO','NOM_DPTO'])[['nspp','nthreatened','nendemics']].sum().sort_values(by='nspp',ascending = False).reset_index()

df_copy1 = pd.DataFrame(df_copy1).reset_index()
df_copy1 = df_copy1.rename(columns={'nspp':'Number_Of_Species', 'nthreatened':'Threatened_species', 'nendemics':'Endemic_species'})

#Renaming the columns so the names are going to be easy to understand
df_copy2 = df_copy1.drop_duplicates(subset = "NOM_DPTO")

#Creating dataframes with the 5 better municipalities to visit in each department depending on number of species, number of endemic species and number of threatened species
departments = df_lat_lon['NOM_DPTO'].unique()
df_nspp = better_mun_to_visit(df_lat_lon,departments,'nspp')
df_threatened = better_mun_to_visit(df_lat_lon,departments,'nthreatened')
df_nendemics = better_mun_to_visit(df_lat_lon,departments,'nendemics')

#Creating the data to plot some graphs 
observatios_year=df_consolidated.groupby('year')['visitors'].sum()
observatios_year_res=observatios_year.reset_index()

observatios_year_1996=df_consolidated[df_consolidated['year'] >= 1996].groupby('year')['visitors'].sum()
observatios_year_1996_res=observatios_year_1996.reset_index()

#--------------------------------------------
df_spe=df_consolidated[['NOM_MPIO', 'nspp']]
df_spe1=df_spe.drop_duplicates()
df_spe_sort_total=df_spe1.sort_values(by='nspp', ascending=False)
df_spe_sort_total.columns=['Municipality','N_species']

#--------------------------------------------
df_spe_sort=df_spe1.sort_values(by='nspp', ascending=False).head(10)
df_spe_sort.columns=['Municipality','N_species']

routes_nspp = [
                        {"label": "Route 1", "value": "1"},
                        {"label": "Route 2", "value": "2"},
                        {"label": "Route 3", "value": "3"},
                        {"label": "Route 4", "value": "4"},
                        {"label": "Route 5", "value": "5"},
                        {"label": "Route 6", "value": "6"},
                        {"label": "Route 7", "value": "7"},
                        {"label": "Route 8", "value": "8"},
                    ]

routes_end = [
                        {"label": "Route 1", "value": "1"},
                        {"label": "Route 2", "value": "2"},
                        {"label": "Route 3", "value": "3"},
                        {"label": "Route 4", "value": "4"},
                    ]

routes_thre = [
                        {"label": "Route 1", "value": "1"},
                        {"label": "Route 2", "value": "2"},
                        {"label": "Route 3", "value": "3"},
                        {"label": "Route 4", "value": "4"},
                    ]

  
