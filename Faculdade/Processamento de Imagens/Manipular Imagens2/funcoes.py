import math
from sys import maxsize
inicio = [0, 0, 0, 1]

x = "x"
y = "y"
z = "z"

def criarPonto(x, y, z):
    return [x, y, z, 1]

def multiplicarMatrizes(listaDeMatrizes):
    matrizResultante = listaDeMatrizes.pop(0)

    while len(listaDeMatrizes) > 0:
        matrizIntermediaria = []
        matrizMultiplicando = listaDeMatrizes.pop(0)

        for numeroDaLinha in range(len(matrizResultante)):
            matrizIntermediaria.append([0 for i in range(len(matrizResultante[numeroDaLinha]))]) 
            for numeroDaColuna in range(len(matrizResultante[numeroDaLinha])):
                limite = len(matrizResultante[numeroDaLinha])-1
                soma = []
                for numeroAuxiliar in range(len(matrizMultiplicando)):
                    soma.append(round(matrizResultante[numeroDaLinha][numeroAuxiliar if numeroAuxiliar <= limite else limite], 4) * round(matrizMultiplicando[numeroAuxiliar][numeroDaColuna], 4))
                matrizIntermediaria[numeroDaLinha][numeroDaColuna] = round(sum(soma),4)
        matrizResultante = matrizIntermediaria
    return matrizResultante

def menorPonto(referencia, matrizDePontos):
    menorDiferenca = maxsize
    menorPonto = matrizDePontos[0]

    for ponto in matrizDePontos:
        resultado = [referencia[i] - abs(ponto[i]) for i in range(len(ponto)-1)]
        resultado.append(1)
        if abs(sum(resultado)) < menorDiferenca:
            menorDiferenca = abs(sum(resultado))
            menorPonto = ponto
    
    return menorPonto

def maiorPonto(referencia, matrizDePontos):
    maiorDiferenca = -maxsize
    maiorPonto = matrizDePontos[0]

    for ponto in matrizDePontos:
        resultado = [referencia[i] - abs(ponto[i]) for i in range(len(ponto)-1)]
        resultado.append(1)
        if abs(sum(resultado)) > maiorDiferenca:
            maiorDiferenca = abs(sum(resultado))
            maiorPonto = ponto
    
    return maiorPonto

def pontoMedio(matrizDePontos):
    menor = menorPonto(inicio, matrizDePontos)
    maior = maiorPonto(menor, matrizDePontos)
    resultado = [(maior[i] - menor[i])/2 + menor[i] for i in range(len(maior)-1)]
    resultado.append(1)
    return resultado
    

def diferencaEntrePontos(ponto1, ponto2):
    menor = menorPonto(inicio, [ponto1, ponto2])
    maior = ponto1 if ponto1 != menor else ponto2
    resultado = [menor[i] - maior[i] for i in range(len(ponto1)-1)]
    resultado.append(1)
    return resultado

def translacionarMatriz(matriz, dx, dy, dz):
    matrizBaseTranslacao = [
        [1,  0,  0,  0],
        [0,  1,  0,  0],
        [0,  0,  1,  0],
        [dx, dy, dz, 1]
    ]

    return multiplicarMatrizes([matriz, matrizBaseTranslacao])

def escalonarMatriz(matriz, sx, sy, sz):
    pontoMedioInicial = pontoMedio(matriz)
    matrizBaseEscalonamento = [
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0,  1]
    ]
    resultado = multiplicarMatrizes([matriz, matrizBaseEscalonamento])
    pontoMedioFinal = pontoMedio(resultado)
    diferenca = diferencaEntrePontos(pontoMedioInicial, pontoMedioFinal)
    
    return translacionarMatriz(resultado, diferenca[0], diferenca[1], diferenca[2])

def rotacionarMatriz(matriz, angulo, eixo):
    matrizBaseRotacao = []
    if eixo == x:
        matrizBaseRotacao = [
            [1, 0, 0, 0],
            [0, math.cos(angulo), -math.sin(angulo), 0],
            [0, math.sin(angulo), math.cos(angulo), 0],
            [0, 0, 0,  1]
        ]
            
    if eixo == y:
        matrizBaseRotacao = [
            [math.cos(angulo), 0, math.sin(angulo), 0],
            [0, 1, 0, 0],
            [-math.sin(angulo), 0, math.cos(angulo), 0],
            [0, 0, 0,  1]
        ]
            
    if eixo == z:
        matrizBaseRotacao = [
            [math.cos(angulo), -math.sin(angulo), 0, 0],
            [math.sin(angulo), math.cos(angulo), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    pontoMedioInicial = pontoMedio(matriz)
    resultado = multiplicarMatrizes([matriz, matrizBaseRotacao])
    pontoMedioFinal = pontoMedio(resultado)
    diferenca = diferencaEntrePontos(pontoMedioInicial, pontoMedioFinal)

    return translacionarMatriz(resultado, diferenca[0], diferenca[1], diferenca[2])
