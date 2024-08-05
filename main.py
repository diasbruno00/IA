
import networkx as nx
import numpy as np
import heapq
import os

def encontrar_arquivo(nome_arquivo, diretorio_inicial=os.getcwd()):
    for raiz, dirs, arquivos in os.walk(diretorio_inicial):
        if nome_arquivo in arquivos:
            return os.path.join(raiz, nome_arquivo)
    return None

def lerTxtMatriz(nome_arquivo):
   
    caminho_arquivo = encontrar_arquivo(nome_arquivo)
    if not caminho_arquivo:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
        return None

    # Inicializa a matriz
    matriz = [['t' for _ in range(42)] for _ in range(42)]

    try:
        # Abre o arquivo no caminho especificado para leitura
        with open(caminho_arquivo, 'r') as file:
            # Lê cada linha do arquivo
            for line in file:
                # Divide a linha por espaços para obter linha, coluna e cor
                linha, coluna, cor = line.split()
                # Preenche a matriz com os valores do arquivo (-1 para converter de 1-based para 0-based)
                matriz[int(linha) - 1][int(coluna) - 1] = cor
        
        print("Matriz lida com sucesso!\n")
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

    return matriz


# Função para adicionar nós ao grafo
def addNos(G):

    for y in range(1,43):
        for x in range(1,43):
            G.add_node((y, x))
    
    print("Grafo criado com sucesso! \n" )


# Função para criar arestas no grafo
def criarArestas(G, matrizGerada):


    # m = Terra
    # t = verde
    # b = cinza claro
    # a = azul
    # z = cinza escuro

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
    
    print("Arestas criadas com sucesso! \n")



def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruir_caminho(veio_de, inicio, objetivo):
    caminho = []
    atual = objetivo
    while atual != inicio:
        caminho.append(atual)
        atual = veio_de[atual]
    caminho.append(inicio)
    caminho.reverse()
    return caminho

def busca_a_estrela(grafo, inicio, objetivo):
    lista_aberta = []
    heapq.heappush(lista_aberta, (0, inicio))
    veio_de = {}
    custo_ate_agora = {}
    veio_de[inicio] = None
    custo_ate_agora[inicio] = 0

    while lista_aberta:
        _, atual = heapq.heappop(lista_aberta)

        if atual == objetivo:
            break

        for proximo in grafo.neighbors(atual):
            novo_custo = custo_ate_agora[atual] + grafo[atual][proximo].get('weight', 1)
            if proximo not in custo_ate_agora or novo_custo < custo_ate_agora[proximo]:
                custo_ate_agora[proximo] = novo_custo
                prioridade = novo_custo + heuristica(objetivo, proximo)
                heapq.heappush(lista_aberta, (prioridade, proximo))
                veio_de[proximo] = atual

                # Exibir o custo acumulado até o próximo nó
                # esta comentado porque polui muito a tela
                #print(f"Movendo para {proximo} com custo acumulado {novo_custo}")

    caminho = reconstruir_caminho(veio_de, inicio, objetivo)
    custo_final = custo_ate_agora[objetivo]
        
    return caminho, custo_final


def imprimir_grafo(caminho):

    for passo, posicao in enumerate(caminho):
        if caminho is None:
         print("Nenhum caminho encontrado")
         return
        else:
            if posicao == (14, 32):
                print(f"Rick chegou no primeiro objetivo! {posicao} \n")
            elif posicao == (36,36):
                print(f"Rick chegou no segundo objetivo! {posicao} \n")
            elif posicao == (6,33):
                print(f"Rick chegou no terceiro objetivo! {posicao} \n")
            elif posicao == (40,21):
                print(f"Rick reuniu todo o grupo e saiu da prisão pela porta inferior! {posicao} \n")


# Cria o grafo
G = nx.Graph()

# Lê a matriz do arquivo
nome_arquivo = 'matriz.txt'
matriz = lerTxtMatriz(nome_arquivo)

# Adiciona nós ao grafo
addNos(G)

# Cria arestas no grafo com base na matriz
criarArestas(G, matriz)

rick = (21, 13)

print(f"Posição inicial de Rick: {rick} \n")

inicio = rick

objetivo =  [(14, 32) , (36,36), (6,33), (40,21)]
caminho = []
custoFinal = 0

for objetivo in objetivo:
    print(f"Rick está indo para {objetivo}")
    caminho, custoFinal = busca_a_estrela(G, inicio, objetivo)
    
    imprimir_grafo(caminho)

print(f"Custo final: {custoFinal} \n")

print("Alunos")

print("Bruno Dias Pinto 18.2.8144")

print("Caio Guilherme Costa Carvalho 18.2.8026")

print("Pablo Batista de Andrade Reis - 20.1.8106")
