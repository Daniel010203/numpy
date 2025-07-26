import numpy as np

# 1D array
a = np.array([1, 2, 3])

# 2D array
b = np.array([[1, 2], [3, 4]])

# Array preenchido com zeros
zeros = np.zeros((3, 3))

# Array preenchido com uns
ones = np.ones((2, 4))

# Array com valores aleatórios
randoms = np.random.rand(2, 2)

# Soma elemento a elemento
np.add(a, [4, 5, 6])  # Output: [5 7 9]

# Subtração
np.subtract(a, [1, 1, 1])  # Output: [0 1 2]

# Multiplicação
np.multiply(a, [2, 3, 4])  # Output: [2 6 12]

# Divisão
np.divide(a, [1, 2, 3])  # Output: [1. 1. 1.]

# Raiz quadrada
np.sqrt(a)  # Output: [1. 1.414... 1.732...]

# Média
np.mean(a)  # Output: 2.0


# Onde a condição é verdadeira, aplica o valor; caso contrário, aplica outro
np.where(a > 1, "maior", "menor")  # Output: ['menor' 'maior' 'maior']

# Comparações
np.equal(a, 2)   # Output: [False  True False]
np.greater(a, 2) # Output: [False False  True]


# Alterar forma (reshape)
c = np.reshape(b, (4,))  # Output: [1 2 3 4]

# Transpor
b.T  # Output: [[1 3] [2 4]]

# Concatenar arrays
np.concatenate((a, [7, 8]))  # Output: [1 2 3 7 8]

# Dividir arrays
np.split(a, 3)  # Output: [array([1]), array([2]), array([3])]

# Somando um valor escalar ao array
a + 10  # Output: [11 12 13]

# Somando arrays de formas diferentes
np.array([[1], [2], [3]]) + np.array([10, 20, 30])
# Output:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]


# Criação de Matrizes

# Matriz 2x3
A = np.array([[1, 2, 3],
              [4, 5, 6]])

# Matriz identidade 3x3
I = np.eye(3)

# Matriz de valores constantes
C = np.full((2, 2), 7)


#Transposição e Reshape
# Transpor matriz (linhas viram colunas)
A.T  # Output: [[1 4] [2 5] [3 6]]

# Alterar forma da matriz
np.reshape(A, (3, 2))  # Output: [[1 2] [3 4] [5 6]]



#Empilhamento e Junção
B = np.array([[7, 8, 9],
              [10, 11, 12]])

# Empilhar verticalmente (linhas)
np.vstack((A, B))
# Output:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# Empilhar horizontalmente (colunas)
np.hstack((A, B))
# Output:
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]


#Indexação e Fatiamento
# Selecionar um elemento específico
A[0, 2]  # Output: 3

# Selecionar uma linha
A[1]  # Output: [4 5 6]

# Selecionar uma coluna
A[:, 0]  # Output: [1 4]

# Submatriz
A[0:2, 1:3]  # Output: [[2 3] [5 6]]

# Operações com Matrizes
# Soma de matrizes
A + B

# Multiplicação elemento por elemento
A * B

# Produto matricial
np.dot(A, B.T)


#Álgebra Linear
# Determinante
np.linalg.det(I)  # Output: 1.0

# Inversa de uma matriz
np.linalg.inv(I)  # Output: mesma matriz identidade

# Autovalores e autovetores
valores, vetores = np.linalg.eig(I)


# Transpor matriz (linhas viram colunas)
A.T  # Output: [[1 4] [2 5] [3 6]]

# Alterar forma da matriz
np.reshape(A, (3, 2))  # Output: [[1 2] [3 4] [5 6]]



# Estatísticas com Numpy
# Criando um array de dados

dados = np.array([10, 15, 20, 35, 40])

# Média
np.mean(dados)  # → 24.0

# Mediana
np.median(dados)  # → 20.0

# Desvio padrão
np.std(dados)  # → 11.401...

# Variância
np.var(dados)  # → 130.0


# Intervalo com espaçamento regular
np.arange(0, 10, 2)  # → [0 2 4 6 8]

# Intervalo entre dois valores com n pontos
np.linspace(0, 1, 5)  # → [0. 0.25 0.5 0.75 1.]

# Números aleatórios
np.random.randint(0, 100, size=(4, 4))

# Aplicar uma função a todos os elementos de um array
def quadrado(x):
    return x ** 2

np.vectorize(quadrado)(np.array([1, 2, 3]))  # → [1 4 9]

# Selecionar elementos com base em uma condição
arr = np.array([2, 5, 7, 1, 8])
np.where(arr > 5, "maior", "menor")  # → ['menor' 'menor' 'maior' 'menor' 'maior']


