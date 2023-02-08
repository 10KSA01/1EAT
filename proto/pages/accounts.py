import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc033f97aeefcb38b6b3f8fb0cc4569db"
# Your Auth Token from twilio.com/console
auth_token  = "5e0f17b5bb7bf7e7bd9ffac39f47cb3b"

flag = False
client = Client(account_sid, auth_token)

dash.register_page(__name__)

number = "+447444585915"
name = "Kumar"

layout = html.Div(children=[
    html.H1(children='Account Settings'),
    html.Div(["Hi ", name]),
	html.Div([
        "Number: ",
         dcc.Input(
            id="number-input",
            type="text",
            placeholder="add your number",

        )
    ]),
    html.Button("Submit", id="button", n_clicks=0),
    html.Div(id='button-clicks')

])

@callback(
    Output('button-clicks', 'children'),
    Input('button', 'n_clicks'))
def clicks(n_clicks):
    global flag
    if n_clicks > 0:
        flag = True
        msg = client.messages.create(
        to= number, 
        from_="+18584805084",
        body="Thank you for adding your number to 1EAT!") 
        print(msg)
        return msg
    else:
        print("Hello")
        return ""
