import os
import numpy as np
import pandas as pd

def ler_txt_para_matriz(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    # Inicializar valores máximos
    max_linha = 0
    max_coluna = 0
    
    # Primeiro passe para determinar as dimensões da matriz
    for linha in linhas:
        partes = linha.strip().split()
        if len(partes) == 3:
            l, c, _ = partes
            max_linha = max(max_linha, int(l))
            max_coluna = max(max_coluna, int(c))
    
    # Inicializar a matriz com None
    matriz = np.empty((max_linha, max_coluna), dtype=object)
    matriz.fill(None)
    
    # Segundo passe para preencher a matriz
    for linha in linhas:
        partes = linha.strip().split()
        if len(partes) == 3:
            l, c, cor = partes
            matriz[int(l) - 1, int(c) - 1] = cor
    
    return matriz



# Exemplo de uso:
caminho_arquivo = "C:/Users/diasb/OneDrive/Área de Trabalho/Inteligencia artificial/teste/matriz.txt"
matriz = ler_txt_para_matriz(caminho_arquivo)


df = pd.DataFrame(matriz)

# Visualizando a matriz
print(df)

# Para visualizar a matriz em uma janela de console interativa (como Jupyter Notebook)
# você pode usar display(df) ao invés de print(df)

# Se estiver usando um ambiente de script padrão, você pode querer salvar a matriz em um arquivo Excel
df.to_excel("matriz_visualizada.xlsx", index=False, header=False)