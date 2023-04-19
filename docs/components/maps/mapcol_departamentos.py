from dash import html , dcc
import plotly.graph_objects as go
          
class mapcol_departamentos:
    """A Class to represent a map of Colombia with two Layers, one for Municipios and 
    the second one for markers as overlay
    
    based in json file of 
    https://www.kaggle.com/code/alfredomaussa/colombia-municipios/notebook?scriptVersionId=39794627
    
    Towns codes available in
    https://www.dane.gov.co/files/censo2005/provincias/subregiones.pdf

    """
    def __init__(self,map_title:str, ID:str,lats, lons):
        """__init__ _summary_

        Args:
            map_title (str): Titulo del mapa, html H4 element
            ID (str): css id to use with callbacks
            df (_type_): dataframe with info to use in choropleth
            markers (_type_): small point as overlay in map
        """        
        self.map_title = map_title 
        self.id = ID
        self.lats = lats
        self.lons = lons 

 
    @staticmethod
    def figura(self):
        map = go.Scattermapbox(
        lat=self.lats,
        lon=self.lons,
        mode='lines',
        line=dict(width=2),
        marker=dict(
            size=5,
        ),
        #text='{} to {} : {}'.format(str('home').title(), str('dest').title(), str('travelling_mode').title()),
        #hoverinfo='text'
    )
        fig = go.Figure(data=map)
        fig.update_layout(
                    geo_scope='south america',
                    mapbox_style="carto-positron",
                    mapbox_zoom=5.5, 
                    mapbox_center = {"lat": 4.570868, "lon": -74.2973328},
                    #annotations= marker,
                    height=1000),

                
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                
        return fig


    def display(self):   
        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=mapcol_departamentos.figura(self), id=self.id)
                ])
                
            ]
        )
        return layout
            
        
    