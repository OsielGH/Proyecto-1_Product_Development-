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


at = df2.groupby(["month"])["air_time"].sum()
at = pd.DataFrame(at)
at.reset_index(inplace=True)

at1 = df2.groupby(["month"])["distance"].sum()
at1 = pd.DataFrame(at1)
at1.reset_index(inplace=True)

fig = go.Figure()
fig.add_traces(go.Scatter( x=at['month'], y=at['air_time'],
                    mode='lines',
                    name='air_time',
                    line_shape='linear'))
fig.add_trace(go.Scatter(x=at1['month'], y=at1['distance'],
                    mode='lines',
                    name='distance'))


content = html.Div([html.H4('Distancia recorrida y tiempo en el aire'),
                    html.Br(),                    
                    dcc.Graph(id='graph', figure=fig) ])