from dash import html, register_page

register_page(__name__, path="/")

layout = html.Div([
  html.H2("Home page"),
  html.Div("contents of home page")
])