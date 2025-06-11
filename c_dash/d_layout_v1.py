from dash import Dash, html
import plotly.express as px

# Local file does not work
  # './d_local_bWLwgP.css',
  
# external_stylesheets = [] # what ever is in assets dire is attached automatically
# This wont work - The file needs to be in ./assets/ dash serves all staic files from here
# external_stylesheets = [
#   "./d_local_bWLwgP.css",
# ]

# As shown in official tutorial: https://dash.plotly.com/tutorial
external_stylesheets = [
  'https://codepen.io/chriddyp/pen/bWLwgP.css',
]

app = Dash(__name__,
           external_stylesheets=external_stylesheets)

app.title="Layout with Dash"

app.layout = ([
  # Add title
  # html.Title("Layout with Dash"),

  # row 1
  html.Div([
    html.H1("Layout visualization")
  ], className="navtop",
      style={"background": "yellow"}),

  # row 2 - with 2 columns
  html.Div([
    # col 1
    html.Div([
      html.H2("Row 1 : Column Left"),
      html.Div("Text for this column")
    ], className="six columns custbg"),
    # col 2
    html.Div([
      html.H2("Row 1 : Column Right"),
      html.Div("Right column content")
    ], className="columns six"),

  ], className="row"),

  # row 3

])

if __name__ == "__main__":
  app.run(debug=True)
