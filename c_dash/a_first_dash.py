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
  dcc.Graph(figure=fig)
])

if __name__ == "__main__":
  app.run(debug=True)