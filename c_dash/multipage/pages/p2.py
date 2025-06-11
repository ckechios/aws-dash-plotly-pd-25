from dash import html, register_page

register_page(__name__)

layout = html.Div([
  html.H2("Page 2"),
  html.Div("contents of page 2")
])