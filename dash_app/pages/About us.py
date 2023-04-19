from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
from dash_labs.plugins.pages import register_page
from components.sampledf.functions import *
import plotly.express as px
from components.markdown.markformat import markformat


# dash-labs plugin call, menu name and route
register_page(__name__, path="/aboutUs")

file1 = open('./data/mdsamples/story1.md')
file2 = open('./data/mdsamples/story2.md')

texto1  = markformat('OUR MISSION', file1.read())
texto2  = markformat('OUR HISTORY', file2.read())

layout=  dbc.Container(
    [
         dbc.Row([
            dbc.Col([
                 html.H1(['Bird watching in Colombia TEAM-228'], style={'textAlign':'center', 'padding':'20px 0px 20px 30px'}),
                 html.Hr()
            ], lg=12,)],justify="center"),
            dbc.Col([
                texto1.show()
            ]),
            dbc.Col([
                texto2.show()
            ]),
            dbc.Row([
             dbc.Col([
        html.Div([
        html.Img(src='/assets/tablaTEAM.png', className= "img")],style={"background-color":"white"})
    ], md=12,  className = "d-flex align-items-center display-5 justify-content-center"),],style={"background-color":"white"})
            
                
    ])
    
