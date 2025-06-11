import dash_bootstrap_components as dbc
from dash import Input, Output, State, html, Dash

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

ctr = 1

modal = html.Div(
    [
        dbc.Button("Open modal", id="open", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Header")),
                dbc.ModalBody("This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ]
)

stack = html.Div(
    [
        html.Div("First item", className="bg-light border mt-5"),
        html.Div(f"Counter: {ctr}", id="ctr-dsp", className="bg-light border"),
        html.Div("Third item", className="bg-light border"),
        modal,
    ], className="vstack gap-3"
)

app.layout = dbc.Container(stack)


@app.callback(
    Output("modal", "is_open"),
    Output("ctr-dsp", "children"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
  global ctr

  ctr = ctr + 1
  clicked = f"Clicked: {ctr} times"
  if n1 or n2:
    return not is_open, clicked
  return is_open, clicked


if __name__ == "__main__":
  app.run(debug=True)
