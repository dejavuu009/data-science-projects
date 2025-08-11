from dash import Dash, dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd



def fetch_financial_data(company='AMZN'):
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')

df = fetch_financial_data()
df.reset_index(inplace=True)
df = df[df.Date > '2019-01-01']
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app =Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([

    html.H4('Amazon'),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Scatter(
                    x=df.Date,
                    y=df.Close,
                    mode='lines',
                    fill='tozeroy',
                    name='Amazon'
                )
            ],
            layout=go.Layout(
                yaxis_type='log',
                height=500,
                title_text='price graph',
                showlegend=True
            )
        )
    ),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=df.Date,
                    y=df.Volume,
                    name='volume',
                )
            ],
            layout=go.Layout(
                yaxis_type='log',
                height=300,
                title_text='graph volume',
                showlegend=True
            )
        )
    )
])

if __name__ == "__main__":
    app.run(debug=True)