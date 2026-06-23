from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('formatted_sales_data.csv')

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

app = Dash(__name__)

fig = px.line(
    df, 
    x='Date', 
    y='Sales', 
    color='Region',
    title='Pink Morsel Sales Trends'
)

fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Sales ($)'
)

app.layout = html.Div(children=[
    html.H1(
        children='Soul Foods: Pink Morsel Sales Visualizer', 
        style={'textAlign': 'center'}
    ),
    dcc.Graph(
        id='sales-visualizer-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)