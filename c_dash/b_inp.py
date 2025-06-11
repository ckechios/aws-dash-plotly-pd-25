# pip install dash

import yfinance as yf
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# df = yf.download("IBM", start="2020-01-01", end="2021-01-01")
# df.to_csv("IBM.csv")

df = pd.read_csv("IBM.csv")

fig = px.scatter(
  df,
  x="Date",
  y="Close",
)

fig.update_traces(mode="lines")

app = Dash()

app.layout = html.Div([
  html.H1("Dash data vizualization"),
  html.Div("Web application with dash"),
  dcc.Graph(figure=fig),
  dcc.Dropdown(
    options=[
      {"label":"New York", "value": "NY"},
      {"label":"North Carolina", "value": "NC"},
      {"label":"California", "value": "CA"},
    ],
    value="CA"
  ),

  html.Div([
    dcc.RadioItems(
      options=[
        {"label":"New York", "value": "NY"},   
        {"label":"California", "value": "CA"},   
      ],
      inline=True,
      style={"background":"yellow", "margin":"10px"}
    )
  ], style={"background":"blue", "padding":"10px"})

])

if __name__ == "__main__":
  app.run(debug=True)