"""
Trying dash bootstrap

pip install dash-bootstrap-components

"""

from dash import Dash, html
import dash_bootstrap_components as dbc

app=Dash(__name__,
         external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
  html.Div([
    html.Div("First Item 1", className="h1 bg-light"),
    html.Div("Second Item"),
    html.Div("Third Item"),
  ], className="hstack gap-3 mt-3")
)

if __name__ == "__main__":
  app.run(debug=True)
