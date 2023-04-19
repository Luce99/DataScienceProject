#libraries
from turtle import color
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
from dash import html

from callbacks import register_callbacks

# Dash instance declaration
app = dash.Dash(
    __name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.BOOTSTRAP], update_title='Loading...'
)
app.config.suppress_callback_exceptions=True

SIDEBAR_STYLE = {
   "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#aad3df",
}

CONTENT_STYLE = {
    "margin-left": "16rem",
    "background-color": "#aad3df"
}
NAV_STYLE = {
    "margin-left": "16rem",
    "background-color": "#465a93",
    "display": "flex",
    "flex-direction" : "row",
    "align-items" : "center",
}

nav = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo 
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets\DS4A.png", height="60px")),
                    ],
                    align="center",
                    className="g-0",
                ),
                style={"textDecoration": "none"},
            ),
            dbc.Collapse(
                dbc.Row([
                dbc.Col([
                html.H1("Data science for all", className="h1Nav", style={"text-align": "center", "margin-left":"20px"}),]),
                dbc.Col([
                html.H1("MINISTRY OF INFORMATION AND COMUNICATION TECHNOLOGIES", className="h1Nav", style={"text-align": "center"}),
                ]),
                ], style={"align-items":"center"}),
                navbar=True,
            ),
        ],style=NAV_STYLE,
    ),
    
)

navbar =  html.Div(
    [
        html.H4("Menu", className="display-3", style={"color":"#465a93"}),
        html.Hr(),

   dbc.Nav([
            dbc.NavLink(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
    vertical=True,
    pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

#Main layout
content = html.Div(dl.plugins.page_container, style=CONTENT_STYLE)
app.layout = dbc.Container(
    [   nav,
        navbar,
        content,
    ],
    className="dbc",
    fluid=True,
)

# Call to external function to register all callbacks
register_callbacks(app)

# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050, debug=True)