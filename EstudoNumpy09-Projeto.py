#Hospital: Monitoramento de Pacientes Internados
#Objetivo: Analisar sinais vitais, tempo médio de internação e detectar padrões anômalos.

# Sinais vitais: 500 pacientes × 7 dias × 3 variáveis (PA, frequência, temperatura)
import numpy as np


dados = np.random.normal(loc=[120, 80, 37], scale=[10, 8, 0.5], size=(500, 7, 3))

# Média dos sinais por paciente
media_vitais = np.mean(dados, axis=1)

# Identificação de pacientes com temperatura >38°C
febre = np.where(dados[:, :, 2] > 38)

# Tempo médio de internação por setor (simulado)
internacoes = np.random.randint(3, 15, size=500)
media_internacao = np.mean(internacoes)

# Filtragem de casos críticos: PA < 90 e temperatura > 38.5
criticos = np.where((dados[:, :, 0] < 90) & (dados[:, :, 2] > 38.5))