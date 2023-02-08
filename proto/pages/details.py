import dash
from dash import html
from components import detail

dash.register_page(__name__, path="/details")

layout = html.Div(children=[detail.Get_Details()])