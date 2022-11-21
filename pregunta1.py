import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import styles
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import sqlalchemy

import config
from app import app
from app import server
from dataframe import df2



conteo_vuelos = df2.groupby(["month"], as_index=False)["origin"].count()

origen = df2['origin'].unique()
fig = go.Figure([go.Scatter(x=conteo_vuelos['month'], y=conteo_vuelos['origin'])])
fig.update_traces(marker_color='#78c2ad')



content = html.Div([html.H4('Cantidad de vuelos en el tiempo (serie temporal)'),
                       html.Br(),
                       dcc.Graph(id='time-series-chart', figure=fig)])

