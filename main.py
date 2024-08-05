
import networkx as nx
import numpy as np

# Função para adicionar nós ao grafo
def addNos(G):
    for y in range(42):
        for x in range(42):
            G.add_node((y, x))

# Função para criar arestas no grafo
def criarArestas(G, matrizGerada):
    for y in range(42):
        for x in range(42):
            # Verifique os vizinhos (cima, baixo, esquerda, direita)
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                # Certifique-se de que os vizinhos estão dentro dos limites da matriz
                if 0 <= ny < 42 and 0 <= nx < 42:
                    # Determine o custo da aresta com base no tipo de terreno
                    if matrizGerada[ny][nx] == 'z':
                        custo = 1
                    elif matrizGerada[ny][nx] == 'm':
                        custo = 3
                    elif matrizGerada[ny][nx] == 't':
                        custo = 5
                    elif matrizGerada[ny][nx] == 'b':
                        custo = 10
                    elif matrizGerada[ny][nx] == 'a':
                        custo = float('inf')  # Defina o custo como infinito para evitar passar por regiões de edifícios
                    else:
                        custo = 0  # Caso o tipo de terreno não seja reconhecido, atribua um custo de 0
                    G.add_edge((y, x), (ny, nx), weight=custo)

# Função para ler o arquivo e gerar a matriz bidimensional
def lerTxtMatriz():
    # Inicializa uma matriz 42x42 com valor padrão 't'
    matriz = [['t' for _ in range(42)] for _ in range(42)]

    # Abre o arquivo matriz.txt para leitura
    with open('C:/Users/diasb/OneDrive/Área de Trabalho/Inteligencia artificial/teste/matriz.txt', 'r') as file:
        # Lê cada linha do arquivo
        for line in file:
            # Divide a linha por espaços para obter linha, coluna e cor
            linha, coluna, cor = line.split()
            # Preenche a matriz com os valores do arquivo
            matriz[int(linha) - 1][int(coluna) - 1] = cor  # -1 para converter de 1-based para 0-based

    return matriz

# Cria o grafo
G = nx.Graph()

# Lê a matriz do arquivo
matriz = lerTxtMatriz()

# Adiciona nós ao grafo
addNos(G)

# Cria arestas no grafo com base na matriz
criarArestas(G, matriz)

# Exibe alguns nós do grafo para verificar se está funcionando corretamente
#print(list(G.nodes)[:10])

# Exibe algumas arestas do grafo com os pesos para verificar se está funcionando corretamente
print(list(G.edges(data=True)))
