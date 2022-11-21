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


gf = df2.groupby(["month"])["temp"].sum()
gf = pd.DataFrame(gf)
gf.reset_index(inplace=True)


gf1 = df2.groupby(["month"])["humid"].sum()
gf1 = pd.DataFrame(gf1)
gf1.reset_index(inplace=True)

gf2 = df2.groupby(["month"])["wind_speed"].sum()
gf2 = pd.DataFrame(gf2)
gf2.reset_index(inplace=True)

fig = go.Figure()
fig.add_traces(go.Scatter( x=gf['month'], y=gf['temp'],
                    mode='lines',
                    name='temp',
                    line_shape='linear'))
fig.add_trace(go.Scatter(x=gf1['month'], y=gf1['humid'],
                    mode='lines',
                    name='humid'))
fig.add_trace(go.Scatter(x=gf2['month'], y=gf2['wind_speed'],
                    mode='lines',
                    name='wind_speed'))
                    


content = html.Div([html.H4("Condiciones climáticas"),
                    html.Br(),                    
                    dcc.Graph(id='graph', figure=fig) ])