# pip install dash

from dash import Dash, dcc, html
import plotly.express as px


app = Dash()

markdown_text="""
# This is an example Markdown

MD text will be rendered
- bullet point 1
- bullet point 2

*italic text*

**Bold text**

[Open Google search](https://google.com)
"""

app.layout = html.Div([
  html.H1("Dash data vizualization"),
  html.Div("Web application with dash"),
  dcc.Markdown(markdown_text),
  
])

if __name__ == "__main__":
  app.run(debug=True)