#Contexto Integrado dos Setores
#Imagine um grupo empresarial que opera nas seguintes frentes:
#- Uma rede de hospitais privados que atende pacientes de planos de saúde.
#- Uma divisão de logística e segurança responsável por entregar medicamentos e equipamentos hospitalares com alta rastreabilidade.
#- Uma empresa atacadista de insumos médicos, com fluxo elevado de produtos para clínicas, farmácias e hospitais.
#- Uma corretora de imóveis corporativos, responsável por negociações hospitalares, clínicas e galpões logísticos.
#- Um sistema de prestação de serviços integrados, que atua com manutenção, corretagem, transporte e segurança.

#Geração de Dados Sintéticos (Clientes e Operações)
import numpy as np

np.random.seed(42)

n_clientes = 5000

# IDs fictícios
clientes_id = np.arange(1, n_clientes + 1)

# Setores distribuídos (códigos de área de atuação)
setores = np.random.choice(['Hospital', 'Logística', 'Atacado', 'Corretagem', 'Serviço'], size=n_clientes)

# Faturamento mensal em R$
faturamento = np.random.normal(loc=15000, scale=5000, size=n_clientes).clip(5000, 30000)

# Número médio de atendimentos ou transações
operacoes = np.random.poisson(lam=50, size=n_clientes)

# Nível de risco ou complexidade (0 a 1)
risco_operacional = np.random.rand(n_clientes)

#Análises Avançadas com NumPy + Scikit-learn
#Clustering (agrupamento de clientes por perfil de operação)
from sklearn.cluster import KMeans

# Vetor de características
X = np.column_stack((faturamento, operacoes, risco_operacional))

# Agrupamento em 4 perfis
kmeans = KMeans(n_clusters=4, random_state=42)
grupos = kmeans.fit_predict(X)



#Regressão: Faturamento vs. Volume Operacional
from sklearn.cluster import KMeans

modelo = LinearRegression()
modelo.fit(operacoes.reshape(-1, 1), faturamento)

# Coeficientes
coef = modelo.coef_[0]
intercepto = modelo.intercept_

#Indicadores por setor:
# Média de faturamento por setor
setores_unicos = np.unique(setores)
media_por_setor = {s: np.mean(faturamento[setores == s]) for s in setores_unicos}

# Total de clientes por setor
contagem_setores = {s: np.sum(setores == s) for s in setores_unicos}

#Mini Dashboard de Resultados:
print("📊 Clientes por Setor:")
for setor, qtd in contagem_setores.items():
    print(f"  {setor}: {qtd} clientes")

print("\n💰 Média de Faturamento por Setor:")
for setor, media in media_por_setor.items():
    print(f"  {setor}: R$ {media:,.2f}")

print(f"\n🔍 Regressão Linear: Faturamento vs Operações")
print(f"  Faturamento = {coef:.2f} × Operações + {intercepto:.2f}")

print("\n🧪 Cluster de Clientes (perfis):")
unique, counts = np.unique(grupos, return_counts=True)
for cluster_id, qtd in zip(unique, counts):
    print(f"  Grupo {cluster_id}: {qtd} clientes")



