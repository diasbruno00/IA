
import networkx as nx
import numpy as np

import csv

G = nx.Graph()


def addNos(G):
    for y in range(42):
            for x in range(42):
                G.add_node((y, x))

                
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


def lerTxtMatriz():
    matriz = [[]]
    with open('matriz.txt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for line in spamreader:
            matriz.append(line)
    return matriz


matriz = lerTxtMatriz()
addNos(G, matriz)
print(G.nodes)  
criarArestas(G, matriz)

print(G.nodes)