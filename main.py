import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import styles
from dash.dependencies import Input, Output


#llamada a paginas externas
import pages.pregunta1 as pregunta1
import pages.pregunta2 as pregunta2
import pages.pregunta3 as pregunta3
import pages.pregunta4  as pregunta4
import pages.error as error
#admin123

from app import app
from app import server
import pandas as pd
from dataframe import df2

sidebare = html.Div(children=[
    html.H2("Dashboard"),
    html.Hr(),
    dbc.Nav([
        dbc.NavLink('1.Cantidad de Vuelos en el tiempo', href="/", active="exact"),
        dbc.NavLink('2.Cantidad de vuelos por Airline', href="/Airline", active="exact"),
        dbc.NavLink('3.Distancia recorrida y tiempo en el aire', href="/Distancia", active="exact"),
        dbc.NavLink('4.Condiciones climáticas', href="/Clima", active="exact"),
    ],
    vertical=True,
    pills=True)
    ],style=styles.SIDEBAR_STYLE
)

content = html.Div(id="page-content", style=styles.CONTENT_STYLE)

app.layout = html.Div(children=[dcc.Location(id="url"), sidebare, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return pregunta1.content
    elif pathname == '/Airline':
        return pregunta2.content
    elif pathname == '/Distancia':
        return pregunta3.content
    elif pathname == '/Clima':
        return pregunta4.content
    else:
        return error.content


if __name__ == '__main__':
    app.run_server(debug=True)