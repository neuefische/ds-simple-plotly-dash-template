import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


################################################################################
# APP INITIALIZATION
################################################################################
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# this is needed by gunicorn command in procfile
server = app.server


################################################################################
# PLOTS
################################################################################
LEGEND = ["clicks", "go fish!"]
SCORES = [0.1, 0.1]


def get_figure(legend, scores):
    return go.Figure(
        [go.Bar(x=legend, y=scores)],
        layout=go.Layout(template="simple_white"),
    )


fig = get_figure(LEGEND, SCORES)

################################################################################
# LAYOUT
################################################################################
app.layout = html.Div(
    [
        html.H2(
            id="title",
            children="Neuefische Interactive Dash Plotly Dashboard",
        ),
        html.H3(
            id="subtitle",
            children="Add some fish text and click, and the chart will change",
        ),
        html.Div(children="Add some text you want (less than 10 characters)!"),
        dcc.Textarea(
            id="textarea-state-example",
            value="",
            style={"width": "100%", "height": 100},
        ),
        html.Button("Submit", id="textarea-state-example-button", n_clicks=0),
        html.Div(id="textarea-state-example-output", style={"whiteSpace": "pre-line"}),
        dcc.Graph(id="bar-chart", figure=fig),
    ]
)

################################################################################
# INTERACTION CALLBACKS
################################################################################
# https://dash.plotly.com/basic-callbacks
@app.callback(
    [
        Output("textarea-state-example-output", "children"),
        Output("bar-chart", "figure"),
    ],
    Input("textarea-state-example-button", "n_clicks"),
    State("textarea-state-example", "value"),
)
def update_output(n_clicks, value):
    fig = get_figure(LEGEND, SCORES)
    if n_clicks > 0:
        if 0 < len(value) < 10:
            text = "you said: " + value
            scores = [0.1 * n_clicks, 0.1]
            fig = get_figure(LEGEND, scores)
            return text, fig
        else:
            return "Please add a text between 0 and 10 characters!", fig
    else:
        return "", fig


# Add the server clause:
if __name__ == "__main__":
    app.run_server()
