from dash import html
import dash_bootstrap_components as dbc
from components.maps.mapcol_municipios import mapcol_municipios
from dash_labs.plugins.pages import register_page
from dash import html , dcc, callback, Input, Output, State
import plotly.graph_objects as go
import json

from components.sampledf.model import df_nspp, df_threatened, df_nendemics



mapa_colombia_municipios = mapcol_municipios('Map of Colombian municipalities with max number of species', 'id_figura_mapa_colombia',df_nspp, 'nspp')

register_page(__name__, path="/mapa_municipios")

layout= html.Div(
    [
        dbc.Row([
            dbc.Col([
                 html.H1("Map of Colombian municipalities with max number of species", className='title ml-2'),
            ]),
        ]),
         dbc.Row([
              dbc.Col([            
                html.Div([
                    html.Div(['Select the filter'], className="mb-2  selector-label"),
                    dcc.Dropdown(
                    id="id_selector_especie",
                    options=[
                        {"label": "All species", "value": "nspp"},
                        {"label": "Endemics", "value": "nendemics"},
                        {"label": "Threatened", "value": "nthreatened"},
                    ],
                    value=['All species'],
                    multi = False
                )
                ])
            ]),
        ],className="card"),
         dbc.Row([
             dbc.Col([html.Div([
                    mapa_colombia_municipios.display()  
                ],id="map")], className='card')
        ]),
    ], className='container-fluid', style={'margin': 'auto', 'width':'100%'}
)

@callback(
        Output("map", "children"), 
        Input("id_selector_especie","value"))

def update_map(selector_especie):
        df = df_nspp
        column ="nspp"
        if selector_especie == 'nspp':
            df = df_nspp
            column = 'nspp'
        elif selector_especie == 'nendemics':
            df = df_nendemics
            column = 'nendemics'
        elif selector_especie == 'nthreatened':
            df = df_threatened
            column = 'nthreatened'
        
        with open ('./data/jsonmaps/MunicipiosColombia.json', encoding='utf-8') as json_file:
            municipios = json.load(json_file)
        
        mapa_colombia_municipios.df = df
        mapa_colombia_municipios.column = column
        
        nuevo_mapa = mapa_colombia_municipios.display()

        
        return [nuevo_mapa]
