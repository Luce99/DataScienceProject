#libraries
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
from dash_labs.plugins.pages import register_page
from components.sampledf.functions import *
import plotly.express as px
from components.sampledf.model import observatios_year_res, observatios_year_1996_res, df_spe_sort_total, df_spe_sort


# dash-labs plugin call, menu name and route
register_page(__name__, path="/graphbars")

#First bar graph
first_bar = px.bar(observatios_year_res, x='year', y='visitors', color="visitors", title="Number of visitors by year in Colombia")


#Second bar graph
second_bar = px.bar(observatios_year_1996_res, x='year', y='visitors', color="visitors", title="Number of visitors by year in Colombia considering the most relevant years")

#Third bar graph
third_bar = px.bar(df_spe_sort_total, x='Municipality', y='N_species', color="N_species",  title="Total number of species by Municipality")

#fourth bar graph

fourth_bar = px.bar(df_spe_sort, x='Municipality', y='N_species', color="N_species",  title="Top 10 of the number of municipalities with the highest number of species")

# specific layout for this page
layout = dbc.Container(
    [    dbc.Row([
            dbc.Col([
                 html.H1(['Bar plots'], style={'textAlign':'center'}),
                 html.Hr()
            ], lg=12,)],justify="center"),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='bargraph',
                         figure= first_bar)

            ], lg=12), 
             dbc.Col([
                dcc.Graph(id='bargraph',
                         figure= second_bar)

            ], lg=12),
              dbc.Col([
                dcc.Graph(id='bargraph',
                         figure= third_bar)

            ], lg=12),
               dbc.Col([
                dcc.Graph(id='bargraph',
                         figure= fourth_bar)

            ], lg=12),
           
        ]),
        ]
)