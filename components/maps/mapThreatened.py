from dash import html , dcc
import plotly.express as px
from components.sampledf.model import df_mun
import json



class mapThreatened:    
    """A class to represent a samplemap of Montreal Elections"""        
    def __init__(self,map_title:str,ID:str):
        """__init__
        Construct all the attributes for the sample map
     
        Args:
            map_title (str): _Title for the map_
            ID (str): _div id to specify unique #id with callbacks and css_
        
        Methods:

        display()
            Function to display a sample map with no arguments, uses plotly express data.
            
            Arguments:
                None

            Returns:
                html.Div : A Div container with a dash core component dcc.Graph() inside
        """
        
        self.map_title = map_title
        self.id = ID

    @staticmethod
    def figura():
         df= df_mun
         
         with open('data/jsonmaps/colombia.geo.json', encoding='utf-8') as json_file:
            departamentos = json.load(json_file)
         for i, each in enumerate(departamentos["features"]):
            departamentos["features"][i]['id']=departamentos["features"][i]['properties']['DPTO']

         fig = px.choropleth(data_frame=df, 
                    geojson=departamentos, 
                    locations='NOM_DPTO', # nombre de la columna del Dataframe
                    featureidkey='properties.NOMBRE_DPT',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    color='nthreatened', #El color depende de las cantidades
                    color_continuous_scale=px.colors.sequential.Viridis
                   )
         fig.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")  
         annotations = [
            dict(
                showarrow=False,
                align="right",
                text="",
                font=dict(color="#000000"),
                bgcolor="#f9f9f9",
                x=0.95,
                y=0.95,
            )
        ]
         fig.update_layout(
            geo_scope='south america',
            mapbox_style="carto-positron",
            mapbox_zoom=5.8, 
            mapbox_center = {"lat": 6.88970868, "lon": -74.2973328},
            annotations=annotations,
            height=400),
         fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
         return fig
         

    def display(self):
       
        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=self.figura())
                ])
                
            ],id=self.id
        )
        return layout

