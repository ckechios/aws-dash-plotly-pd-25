# pip install dash

import yfinance as yf
import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback_context # Import callback_context
import plotly.express as px

# df = yf.download("IBM", start="2020-01-01", end="2021-01-01")
# df.to_csv("IBM.csv")

# Assuming IBM.csv is present in the same directory
try:
    df = pd.read_csv("IBM.csv")
except FileNotFoundError:
    print("IBM.csv not found. Downloading data...")
    df = yf.download("IBM", start="2020-01-01", end="2021-01-01")
    df.to_csv("IBM.csv")
    df = pd.read_csv("IBM.csv") # Reload after saving

fig = px.scatter(
    df,
    x="Date",
    y="Close",
)

fig.update_traces(mode="lines")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dash Data Visualization"),
    html.Div("Web application with Dash"),
    dcc.Graph(figure=fig),

    # Dropdown with an ID for callback
    dcc.Dropdown(
        id="location-dropdown",  # Added ID
        options=[
            {"label":"New York", "value": "NY"},
            {"label":"North Carolina", "value": "NC"},
            {"label":"California", "value": "CA"},
        ],
        value="CA"
    ),

    html.Div([
        # RadioItems with an ID for callback
        dcc.RadioItems(
            id="location-radio",  # Added ID
            options=[
                {"label":"New York", "value": "NY"},
                {"label":"California", "value": "CA"},
            ],
            inline=True,
            style={"background":"yellow", "margin":"10px"}
        )
    ], style={"background":"blue", "padding":"10px"}),

    # Div to display the status, with an ID for callback output
    html.Div(id="status-output", style={"margin-top": "20px", "font-size": "20px", "font-weight": "bold"})
])

# Callback to update the status-output div
@app.callback(
    Output("status-output", "children"),  # Output: children of status-output div
    [
        Input("location-dropdown", "value"),  # Input: value from dropdown
        Input("location-radio", "value")      # Input: value from radio buttons
    ]
)
def update_status(dropdown_value, radio_value):
    """
    Updates the status div based on the selected dropdown or radio button value.
    Uses callback_context to determine which input triggered the update.
    """
    triggered_id = callback_context.triggered_id

    if triggered_id == "location-dropdown":
        return f"Selected from Dropdown: {dropdown_value}"
    elif triggered_id == "location-radio":
        return f"Selected from Radio Buttons: {radio_value}"
    else:
        # This handles the initial load of the application.
        # If the dropdown has an initial value, display it.
        # Otherwise, if the radio button has an initial value, display that.
        if dropdown_value is not None:
            return f"Selected from Dropdown: {dropdown_value}"
        elif radio_value is not None:
            return f"Selected from Radio Buttons: {radio_value}"
        else:
            return "No selection yet."

if __name__ == "__main__":
    app.run(debug=True)
