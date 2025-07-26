#Logística: Otimização de Rotas e Tempos de Entrega
#Objetivo: Analisar o tempo médio de entrega por região, detectar gargalos logísticos e simular melhorias.

import numpy as np

# Tempo de entrega (dias) para 5 regiões × 30 dias
entregas = np.random.randint(1, 15, size=(5, 30))  # Regiões × Dias

# Média de entrega por região
media_por_regiao = np.mean(entregas, axis=1)

# Detectar entregas críticas (>12 dias)
criticas = np.where(entregas > 12)

# Simular melhoria na região 

import numpy as np

# Tempo de entrega (dias) para 5 regiões × 30 dias
entregas = np.random.randint(1, 15, size=(5, 30))  # Regiões × Dias

# Média de entrega por região
media_por_regiao = np.mean(entregas, axis=1)

# Detectar entregas críticas (>12 dias)
criticas = np.where(entregas > 12)

# Simular melhoria na região com maior média
regiao_pior = np.argmax(media_por_regiao)
entregas[regiao_pior] = np.maximum(entregas[regiao_pior] - 2, 1)

# Novo tempo médio após ajuste
nova_media = np.mean(entregas, axis=1)