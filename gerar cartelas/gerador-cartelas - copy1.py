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
    Bingo = random.randint(1, 15)
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
    Bingo = random.randint(16, 30)

    # se o valor ja estiver dentro da lista, nao faz nada
    if Bingo not in I:
        I.append(Bingo)

    # enquanto a lista for diferente de 5, a funcao vai continuar sendo chamada
    if len(I) != 5:
        IdeBingo()


def NdeBingo():
    # vai sortear entre os dois valores
    Bingo = random.randint(31, 45)
    
    # se o valor ja estiver dentro da lista, nao faz nada
    if Bingo not in N:
        N.append(Bingo)

    # enquanto a lista for diferente de 5, a funcao vai continuar sendo chamada
    if len(N) != 5:
        NdeBingo()


def GdeBingo():
    # vai sortear entre os dois valores
    Bingo = random.randint(46, 60)

    # se o valor ja estiver dentro da lista, nao faz nada
    if Bingo not in G:
        G.append(Bingo)

    # enquanto a lista for diferente de 5, a funcao vai continuar sendo chamada
    if len(G) != 5:
        GdeBingo()


def OdeBingo():
    # vai sortear entre os dois valores
    Bingo = random.randint(61, 75)

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
