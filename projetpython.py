import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Replace these dummy data with your actual time series data.
data = {
    "date": pd.date_range(start="2022-01-01", periods=60, freq="D"),
    "price": [10000 + i * 50 for i in range(60)],
}

df = pd.DataFrame(data)

app = dash.Dash(__name__)

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
    fig = px.line(df_subset, x="date", y="price")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)