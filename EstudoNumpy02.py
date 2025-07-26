import numpy as np

vendas = np.array([20, 35, 50, 40, 25, 30, 45])  # De domingo a sábado
dias = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']

media = np.mean(vendas)
total = np.sum(vendas)
max_index = np.argmax(vendas)
min_index = np.argmin(vendas)

print(f'Dia com mais vendas: {dias[max_index]} ({vendas[max_index]})')
print(f'Dia com menos vendas: {dias[min_index]} ({vendas[min_index]})')
print(f'Média semanal de vendas: {media}')
print(f'Total de vendas na semana: {total}')

# Dias com vendas acima da média
dias_acima = [dias[i] for i in range(len(vendas)) if vendas[i] > media]
print(f'Dias acima da média: {dias_acima}')

# Comissões de 10%
comissoes = vendas * 0.10
print(f'Comissões diárias: {comissoes}')