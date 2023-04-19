import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
from dash import html

register_page(__name__, path="/")

from components.kpi.kpibadge import kpibadge
from components.kpi.kpiplot import kpiplot
from components.table.table import table
#from components.sampledf.model import df_costos
from components.sampledf.model import df_mun
from components.sampledf.model import df_consolidated
from components.maps.mapsample import mapsample



kpi1plot = kpiplot('Total species endemics', df_mun['nendemics'], "79")
kpi2plot = kpiplot('Total species threatened', df_mun['nthreatened'], "72")
kpi3plot = kpiplot('Total species', df_mun['nspp'], "1954")

kpi1 = kpibadge('32', 'Total departments', 'Normal')
kpi2 = kpibadge('870', 'Max number of species in a municipality', 'Normal')
kpi3 = kpibadge('27 ', 'Max number of endemic species in a municipality', 'Normal')
kpi4 = kpibadge('28', 'Max number of threatened species in a municipality', 'Danger')

mapa_ejemplo = mapsample('Number of species in Colombia marked by state', 'id_mapa_ejemplo')

params1 = {
            'title': 'BirdWatching data', 
            'description': 'Table with relevant information about birdWatching',
            'columns': ['NOM_MPIO', 'year', 'visitors', 'nspp', 'nthreatened', 'nendemics']
}
tablaventas = table(df_consolidated,params1)


layout=  dbc.Container(
    [
         dbc.Row([
            dbc.Col([
                 html.H1(['Bird watching in Colombia'], style={'textAlign':'center', 'padding':'20px 0px 20px 30px'}),
                 html.Hr()
            ], lg=12,)],justify="center"),
             dbc.Row([
     dbc.Col([
        html.Div([
        html.Img(src='/assets/hummingbird.png', className= "img")])
    ], md=3,  className = "d-flex align-items-center display-3 justify-content-start"),
     
    dbc.Col([
        dbc.Row([html.P('Colombia is the country with the largest diversity of birds in the world, with over more than 1,950 species representing almost 20% of total bird diversity worldwide. Bird sightseeing promotes sustainable tourism since it promotes ecosystem protection, conservation, and growth of species. These kinds of practices and economic development possibilities offer Colombia in its post-conflict a competitive advantage in terms of promoting tourism and economic growth due to these activities. Birdwatching has the potential to be an emerging industry because the different Colombian advantages such as biodiversity, landscapes, and cultural richness are magnets for national and international tourists.')])
    ], md=6, className = "d-flex display-4 align-self-center flex-column align-items-end"),
   
    dbc.Col([
        html.Div([
        html.Img(src='/assets/parrot.png',  className= "img")])
    ], md=3,  className = "d-flex align-items-center display-3 justify-content-end"),
]),
       dbc.Row([
            dbc.Col([
                kpi1plot.display()
            ], className='card'),
              dbc.Col([
                kpi2plot.display()
            ], className='card'),
             dbc.Col([
                kpi3plot.display()
            ], className='card'),
        ]),    
        dbc.Row([
            dbc.Col([
                mapa_ejemplo.display()


            ], md=8), 
            dbc.Col([
                dbc.Row([
                    dbc.Col([ kpi1.display()]),
                    dbc.Col([ kpi2.display()])
                ]),
                dbc.Row([
                    dbc.Col([ kpi3.display()]),
                    dbc.Col([ kpi4.display()])
                ]),
            ]), 
        ]),
        dbc.Row([
            dbc.Col([
                tablaventas.display()
            ], className='card')
        ])
        
      
    ]
)  