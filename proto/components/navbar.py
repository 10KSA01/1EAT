from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# from app import app
from dash_iconify import DashIconify


MAIN_LOGO = "assets\logo.png"

logo = dbc.Row(
    [
        dbc.Col(html.Img(src=MAIN_LOGO, height="30px"), width={"order":0})
    ],
    align="left",
    className="g-0",
)


switchers = dbc.Row(
    [
        dbc.Col(dcc.Link(dbc.Button("Overview"), href="/" )),
        dbc.Col(dbc.Label(" | ")),
        dbc.Col(dcc.Link(dbc.Button("Details"), href="/details" )),
    ],
    align="left",
    className="g-0",
)

buttons = dbc.Row(
    [
        dbc.Col(dcc.Link(DashIconify(
        icon="ic:outline-account-circle",
        width=30,
        color="white"
    ), href="/accounts")),
          dbc.Col(width=20),
        dbc.Col(DashIconify(
                icon="ant-design:setting-outlined",
                width=30,
                color="white" 
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Col(logo, align="left", width="auto"),
            dbc.Col(switchers, align="center", width="auto"),
            dbc.Col(buttons,align="right", width="auto"),
        ]
    ),
    color="dark",
    dark=True,
)

# # add callback for toggling the collapse on small screens
# @app.callback(
#     Output("navbar-collapse", "is_open"),
#     [Input("navbar-toggler", "n_clicks")],
#     [State("navbar-collapse", "is_open")],
# )
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open