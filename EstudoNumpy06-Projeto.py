import numpy as np

# Simulando temperaturas de 4 cidades em 7 dias (°C)
temperaturas = np.array([
    [28, 29, 30, 31, 32, 30, 29],  # Cidade 1
    [22, 24, 23, 26, 27, 25, 24],  # Cidade 2
    [33, 34, 33, 35, 36, 34, 33],  # Cidade 3
    [18, 19, 20, 20, 21, 22, 20]   # Cidade 4
])

# Estatísticas por cidade
medias_cidade = np.mean(temperaturas, axis=1)
maximas_cidade = np.max(temperaturas, axis=1)
minimas_cidade = np.min(temperaturas, axis=1)

# Estatísticas por dia
media_por_dia = np.mean(temperaturas, axis=0)
dia_mais_quente = np.argmax(media_por_dia)

# Filtragem — dias quentes da Cidade 1 (>30°C)
dias_quentes_cidade1 = np.where(temperaturas[0] > 30)[0]

# Ordenação da Cidade 2
ordenada_cidade2 = np.sort(temperaturas[1])

# Transposição para ver temperaturas por dia
temp_por_dia = temperaturas.T

# Exibindo resultados
print("📊 Médias de temperatura por cidade:")
for i, media in enumerate(medias_cidade, start=1):
    print(f"  Cidade {i}: {media:.2f}°C")

print("\n🌡️ Máximas por cidade:", maximas_cidade)
print("❄️ Mínimas por cidade:", minimas_cidade)

print(f"\n🔥 Dia mais quente (maior média entre cidades): Dia {dia_mais_quente + 1}")
print("📆 Média de temperatura por dia:", media_por_dia)

print(f"\n☀️ Dias em que a Cidade 1 teve temperatura acima de 30°C: {dias_quentes_cidade1 + 1}")

print("\n🧮 Temperaturas ordenadas da Cidade 2:", ordenada_cidade2)

print("\n🔄 Temperaturas por dia (transposta):\n", temp_por_dia)