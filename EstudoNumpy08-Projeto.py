#Comércio Varejista de Atacado: Análise de Vendas e Estoque
#Objetivo: Identificar produtos com maior giro, sazonalidade nas vendas e prever reabastecimento.


import numpy as np  
# Vendas de 20 produtos em 12 meses
vendas = np.random.randint(100, 1500, size=(20, 12))

# Produto mais vendido no ano
total_anual = np.sum(vendas, axis=1)
mais_vendido = np.argmax(total_anual)

# Média mensal geral
media_mensal = np.mean(vendas, axis=0)

# Detecção de sazonalidade (desvio padrão elevado)
sazonalidade = np.std(vendas, axis=1)
produtos_sazonais = np.where(sazonalidade > 300)[0]

# Estimativa de estoque necessário p/ próximo mês
estoque_minimo = np.max(vendas[:, -3:], axis=1)