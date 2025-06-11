from dash import html, register_page

register_page(__name__)

layout = html.Div([
  html.H2("Page 1"),
  html.Div("contents of page 1")
])