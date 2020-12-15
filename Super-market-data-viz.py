#!/usr/bin/env python
# coding: utf-8
from jupyter_dash import jupyter_dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df_pu=pd.read_csv("df_pu.csv")
fig=px.histogram(df_pu, x="City",y="Sales_pu",histfunc="sum").update_layout(xaxis={'categoryorder':'sum descending'})
y_data=["Sales_pu","Profit_pu","Discount","Quantity"]
x_data=['Ship Mode', 'Segment', 'City', 'State', 'Region', 'Category','Sub-Category']
functions=["sum","min","max","avg"]
app = jupyter_dash.JupyterDash()

app.layout =html.Div([
    html.H1(children=" Interactive Visualization Dashboard",style={"height":"50px","margin-top":"0px","text-align":"center","background":"#adf0ef"}),
    
    html.Div([
    html.H4(children="X_data",style={"margin":"10px","color":"#a5a6b0"}),
    
    dcc.Dropdown(
        id="dropdown0",
        options=[{"label": x, "value": x} 
                 for x in x_data],
        value=functions[:1],

        style={
               "height":"60px",
               "width":"100px",
               "color":"blue",
               "padding":"0px",
               "font-size":"20px",
               "border":None,
               "cursor":"pointer","display":"inline-block"
                
        })],style={"margin-left":"90px","display":"inline-block"}),
    
    
    html.Div([
    html.H4(children="Ydata",style={"margin":"10px","color":"#a5a6b0"}),
    
    dcc.Dropdown(
        id="dropdown1",
        options=[{"label": x, "value": x} 
                 for x in y_data],multi=True,
        value=y_data[:1],

        style={
               "height":"60px",
               "width":"230px",
               "color":"blue",
               "padding":"0px",
               "font-size":"20px",
               "border":None,
               "cursor":"pointer",
                "display":"inline-block",
                
        })],style={"margin-left":"90px","display":"inline-block"}),
    html.Div([
    html.H4(children="Aggregate",style={"margin":"10px","color":"#a5a6b0"}),
    
    dcc.Dropdown(
        id="dropdown2",
        options=[{"label": x, "value": x} 
                 for x in functions],
        
        value=functions[:1],

        style={
               "height":"60px",
               "width":"100px",
               "color":"blue",
               "padding":"0px",
               "font-size":"20px",
               "border":None,
               "cursor":"pointer","display":"inline-block"
                
        })],style={"margin-left":"90px","display":"inline-block"})
    
    #
    
    ,dcc.Graph(id="State_hist",figure=fig)
],style={"border":"2px solid #adf0ef"})

@app.callback(
    Output("State_hist", "figure"), 
    [Input("dropdown0", "value"),
     Input("dropdown1","value"),
    Input("dropdown2","value")])
def update_histogram(x_data,y_data,func):
    fig=px.histogram(df_pu, x=x_data,y=y_data,histfunc=func)
    fig.update_layout(xaxis={'categoryorder':'sum descending'})
    return fig

app.run_server(mode="inline")




