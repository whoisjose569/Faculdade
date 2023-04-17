import cv2
import numpy as np

def espelhaMatriz(matriz):
    vetInvertido2 = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz[i])):
            elemento_espelhado = matriz[i][len(matriz[i])-j-1]
            linha.append(elemento_espelhado)
        vetInvertido2.append(linha)
    return vetInvertido2

img = cv2.imread('retangulo.png')
imgArray = np.array(img)
novaImagem = np.array(espelhaMatriz(imgArray))
cv2.imwrite('imagemEspelhada.png', novaImagem)



def matrizDireita(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    matrizDireita = []
    for i in range(colunas):
        linha = []
        for j in range(linhas):
            linha.append(0)
        matrizDireita.append(linha)
    
    for i in range(linhas):
        for j in range(colunas):
            matrizDireita[j][linhas-i-1] = matriz[i][j]
    
    return matrizDireita

def matrizEsquerda(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    matrizEsquerda = []
    for i in range(colunas):
        linha = []
        for j in range(linhas):
            linha.append(0)
        matrizEsquerda.append(linha)
    
    for i in range(linhas):
        for j in range(colunas):
            matrizEsquerda[colunas-j-1][i] = matriz[i][j]
    
    return matrizEsquerda

img = cv2.imread("retangulo.png")
imgArray = np.array(img)
novaImagem = np.array(matrizDireita(imgArray))
cv2.imwrite("retanguloDireita.png", novaImagem)

img = cv2.imread("retangulo.png")
imgArray = np.array(img)
novaImagem = np.array(matrizEsquerda(imgArray))
cv2.imwrite("retanguloEsquerda.png", novaImagem)













