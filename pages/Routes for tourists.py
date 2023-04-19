
from dash import html , dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash_labs.plugins.pages import register_page
from components.sampledf.dicts_cluster import *

from components.maps.mapcol_departamentos import mapcol_departamentos
from components.maps.mapClusters import mapClusters 
from components.sampledf.functions import get_route


from components.sampledf.model import  df_nspp, df_threatened, df_nendemics, routes_end, routes_nspp, routes_thre, clusters
from components.table.table import table

cluster_total, cluster_ntreat, cluster_endemic, cluster_nspp = dicts_list()

#we declared the routes to see all the birds in general
cluster_0 = cluster_total[0]
cluster_1 = cluster_total[1]
cluster_2 = cluster_total[2]
cluster_3 = cluster_total[3]
cluster_4 = cluster_total[4]
cluster_5 = cluster_total[5]
cluster_6 = cluster_total[6]
cluster_7 = cluster_total[7]

#We declared the routes to see endemic birds
cluster_end_0 = cluster_endemic[0]
cluster_end_1 = cluster_endemic[1]
cluster_end_2 = cluster_endemic[2]
cluster_end_3 = cluster_endemic[3]

#We declared the routes to see threatened birds
cluster_thre_0 = cluster_ntreat[0]
cluster_thre_1 = cluster_ntreat[1]
cluster_thre_2 = cluster_ntreat[2]
cluster_thre_3 = cluster_ntreat[3]

cluster_def = cluster_0
routes = routes_nspp
#cluster_1 = cluster

df_filtrado = clusters[clusters['cluster_total']==0]
list_mun = df_filtrado['COD_DANE'].unique()
lats,lons =  get_route(list_mun, 'driving', df_filtrado)
mapa_rutas = mapcol_departamentos('Best routes to know birds in Colombia', 'div_municipios_fig2',lats, lons)

params2 = {
            'title': 'Number of species', 
            'description': 'List of number of municipalities with max amount of species',
            'columns': ['NOM_DPTO','NOM_MPIO','nspp'],
}
params3 = {
            'title': 'Endemic', 
            'description': 'List of number of municipalities with max amount of endemic species',
            'columns': ['NOM_DPTO','NOM_MPIO','nendemics'],
}
params4 = {
            'title': 'Threatened', 
            'description': 'List of number of municipalities with max amount of threatened species',
            'columns': ['NOM_DPTO','NOM_MPIO','nthreatened'],
}
tabla_datos_2 = table(df_nspp,params2)
tabla_datos_3 = table(df_nendemics,params3)
tabla_datos_4 = table(df_threatened,params4)


register_page(__name__, path="/routesPerDepartment")

layout= html.Div(
    [
        dbc.Row([
            dbc.Col([
                 html.H1("Routes", className='title ml-2'),
            ])
           
        ]),

        html.Div([
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
                    value=['nspp'],
                    multi = False
                )
                ])
            ]),
             dbc.Col([            
                html.Div([
                    html.Div(['Select the route'], className="mb-2  selector-label"),
                    dcc.Dropdown(
                    id="id_selector_route",
                    options= routes,
                    value=['1'],
                    multi = False
                )
                ],id="id_route")
            ]),
            
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Button([
                    'Filtrar'
                ],id="id_filtrar")
                
            ],class_name="d-flex justify-content-end mt-2"),
        ]),

        ],className="card"),
        dbc.Row([
         dbc.Col([
                html.Div([
                    html.Div(['Select the state'], className="mb-2  selector-label"),
                    dcc.Dropdown(
                    id="id_selector_departamento",
                    options= cluster_def,
                    value=['ANTIOQUIA'],
                    multi = False
                )
                ], id= "id_departamento")
                
            ]),
         ],className="card"),
        dbc.Row([
             dbc.Col([html.Div([
                    mapa_rutas.display()  
                ],id="row_map")], className='card')
        ]),

         dbc.Row([
            dbc.Col([
                html.Div([
                    tabla_datos_2.display()
                ],id="row_tabla")   
            ]),
            dbc.Col([
                html.Div([
                    tabla_datos_3.display()
                ],id="row_tabla")   
            ]),
            dbc.Col([
                html.Div([
                    tabla_datos_4.display()
                ],id="row_tabla")   
            ])
        ], className= "card"),

    

    ], className='container-fluid', style={'margin': 'auto', 'width':'100%'}
)  

@callback( Output("id_route", "children"), 
    Input("id_selector_especie", "value"))
def  update_list_of_routes(selector_especie):
    routes = routes_nspp
    if selector_especie == 'nspp':
        routes = routes_nspp
    if selector_especie == 'nendemics':
        routes = routes_end
    if selector_especie == 'nthreatened':
        routes = routes_thre
        
    selector_route =[  html.Div([
                    html.Div(['Select the route'], className="mb-2  selector-label"),
                    dcc.Dropdown(
                    id="id_selector_route",
                    options= routes,
                    value=['1'],
                    multi = False
                )
                ])]
        
    return selector_route
        
    

