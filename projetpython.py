import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

df = pd.read_csv("bnp_paribas_prices.csv", parse_dates=["Timestamp"])

app = dash.Dash(__name__)

app.layout = html.Div([html.H1("BNP Paribas Price Dashboard"),dcc.Graph(id="time-series-graph"),dcc.Interval(id="interval-component", interval=1 * 1000,  n_intervals=0),] )



app.layout = html.Span(
    [
        html.H1("Crypto Dashboard"),
        dcc.Graph(id="time-series-graph"),
        dcc.Interval(id="interval-component", interval=1 * 1000, n_intervals=0),
    ]
)

@app.callback(Output("time-series-graph", "figure"), Input("interval-component", "n_intervals"))
def update_graph(n):
    df_subset = df.iloc[:n+1, :]
    fig = px.line(df_subset, x="Timestamp", y="Price")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
