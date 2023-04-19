from dash_labs.plugins.pages import register_page
from components.maps.mapEndemics import mapEndemics
from components.maps.mapThreatened import mapThreatened
from components.maps.mapsample import mapsample
from components.maps.mapObservations import mapObservations
import dash_bootstrap_components as dbc

register_page(__name__, path="/heatmaps")

from dash import  dcc, html, Input, Output, callback
import plotly.express as px

#Create the maps 
map = mapThreatened('Number of threatened species marked by state', 'id_mapa_threatened')

mapa_2 = mapEndemics('Number of endemic species marked by state', 'id_mapa_endemics')

mapa_3 = mapsample('Number of species marked by state', 'id_mapa_ejemplo')

mapa_4 = mapObservations('Summatory of observations marked by state', 'id_mapa_observations')

layout = [html.Div([
               dbc.Row([
            dbc.Col([
                 html.H1(['Maps'], style={'textAlign':'center'}),
                 html.Hr()
            ], lg=12,)],justify="center"),
                dbc.Row([
            dbc.Col([
                mapa_3.display()
            ], md=6),
            dbc.Col([
                mapa_4.display()
            ], md=6),]),
                dbc.Row([
            dbc.Col([
                map.display()
            ], md=6),
            dbc.Col([
                mapa_2.display()
            ], md=6),]),
                 ])]


