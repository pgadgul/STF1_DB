import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output 

import requests 
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd

@app.route("/")
def index():
    return "Hello,world!"

df = pd.read_csv('2020-01-28T10_37_27-05_00_SEN_Hk_tlm_t.csv')

# remove rows if the column value is out of range[set_minimum, set_maximum]
def remove_outliers(df,column_string,set_maximum,set_minimum):
        dataframe = df[df[column_string] > set_minimum]
        dataframe = dataframe[dataframe[column_string] < set_maximum]
        return dataframe
df_temp = remove_outliers(df,'TEMP_0',500,-500)
TEMP_0_ro = df_temp['TEMP_0'].values.tolist()
fig=plt.plot(TEMP_0_ro)

app = dash.Dash() 

server = app.server

app.layout = html.Div([
    dcc.Graph(id="graph", figure=fig),
    html.A(
        html.Button("Download HTML"), 
        id="download",
        href="data:text/html;base64," + encoded,
        download="plotly_graph.html"
    )
])


if __name__ == '__main__': 
    app.run_server(debug=True)

