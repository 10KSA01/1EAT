import dash
from dash import html, dcc
from components import overview

dash.register_page(__name__, path='/login')

layout = html.Div(children=[overview.Get_overview()])