@callback(
        [Output("row_map", "children"),
         Output("id_departamento","children")],
        [
         State("id_selector_especie","value"),
         State("id_selector_route","value"),
         Input("id_filtrar", "n_clicks"),
                
        ],prevent_initial_call=True
    )
def update_map(selector_especie,selector_route,nclicks):
        df = df_nspp
        cluster_def = cluster_0
        if selector_especie == 'nspp' and selector_route == '1' :
            df = clusters[clusters['cluster_total']==0]
            cluster_def = cluster_0
            
        elif selector_especie == 'nspp' and selector_route == '2' :
            df = clusters[clusters['cluster_total']==1]
            cluster_def = cluster_1
            
        elif selector_especie == 'nspp' and selector_route == '3' :
            df = clusters[clusters['cluster_total']==2]
            cluster_def = cluster_2
            
        elif selector_especie == 'nspp' and selector_route == '4' :
            df = clusters[clusters['cluster_total']==3]
            cluster_def = cluster_3
            
        elif selector_especie == 'nspp' and selector_route == '5' :
            df = clusters[clusters['cluster_total']==4]
            cluster_def = cluster_4
            
        elif selector_especie == 'nspp' and selector_route == '6' :
            df = clusters[clusters['cluster_total']==5]
            cluster_def = cluster_5
            
        elif selector_especie == 'nspp' and selector_route == '7' :
            df = clusters[clusters['cluster_total']==6]
            cluster_def = cluster_6
            
        elif selector_especie == 'nspp' and selector_route == '8' :
            df = clusters[clusters['cluster_total']==7]
            cluster_def = cluster_7
            
        elif selector_especie == 'nendemics'and selector_route == '1' :
            df = clusters[clusters['cluster_n_demic']==0]
            cluster_def = cluster_end_0
            
        elif selector_especie == 'nendemics'and selector_route == '2' :
            df = clusters[clusters['cluster_n_demic']==1]
            cluster_def = cluster_end_1

            
        elif selector_especie == 'nendemics'and selector_route == '3' :
            df = clusters[clusters['cluster_n_demic']==2]
            cluster_def = cluster_end_2
            
        
        elif selector_especie == 'nendemics'and selector_route == '4' :
            df = clusters[clusters['cluster_n_demic']==3]
            cluster_def = cluster_end_3
            
            
        elif selector_especie == 'nthreatened'and selector_route == '1' :
            df = clusters[clusters['cluster_n_tret']==0]
            cluster_def = cluster_thre_0
            
        elif selector_especie == 'nthreatened'and selector_route == '2' :
            df = clusters[clusters['cluster_n_tret']==1]
            cluster_def = cluster_thre_1
            
        elif selector_especie == 'nthreatened'and selector_route == '3' :
            df = clusters[clusters['cluster_n_tret']==2]
            cluster_def = cluster_thre_2
            
        elif selector_especie == 'nthreatened'and selector_route == '4' :
            df = clusters[clusters['cluster_n_tret']==3]
            cluster_def = cluster_thre_3
        
        list_mun = df['COD_DANE'].unique()
        lats,lons =  get_route(list_mun, 'driving', df)
        
        mapa_rutas.lats = lats
        mapa_rutas.lons = lons
        
        nuevo_mapa = mapa_rutas.display()
        
        new_selector = [html.Div(['Select the state'], className="mb-2  selector-label"),
                    dcc.Dropdown(
                    id="id_selector_departamento",
                    options= cluster_def,
                    value=['ANTIOQUIA'],
                    multi = False
                )]
        
        return[nuevo_mapa, new_selector] 
    
            
@callback(Output("row-map","children"),
          
          [State("id_selector_especie","value"),
          Input("id_selector_departamento", "value")])

def update_map(selector_especie, selector_departamento):
        column = 'nspp'
        if selector_especie == 'nspp':
            column = 'nspp'
        if selector_especie == 'nendemics':
            column = 'nendemics'
        if selector_especie == 'nthreatened':
            column = 'nthreatened'
        
        df_filtrado = df[df['NOM_DPTO']==selector_departamento]
        
        mun_list = df_filtrado['COD_DANE'].unique()
        
        if len(mapa_rutas) == 1 :
            nuevo_mapa =  mapClusters('Best routes to know birds in Colombia', 'div_municipios_fig2',df_filtrado,column)
        else:
             lats, lons =  get_route(mun_list, 'driving', df_filtrado)
             mapa_rutas.lats = lats
             mapa_rutas.lons = lons
        
        
        nuevo_mapa = mapa_rutas.display()
        
        return[nuevo_mapa] 
        
        
        
        
       

