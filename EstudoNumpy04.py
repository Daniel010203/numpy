import dash
from dash import html, dcc
import plotly.graph_objs as go
import numpy as np

# Dados fictícios (vendas de 5 vendedores de segunda a sábado)
vendas = np.array([
    [62000, 58000, 61000, 60500, 59000, 60000],
    [57000, 64000, 58000, 61000, 62000, 63000],
    [55000, 56000, 57000, 58000, 56000, 59000],
    [60000, 65000, 67000, 68000, 66000, 69000],
    [58000, 59000, 60000, 61000, 62000, 63000]
])

dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']
meta = 60000

app = dash.Dash(__name__)

# Gráfico interativo
fig = go.Figure()
for i in range(vendas.shape[0]):
    fig.add_trace(go.Scatter(
        x=dias,
        y=vendas[i],
        mode='lines+markers',
        name=f'Vendedor {i+1}'
    ))

fig.add_shape(
    type='line',
    x0=0,
    y0=meta,
    x1=5,
    y1=meta,
    line=dict(color='red', dash='dash'),
    name='Meta'
)
fig.update_layout(title='Desempenho de Vendas por Dia',
                  xaxis_title='Dia',
                  yaxis_title='Vendas (R$)',
                  hovermode='x unified')

# Layout do app
app.layout = html.Div([
    html.H1('Dashboard Interativo de Vendas'),
    html.P('Análise por dia da semana para os 5 melhores vendedores'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)