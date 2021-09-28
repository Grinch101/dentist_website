import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def updater(fig=None, title='TITLE', xaxistitle='x title', yaxistitle='y title', font='Arial', fontsize=12):
    Config = {
        'displayModeBar': True,
        'displaylogo': False,
        "fillFrame": False,
        'scrollZoom': True,
        'modeBarButtonsToAdd': ['drawline',
                                'drawopenpath',
                                'drawclosedpath',
                                'drawcircle',
                                'drawrect',
                                'eraseshape'
                                ]
    }
    if fig is not None:
        fig.layout = {'font': {'color': 'black', 'family': font, fontsize: 12},
                  'legend': {'title': {'text': 'Legend Title'}},
                  'margin': {'b': 10, 'l': 10, 'r': 10, 't': 51},
                  'template': 'ggplot2',
                  'legend': {'title': {'text': 'Legend Title'}},
                  'title': {'font': {'size': 18}, 'text': title},
                  'xaxis': {'rangeslider': {'visible': False}, 'title': {'text': xaxistitle}, 'type': 'linear'},
                  'yaxis': {'rangeslider': {'visible': False}, 'title': {'text': yaxistitle}, 'type': 'linear'},
                  'transition_duration': 500}
    return fig, Config


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app = dash.Dash(__name__)
a, config = updater()
app.layout = html.Div([
    dcc.Graph(id='graph-with-slider', config=config),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)
    # fig, config = updater(fig, title='test')
    fig.layout = {
    'legend': {'itemsizing': 'constant', 'title': {'text': 'continent'}, 'tracegroupgap': 0},
    'margin': {'t': 30,'l':2},
    'template': 'ggplot2',
    'transition': {'duration': 500},
    'xaxis': {'anchor': 'y', 'domain': [0.0, 1.0], 'title': {'text': 'gdpPercap'}, 'type': 'log'},
    'yaxis': {'anchor': 'x', 'domain': [0.0, 1.0], 'title': {'text': 'lifeExp'}}
    }

    return fig


if __name__ == '__main__':
    app.run_server(debug=False)