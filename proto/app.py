from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc
from authlib.integrations.flask_client import OAuth
from components import navbar
from dotenv import find_dotenv, load_dotenv
from os import environ as env
from flask import Flask, redirect, render_template, session, url_for
from urllib.parse import quote_plus, urlencode

external_stylesheets = [dbc.themes.BOOTSTRAP,
                        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
                        dbc.icons.BOOTSTRAP]

app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app.server.secret_key = env.get("APP_SECRET_KEY")
oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)

@app.server.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")

@app.server.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@app.server.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

app.layout = html.Div([
    navbar.navbar,
	dash.page_container
])

if __name__ == '__main__':
	app.run_server(debug=False, port=3000)