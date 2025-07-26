#Segurança do Trabalho: Análise de Acidentes e Prevenção
#Objetivo: Mapear acidentes por setor, identificar padrões críticos e simular impactos de medidas preventivas.

import numpy as np

# Acidentes: 10 setores × 12 meses × 3 tipos (queda, corte, choque)
acidentes = np.random.poisson(lam=5, size=(10, 12, 3))

# Total por setor
total_setor = np.sum(acidentes, axis=(1, 2))

# Setor com maior risco
risco_setor = np.argmax(total_setor)

# Simular medidas de segurança com redução de 20% nos acidentes
acidentes[risco_setor] = (acidentes[risco_setor] * 0.8).astype(int)

# Comparação antes/depois
novo_total = np.sum(acidentes, axis=(1, 2))
impacto = total_setor[risco_setor] - novo_total[risco_setor]