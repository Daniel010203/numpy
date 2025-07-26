#Corretagem de Imóveis: Análise de Mercado e Comissões
#Objetivo: Estimar comissões, analisar volume de vendas por zona e prever tendências de preço.

import numpy as np

# Vendas mensais: 6 zonas × 12 meses
vendas = np.random.randint(10, 100, size=(6, 12))

# Preço médio por imóvel por zona
precos = np.random.normal(loc=350000, scale=50000, size=(6,))

# Comissões por zona (5%)
comissoes = vendas * precos[:, np.newaxis] * 0.05

# Zona com maior faturamento
faturamento = np.sum(comissoes, axis=1)
zona_top = np.argmax(faturamento)

# Tendência de crescimento: calcular variação média mês a mês
variacao_mensal = np.diff(vendas, axis=1)
tendencia = np.mean(variacao_mensal, axis=1)