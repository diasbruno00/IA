
import networkx as nx
import csv

G = nx.Graph()

def salvarTxtMatriz(matriz):
    with open('matriz.txt', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerows(matriz)

def gerarMatriz44X44(linha, coluna):
 
    matriz = []
    for i in range(linha):
        for j in range(coluna):
            matriz.append((i, j))
            G.add_node((i, j))
    return matriz

def criarArestas(G):
        for y in range(42):
            for x in range(42):
                # Verifique os vizinhos (cima, baixo, esquerda, direita)
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    # Certifique-se de que os vizinhos estão dentro dos limites da matriz
                    if 0 <= ny < 42 and 0 <= nx < 42:
                        # Determine o custo da aresta com base no tipo de terreno
                        if matrizGerada[ny][nx] == 'asfalto':
                            custo = 1
                        elif matrizGerada[ny][nx] == 'terra':
                            custo = 3
                        elif matrizGerada[ny][nx] == 'grama':
                            custo = 5
                        elif matrizGerada[ny][nx] == 'paralelepípedo':
                            custo = 10
                        elif matrizGerada[ny][nx] == 'edificio':
                            custo = float('inf')  # Defina o custo como infinito para evitar passar por regiões de edifícios
                        else:
                            custo = 0  # Caso o tipo de terreno não seja reconhecido, atribua um custo de 0
                        G.add_edge((y, x), (ny, nx), weight=custo)


def lerTxtMatriz():
    matriz = []
    with open('matriz.txt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        matriz = [line for line in spamreader]

    return matriz



matrizGerada = gerarMatriz44X44(42,42)
criarArestas(G)
