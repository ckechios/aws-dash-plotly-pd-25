"""
https://dash.plotly.com/external-resources#usage

rows, cols, css, graph, dangerHTML, dropdown, upd graph fig
Added: 
  dropdown to choose stock
  update fig
  error for file not found
"""

# import dash_core_components as dcc
import pandas as pd
from dash import html, dcc, Output, Input, dash_table
import dash
import plotly.express as px

# As shown in official tutorial: https://dash.plotly.com/tutorial
external_stylesheets = [
  "https://codepen.io/chriddyp/pen/bWLwgP.css",
  "./assets/b_stylesheet.css",
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# print(df.head())


def update_graph(stockname: str) -> list[pd.DataFrame, px.scatter]:
  try:
    df = pd.read_csv(f"{stockname}.csv")
  except FileNotFoundError:
    df = pd.DataFrame()
    raise Exception(f"File not found: {stockname}.csv")

  fig = px.scatter(
      df,
      x="Date",
      y="Close",
  )
  fig.update_traces(mode="lines")
  return df, fig

first_stock = "IBM"
df, fig = update_graph(first_stock)

app.layout = html.Div(
  [
    # Row 1
    html.Div([
      html.H1("Dash Data Visualization"),
    ], className="row center",
        style={"textAlign": "center"}),
    
    # Row 2
    html.Div([
        html.Div([
          html.H2("Chose Data"),
          html.Div("""
                   The dropdown below allows you to choose a stock from the 
                   csv's present. Stocks availabele are GOOGL, IBM etc.
                   """),
          dcc.Dropdown(
              id="stock-dropdown",
              options=[
                  {"label": "RACE", "value": "RACE"},
                  {"label": "GOOGL", "value": "GOOGL"},
                  {"label": "IBM", "value": "IBM"},
                  {"label": "AAPL", "value": "AAPL"},
              ],
              value=first_stock,
              clearable=False,
          ),

        ], className="six columns custbg"
        ),

        html.Div([
            html.H2("Graph of above"),
            dcc.Graph(id="stock-graph", figure=fig),
            html.Div("Some other content"),
        ],
            className="six columns"),
    ], className="row"),

    html.Div("Status: ---",id="status-msg"),

    # Row 3 - table
    html.Div([
        html.H4("The Data Head"),
        # html.Div(df.head().to_html()),
        dash_table.DataTable(
          id="stock-table",
          data=df.to_dict("records"),
          page_size=10
        )

    ], className="row txtctr"),
  ]
)

@app.callback(
  Output("stock-graph", "figure"),
  Output("stock-table", "data"),
  Output("status-msg", "children"),
  Input("stock-dropdown", component_property="value"),
)
def update_fig(stockname):
  print(f"symbol: {stockname}")
  try:
    df, fig = update_graph(stockname)
    message = f"Status: Update Graph for {stockname}"
  except Exception as e:
    df = pd.DataFrame()
    fig = px.scatter(df)
    message = f"Error: {str(e)}"
  return fig, df.to_dict("records"), message

if __name__ == "__main__":
  app.run(debug=True)
