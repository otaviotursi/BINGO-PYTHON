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
    # enquanto a lista for diferente de 5, a funcao vai continuar sendo chamada
    lista1 = [1,2,3,4,5]
    lista2 = [6,7,8,9,10]
    lista3 = [11,12,13,14,15]

    ultimaLista = 'Vazio'
    while len(B) < 5:
        # vai sortear entre os valores das listas
        Bingo1 = random.choice(lista1)
        Bingo2 = random.choice(lista2)
        Bingo3 = random.choice(lista3)
        Bingo = random.choice([Bingo1,Bingo2,Bingo3])
        semAval = False
        if Bingo < 6:
            if ultimaLista == 'Bingo1':
                semAval = True
            ultimaLista = 'Bingo1'
        elif Bingo < 11:
            if ultimaLista == 'Bingo2':
                semAval = True
            ultimaLista = 'Bingo2'
        else:
            if ultimaLista == 'Bingo3':
                semAval = True
            ultimaLista = 'Bingo3'

        if not semAval:
            # se o valor ja estiver dentro da lista, exclui ele
            if Bingo not in B:
                if ("0" + str(Bingo)) not in B:
                    if Bingo <= 9:
                        Bingo = "0" + str(Bingo)
                    B.append(Bingo)


def IdeBingo():
    # valores possiveis de serem sorteados
    lista1 = [16,17,18,19,20]
    lista2 = [21,22,23,24,25]
    lista3 = [26,27,28,29,30]

    ultimaLista = 'Vazio'
    # enquanto a lista for diferente de 5, a funcao vai continuar sendo chamada
    while len(I) < 5:
        # vai sortear entre os valores das listas
        Bingo1 = random.choice(lista1)
        Bingo2 = random.choice(lista2)
        Bingo3 = random.choice(lista3)
        Bingo = random.choice([Bingo1,Bingo2,Bingo3])
        
        # faz uma verificao se a lista sorteada, foi a ultima ou não. 
        semAval = False
        if Bingo < 21:
            if ultimaLista == 'Bingo1':
                semAval = True
            ultimaLista = 'Bingo1'
        elif Bingo < 26:
            if ultimaLista == 'Bingo2':
                semAval = True
            ultimaLista = 'Bingo2'
        else:
            if ultimaLista == 'Bingo3':
                semAval = True
            ultimaLista = 'Bingo3'
        
        # se a verificação liberar, passa para a próxima etapa, se não, continua no ciclo
        if not semAval:
            # se o valor não estiver dentro da lista, vai adicionar ele
            if Bingo not in I:
                I.append(Bingo)


def NdeBingo():
    lista1 = [31,32,33,34,35]
    lista2 = [36,37,38,39,40]
    lista3 = [41,42,43,44,45]

    ultimaLista = 'Vazio'
    while len(N) < 5:
        Bingo1 = random.choice(lista1)
        Bingo2 = random.choice(lista2)
        Bingo3 = random.choice(lista3)
        Bingo = random.choice([Bingo1,Bingo2,Bingo3])
        
        semAval = False
        if Bingo < 36:
            if ultimaLista == 'Bingo1':
                semAval = True
            ultimaLista = 'Bingo1'
        elif Bingo < 41:
            if ultimaLista == 'Bingo2':
                semAval = True
            ultimaLista = 'Bingo2'
        else:
            if ultimaLista == 'Bingo3':
                semAval = True
            ultimaLista = 'Bingo3'

        if not semAval:
            if Bingo not in N:
                N.append(Bingo)


def GdeBingo():
    lista1 = [46,47,48,49,50]
    lista2 = [51,52,53,54,55]
    lista3 = [56,57,58,59,60]

    ultimaLista = 'Vazio'
    while len(G) < 5:
        Bingo1 = random.choice(lista1)
        Bingo2 = random.choice(lista2)
        Bingo3 = random.choice(lista3)
        Bingo = random.choice([Bingo1,Bingo2,Bingo3])
        
        semAval = False
        if Bingo < 51:
            if ultimaLista == 'Bingo1':
                semAval = True
            ultimaLista = 'Bingo1'
        elif Bingo < 56:
            if ultimaLista == 'Bingo2':
                semAval = True
            ultimaLista = 'Bingo2'
        else:
            if ultimaLista == 'Bingo3':
                semAval = True
            ultimaLista = 'Bingo3'
        
        if not semAval:
            if Bingo not in G:
                G.append(Bingo)

def OdeBingo():
    lista1 = [61,62,63,64,65]
    lista2 = [66,67,68,69,70]
    lista3 = [71,72,73,74,75]

    ultimaLista = 'Vazio'
    while len(O) < 5:
        Bingo1 = random.choice(lista1)
        Bingo2 = random.choice(lista2)
        Bingo3 = random.choice(lista3)
        Bingo = random.choice([Bingo1,Bingo2,Bingo3])
        
        semAval = False
        if Bingo < 66:
            if ultimaLista == 'Bingo1':
                semAval = True
            ultimaLista = 'Bingo1'
        elif Bingo < 71:
            if ultimaLista == 'Bingo2':
                semAval = True
            ultimaLista = 'Bingo2'
        else:
            if ultimaLista == 'Bingo3':
                semAval = True
            ultimaLista = 'Bingo3'
        
        if not semAval:
            if Bingo not in O:
                O.append(Bingo)
        

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

        # id unico da tabela e rodada destinada 
        print('------------------------')
        print(f"ID: {quantidadeCartelas} R:{rodadasCartelas}")
        print(f'B  | I  | N  | G  | O  ')
        

        # jogando os valores sorteados dentro do papel (cartela a ser impressa)
        x = 10
        y = 100
        if (rodadasCartelas == '1'):
            img = cv2.imread("bingo_cartelaRotaract1.jpg")
        elif (rodadasCartelas == '2'):
            img = cv2.imread("bingo_cartelaRotaract2.jpg")
        elif (rodadasCartelas == '3'):
            img = cv2.imread("bingo_cartelaRotaract3.jpg")
        else:
            img = cv2.imread("bingo_cartelaRotaract4.jpg")

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
        quantidadeCartelas += 1

        print('------------------------')
