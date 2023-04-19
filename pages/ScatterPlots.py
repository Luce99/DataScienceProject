#libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
import plotly.express as px
from dash import dcc
from dash import html , dcc, callback, Input, Output, State
from components.sampledf.model import df_mun

# dash-labs plugin call, menu name and route
register_page(__name__, path="/scatterplots")


#scatter plots

#third scatter plot
fig3 = px.scatter(df_mun, x="nspp", y=["nthreatened","nendemics"], color_discrete_sequence=["red", "green"], labels= {"nspp":"Number of species", "nendemics":"Endemic", "nthreatened":"Threatened"})


#third scatter plot
new_df = df_mun[["area_km","nspp","nthreatened","nendemics"]]
pairplot = px.scatter_matrix(new_df,
    dimensions=["area_km","nspp","nthreatened","nendemics"], height= 600)


# specific layout for this page
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                 html.H1(['Scatter Plots'],id="div_title_maps", style={'textAlign':'center'}),
                 html.Hr()
            ], lg=12), 
           
        ],justify="center"),

        dbc.Row([
             dbc.Col([
                dcc.Graph(id='scatter-plot'),
                html.P("Filter by number of species:"),
             dcc.RangeSlider(
                id='range-slider',
                min=200, max=800, step=100,
                marks={200: '200', 800: '800'},
                value=[200, 600]
            ),], md=6),
            dbc.Col([
                dcc.Graph(id='scatter-plot-2'),
                html.P("Filter by number of species:"),
            dcc.RangeSlider(
                id='range-slider-2',
                min=200, max=800, step=100,
                marks={200: '200', 800: '800'},
                value=[300, 500]
            ),], md=6),
             ],justify="center"),
        html.H2('Overlap of both endemic and threatened',
                        style={'textAlign':'center'}),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='scatter-plot-3'),
                html.P("Filter by number of species:"),
             dcc.RangeSlider(
                id='range-slider-3',
                min=200, max=800, step=100,
                marks={200: '200', 800: '800'},
                value=[200, 800]
            ),], md=6),],justify="center", style={"background-color":"white"}),
         html.H2('Correlation between numerical variables',
                        style={'textAlign':'center'}),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='scatterplot',
                         figure= pairplot, style={"background-color":"white"})], md= 8,)
             ],justify="center", style={"background-color":"white"})

        
    ]
)
@callback(
    Output("scatter-plot", "figure"), 
    Input("range-slider", "value"))

def update_bar_chart(slider_range):
    df = df_mun 
    low, high = slider_range
    mask = (df['nspp'] > low) & (df['nspp'] < high)
    fig = px.scatter(
        df[mask], x="nspp", y="nendemics", color_discrete_sequence=["green"],  labels= {"nspp":"Number of species", "nendemics":"Endemic"} )
    fig.update_layout(title ="Endemic")
    return fig

@callback(
    Output("scatter-plot-2", "figure"), 
    Input("range-slider-2", "value"))

def update_bar_chart(slider_range):
    df = df_mun 
    low, high = slider_range
    mask = (df['nspp'] > low) & (df['nspp'] < high)
    fig = px.scatter(
        df[mask], x="nspp", y="nthreatened", color_discrete_sequence=["red"], labels= {"nspp":"Number of species", "nthreatened":"Threatened"} )
    fig.update_layout(title ="Threatened")
    return fig

@callback(
    Output("scatter-plot-3", "figure"), 
    Input("range-slider-3", "value"))

def update_bar_chart(slider_range):
    df = df_mun 
    low, high = slider_range
    mask = (df['nspp'] > low) & (df['nspp'] < high)
    fig = px.scatter(
        df[mask], x="nspp", y=["nthreatened","nendemics"], color_discrete_sequence=["red","green"] )
    fig.update_layout(title ="Threatened and Endemic")
    return fig
