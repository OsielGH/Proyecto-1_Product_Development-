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


df4=pd.DataFrame({'count' : df2.groupby( ['carrier', 'month'] ).size()}).reset_index()
df5 = df4.pivot("carrier", "month", "count")

fig = px.imshow(df5, text_auto=True)



content = html.Div([html.H4('Cantidad de vuelos por Airline'),
                    html.Br(),                    
                    dcc.Graph(id='graph', figure=fig) ])





