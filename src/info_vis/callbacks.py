from dash import Input, Output
from app import app


@app.callback(
    Output('component_name', 'component_property'),  # function output destination
    Input('component_name', 'component_property'),  # for parm 1
    Input('component_name', 'component_property')  # for param 2
)
def function(param_1, param_2):
    pass