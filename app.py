from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('formatted_sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

app = Dash(__name__)

colors = {
    'background': '#FFF5F7',
    'text': '#333333',
    'accent': '#E83E8C',
    'card_bg': '#FFFFFF'
}

app.layout = html.Div(
    style={
        'backgroundColor': colors['background'], 
        'padding': '20px', 
        'fontFamily': 'Arial, sans-serif', 
        'minHeight': '100vh'
    }, 
    children=[
    
    html.H1(
        children='Soul Foods: Pink Morsel Sales Visualizer',
        style={
            'textAlign': 'center',
            'color': colors['accent'],
            'padding': '10px',
            'marginBottom': '30px',
            'textShadow': '1px 1px 2px rgba(0,0,0,0.1)'
        }
    ),

    html.Div(
        style={
            'backgroundColor': colors['card_bg'],
            'padding': '20px',
            'borderRadius': '10px',
            'boxShadow': '0 4px 8px rgba(0,0,0,0.1)',
            'width': '60%',
            'margin': '0 auto 30px auto',
            'textAlign': 'center',
            'transition': 'all 0.3s ease-in-out'
        },
        children=[
            html.Label(
                'Filter by Region:', 
                style={'fontWeight': 'bold', 'marginRight': '20px', 'color': colors['text']}
            ),
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': ' All Regions', 'value': 'all'},
                    {'label': ' North', 'value': 'north'},
                    {'label': ' East', 'value': 'east'},
                    {'label': ' South', 'value': 'south'},
                    {'label': ' West', 'value': 'west'}
                ],
                value='all',
                inline=True,
                style={'display': 'inline-block', 'color': colors['text']},
                inputStyle={'margin-right': '5px', 'margin-left': '15px', 'cursor': 'pointer'}
            )
        ]
    ),

    html.Div(
        style={
            'backgroundColor': colors['card_bg'],
            'padding': '20px',
            'borderRadius': '10px',
            'boxShadow': '0 4px 8px rgba(0,0,0,0.1)',
            'margin': '0 auto',
            'width': '90%'
        },
        children=[
            dcc.Graph(
                id='sales-chart',
                animate=True,
                animation_options={
                    'transition': {
                        'duration': 750,
                        'ease': 'cubic-in-out'
                    }
                }
            )
        ]
    )
])

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
        title_text = 'Pink Morsel Sales - All Regions'
    else:
        filtered_df = df[df['Region'] == selected_region]
        title_text = f'Pink Morsel Sales - {selected_region.capitalize()} Region'

    fig = px.line(
        filtered_df,
        x='Date',
        y='Sales',
        color='Region' if selected_region == 'all' else None, 
        title=title_text
    )

    fig.update_layout(
        plot_bgcolor=colors['card_bg'],
        paper_bgcolor=colors['card_bg'],
        font_color=colors['text'],
        title_font_size=22,
        title_x=0.5,
        xaxis_title='Date',
        yaxis_title='Sales ($)',
        xaxis=dict(showgrid=True, gridcolor='#E0E0E0'),
        yaxis=dict(showgrid=True, gridcolor='#E0E0E0'),
        transition_duration=500
    )

    if selected_region != 'all':
         fig.update_traces(line_color=colors['accent'])

    return fig

if __name__ == '__main__':
    app.run(debug=True)