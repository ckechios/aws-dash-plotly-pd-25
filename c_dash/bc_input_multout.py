# pip install dash

import yfinance as yf
import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback_context
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
        id="location-dropdown",
        options=[
            {"label":"New York", "value": "NY"},
            {"label":"North Carolina", "value": "NC"},
            {"label":"California", "value": "CA"},
        ],
        value="CA" # Initial value for dropdown
    ),

    html.Div([
        # RadioItems with an ID for callback
        dcc.RadioItems(
            id="location-radio",
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

# Callback to update the status-output div, dropdown, and radio buttons
@app.callback(
    Output("status-output", "children"),
    Output("location-dropdown", "value"), # Output: value of dropdown
    Output("location-radio", "value"),    # Output: value of radio buttons
    [
        Input("location-dropdown", "value"),
        Input("location-radio", "value")
    ]
)
def update_status_and_components(dropdown_value, radio_value):
    """
    Updates the status div, dropdown, and radio buttons based on the selected input.
    Synchronizes the dropdown and radio button values and updates the status div.
    """
    triggered_id = callback_context.triggered_id
    radio_options_values = [opt["value"] for opt in app.layout["location-radio"].options]

    # Initialize return values
    status_text = "No selection yet."
    new_dropdown_value = dropdown_value
    new_radio_value = radio_value

    if triggered_id == "location-dropdown":
        status_text = f"Selected from Dropdown: {dropdown_value}"
        new_dropdown_value = dropdown_value # Keep dropdown value as is
        # If dropdown value is one of the radio options, update radio
        if dropdown_value in radio_options_values:
            new_radio_value = dropdown_value
        else:
            # If dropdown value is not in radio options (e.g., "NC"),
            # clear the radio selection or keep its current valid state.
            # Setting to None will deselect the radio button if it was previously selected.
            new_radio_value = None

    elif triggered_id == "location-radio":
        status_text = f"Selected from Radio Buttons: {radio_value}"
        new_radio_value = radio_value # Keep radio value as is
        new_dropdown_value = radio_value # All radio options are valid dropdown options

    else:
        # Initial load of the application
        if dropdown_value is not None:
            status_text = f"Selected from Dropdown: {dropdown_value}"
            new_dropdown_value = dropdown_value
            if dropdown_value in radio_options_values:
                new_radio_value = dropdown_value
            else:
                new_radio_value = None # Clear radio if initial dropdown value isn't in radio options
        elif radio_value is not None:
            status_text = f"Selected from Radio Buttons: {radio_value}"
            new_radio_value = radio_value
            new_dropdown_value = radio_value
        else:
            status_text = "No selection yet."
            new_dropdown_value = None
            new_radio_value = None

    return status_text, new_dropdown_value, new_radio_value

if __name__ == "__main__":
    app.run(debug=True)
