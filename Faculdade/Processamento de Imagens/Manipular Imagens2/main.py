#Isabelle Araujo Sepulveda - 60382-1
#José Vitor de Araujo - 60331-7
#Vitor Alexandre Oliveira da Silva - 60913-7


from funcoes import *

ponto1 = criarPonto(3, 2, 0)
ponto2 = criarPonto(3, 3, 0)
ponto3 = criarPonto(5, 2, 0)
ponto4 = criarPonto(5, 3, 0)
ponto5 = criarPonto(3, 2, 2)
ponto6 = criarPonto(3, 3, 2)
ponto7 = criarPonto(5, 2, 2)
ponto8 = criarPonto(5, 3, 2)

matriz = [
    ponto1, ponto2, ponto3, ponto4, ponto5, ponto6, ponto7, ponto8
]


print(escalonarMatriz(rotacionarMatriz( matriz, math.radians(90), z), 2, 2, 1 ))