import random
import time
import re
import cv2
import numpy as np
import sys
import os

B = []
I = []
N = []
G = []
O = []


def BdeBingo():
    # vai sortear entre os dois valores
    listaB = [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15]
    Bingo = random.choice(listaB)
    Bingo1 = random.choice(listaB)
    while Bingo == Bingo1: 
        Bingo1 = random.choice(listaB)
    listaBin = [Bingo, Bingo1]
    Bingo = random.choice(listaBin)

    if Bingo <= 9:
        Bingo = "0" + str(Bingo)

    # se o valor ja estiver dentro da lista, nao faz nada
    if Bingo not in B:
        B.append(Bingo)
    
    # enquanto a lista for diferente de 5, a funcao vai continuar sendo chamada
    if len(B) != 5:
        BdeBingo()


def IdeBingo():
    # vai sortear entre os dois valores
    listaI = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    Bingo = random.choice(listaI)
    Bingo1 = random.choice(listaI)
    while Bingo == Bingo1: 
        Bingo1 = random.choice(listaI)
    listaBin = [Bingo, Bingo1]
    Bingo = random.choice(listaBin)


    # se o valor ja estiver dentro da lista, nao faz nada
    if Bingo not in I:
        I.append(Bingo)

    # enquanto a lista for diferente de 5, a funcao vai continuar sendo chamada
    if len(I) != 5:
        IdeBingo()


def NdeBingo():
    # vai sortear entre os dois valores
    listaN = [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
    Bingo = random.choice(listaN)
    Bingo1 = random.choice(listaN)
    while Bingo == Bingo1: 
        Bingo1 = random.choice(listaN)
    listaBin = [Bingo, Bingo1]
    Bingo = random.choice(listaBin)

    # se o valor ja estiver dentro da lista, nao faz nada
    if Bingo not in N:
        N.append(Bingo)

    # enquanto a lista for diferente de 5, a funcao vai continuar sendo chamada
    if len(N) != 5:
        NdeBingo()


def GdeBingo():
    # vai sortear entre os dois valores
    listaG = [46,47,48,49,50,51,52,53,54,55,56,57,58,59, 60]
    Bingo = random.choice(listaG)
    Bingo1 = random.choice(listaG)
    while Bingo == Bingo1: 
        Bingo1 = random.choice(listaG)
    listaBin = [Bingo, Bingo1]
    Bingo = random.choice(listaBin)


    # se o valor ja estiver dentro da lista, nao faz nada
    if Bingo not in G:
        G.append(Bingo)

    # enquanto a lista for diferente de 5, a funcao vai continuar sendo chamada
    if len(G) != 5:
        GdeBingo()


def OdeBingo():
    # vai sortear entre os dois valores
    listaO = [61,62,63,64,65,66,67,68,69,70,71,72,73,74, 75]
    Bingo = random.choice(listaO)
    Bingo1 = random.choice(listaO)
    while Bingo == Bingo1: 
        Bingo1 = random.choice(listaO)
    listaBin = [Bingo, Bingo1]
    Bingo = random.choice(listaBin)

    # se o valor ja estiver dentro da lista, nao faz nada
    if Bingo not in O:
        O.append(Bingo)
        
    # enquanto a lista for diferente de 5, a funcao vai continuar sendo chamada
    if len(O) != 5:
        OdeBingo()


def sortearNumeros():
    # limpa a lista
    B.clear()
    I.clear()
    N.clear()
    G.clear()
    O.clear()

    # sorteia os numeros de cada tabela
    BdeBingo()
    IdeBingo()
    NdeBingo()
    GdeBingo()
    OdeBingo()



while True:
    # input de quantidade de cartelas e quantidade de rodadas
    qntCartelas = input("Quantas cartelas você deseja? ")
    rodadasCartelas = input("Para qual rodada essas cartelas irão valer? ")


    quantidadeCartelas = 1
    while quantidadeCartelas <= int(qntCartelas):

        # chama a funcao de sortear os numeros
        sortearNumeros()

        # apresentacao dos numeros da cartela e print 
        print('------------------------')
        print(f"ID: {quantidadeCartelas} R:{rodadasCartelas}")
        print(f'B  | I  | N  | G  | O  ')
        

        # jogando os valores sorteados dentro do papel (cartela a ser impressa)
        x = 10
        y = 100
        img = cv2.imread("bingo_cartelaRotaract.jpg")
        for i in range(len(B)):
            print(f'{B[i]} | {I[i]} | {N[i]} | {G[i]} | {O[i]}')
            
            # informações inicias dentro da cartela
            cv2.putText(img, str('ID:' + str(quantidadeCartelas)), (60, 160), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), thickness=2)
            cv2.putText(img, ("R:" + str(rodadasCartelas)), (460, 160), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), thickness=2)
            
            # dispoê o numero da letra B, (coluna x linha)
            cv2.putText(img, str(B[i]), (55, (400 + (116 * i))), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=2)
            # dispoê o numero da letra i, (coluna x linha)
            cv2.putText(img, str(I[i]), (165, (400 + (116 * i))), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=2)

            # dispoê o numero da letra N, (coluna x linha)
            if not i == 2:
                cv2.putText(img, str(N[i]), (285, (400 + (116 * i))), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=2)

            # dispoê o numero da letra G, (coluna x linha)
            cv2.putText(img, str(G[i]), (395, (400 + (116 * i))), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=2)
            # dispoê o numero da letra O, (coluna x linha)
            cv2.putText(img, str(O[i]), (510, (400 + (116 * i))), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=2)

        cv2.imwrite('cartelas-numeradas/CARTELA_' + str(quantidadeCartelas) + '_R' + str(rodadasCartelas) + '.jpg', img)
        cv2.destroyWindow("bingo_cartelaRotaract.jpg")
        quantidadeCartelas += 1

        print('------------------------')
