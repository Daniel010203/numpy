import numpy as np
import matplotlib.pyplot as plt

# Dados fictícios: vendas dos 5 vendedores (de 2ª a sábado)
# Cada linha representa um vendedor, cada coluna um dia da semana
vendas = np.array([
    [62000, 58000, 61000, 60500, 59000, 60000],  # Vendedor 1
    [57000, 64000, 58000, 61000, 62000, 63000],  # Vendedor 2
    [55000, 56000, 57000, 58000, 56000, 59000],  # Vendedor 3
    [60000, 65000, 67000, 68000, 66000, 69000],  # Vendedor 4
    [58000, 59000, 60000, 61000, 62000, 63000]   # Vendedor 5
])

dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
meta = 60000

# Total de vendas por vendedor
vendas_totais = np.sum(vendas, axis=1)

# Comissão padrão (5%)
comissao_padrao = vendas_totais * 0.05

# Verifica quem bateu a meta em pelo menos um dia
bateu_meta_por_dia = vendas >= meta
bateu_meta_geral = np.any(bateu_meta_por_dia, axis=1)

# Aplica comissão dobrada (10%) para os que bateram a meta
comissao_final = np.where(bateu_meta_geral, vendas_totais * 0.10, comissao_padrao)

# Visualização gráfica
for i in range(vendas.shape[0]):
    plt.plot(dias, vendas[i], marker='o', label=f'Vendedor {i+1}')

plt.axhline(meta, color='red', linestyle='--', label='Meta diária')
plt.title('Desempenho de vendas por dia')
plt.xlabel('Dia da semana')
plt.ylabel('Vendas (R$)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Exibir comissões
for i, valor in enumerate(comissao_final):
    print(f'Vendedor {i+1}: Comissão = R$ {valor:.2f}')