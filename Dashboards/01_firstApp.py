from dash import Dash, dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd




app = Dash(__name__)
app.layout = html.Div([
    html.H2("Hello, world!"),
    dcc.Graph(figure=go.Figure([
        go.Bar(
            x=[2017, 2018, 2019],
            y=[150, 180, 220],
            name= 'local'
        ),
        go.Bar(
            x=[2017, 2018, 2019],
            y=[70, 160, 240],
            name= 'remote'
        )
    ]))
])

if __name__ == "__main__":
    app.run(debug=True)
