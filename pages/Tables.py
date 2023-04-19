import dash
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page


from components.table.table import *
from components.sampledf.model import df_copy1, df_copy2

data = df_copy1
data2 = df_copy2


register_page(__name__, path="/tables")

params1 = {
            'title': 'Departments', 
            'description': 'Information per department',
            'columns': ['NOM_DPTO','Number_Of_Species','Threatened_species','Endemic_species']
}

params2 = {
            'title': 'Municipalities', 
            'description': 'Information per municipality',
            'columns': ['NOM_MPIO','Number_Of_Species','Threatened_species','Endemic_species']
            
}




tablaDepartamentos = table(data2,params1)
tablaMunicipios = table(data, params2)

layout= dbc.Container([
     dbc.Row([
            dbc.Col([
                 html.H1(['Data'], style={'textAlign':'center'}),
                 html.Hr()
            ], lg=12,)],justify="center"),
    dbc.Row([
        dbc.Col([         
            tablaDepartamentos.display()
        ])
    ], className= "card"),
    dbc.Row([
        dbc.Col([
            tablaMunicipios.display()
        ])
    ], className= "card"),
])