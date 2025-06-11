from dash import Dash, html, dcc, page_registry, page_container

app = Dash(__name__, use_pages=True)

app.layout = html.Div(
  [
    html.H1("Multipage app"),
    # header
    html.Div([
      html.Div(
        dcc.Link(f"{page['name']}",
                 href=f"{page['path']}")
      ) for page in page_registry.values()
    ]),
    # contents of a route
    page_container,
    # Footer
    html.Hr(),
    html.Div([
      # html.Div("Footer")
      dcc.Link("Home", href="/", style={"marginRight": "10px"}),
      dcc.Link("About", href="About")
    ], style={"position": "absolute",
              "bottom": "10px", 
              "width": "100%",
              "borderTop":"1px solid black"})
  ]
)

if __name__ == "__main__":
  app.run(debug=True)
