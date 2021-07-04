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


# img = np.zeros((512,512,3), np.uint8)

def BdeBingo():
    Bingo = random.randint(1, 15)
    if Bingo <= 9:
        Bingo = "0" + str(Bingo)
    if Bingo not in B:
        B.append(Bingo)
    if len(B) == 5:
        pass
    else:
        BdeBingo()


def IdeBingo():
    Bingo = random.randint(16, 30)
    if Bingo not in I:
        I.append(Bingo)
    if len(I) == 5:
        pass
    else:
        IdeBingo()


def NdeBingo():
    Bingo = random.randint(31, 45)
    if Bingo not in N:
        N.append(Bingo)
    if len(N) == 5:
        pass
    else:
        NdeBingo()


def GdeBingo():
    Bingo = random.randint(46, 60)
    if Bingo not in G:
        G.append(Bingo)
    if len(G) == 5:
        pass
    else:
        GdeBingo()


def OdeBingo():
    Bingo = random.randint(61, 75)
    if Bingo not in O:
        O.append(Bingo)
        
    if len(O) == 5:
        pass
    else:
        OdeBingo()


def sortearNumeros():
    B.clear()
    I.clear()
    N.clear()
    G.clear()
    O.clear()
    BdeBingo()
    IdeBingo()
    NdeBingo()
    GdeBingo()
    OdeBingo()


while True:
    qntCartelas = input("Quantas cartelas você deseja? ")
    idCartelas = input("Para qual rodada essas cartelas irão valer? ")

    quantidadeCartelas = 1
    while quantidadeCartelas <= int(qntCartelas):
        print(quantidadeCartelas)

        sortearNumeros()
        print('------------------------')
        print(f"ID: {idCartelas}")
        print(f'B  | I  | N  | G  | O  ')
        x = 10
        y = 100
        img = cv2.imread("bingo_cartela.jpg")
        for i in range(len(B)):
            print(f'{B[i]} | {I[i]} | {N[i]} | {G[i]} | {O[i]}')
# testando git
                                        #(x,y PARA A COLOCACAO DE NUMEROS)
            # rodadaString = str(idCartelas) + str(qntCartelas) + str(i)
            cv2.putText(img, str('ID:' + str(quantidadeCartelas)), (60, 140), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), thickness=2)
            idString = ("R:" + str(idCartelas))
            cv2.putText(img, idString, (460, 140), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), thickness=2)
            
            cv2.putText(img, str(B[i]), (60, (250 + (116 * i))), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=2)
            cv2.putText(img, str(I[i]), (170, (250 + (116 * i))), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=2)

            if i == 2:
                pass
            else:
                cv2.putText(img, str(N[i]), (290, (250 + (116 * i))), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=2)

            cv2.putText(img, str(G[i]), (400, (250 + (116 * i))), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=2)
            cv2.putText(img, str(O[i]), (515, (250 + (116 * i))), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness=2)

            '''cv2.putText(img, B[i], (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
            cv2.putText(img, '12', (55, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
            cv2.putText(img, '13', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
            cv2.putText(img, '14', (145, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
            cv2.putText(img, '15', (190, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))

            cv2.putText(img, '21', (10, 145), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
            cv2.putText(img, '31', (55, 190), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
            cv2.putText(img, '41', (100, 235), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
            cv2.putText(img, '51', (145, 290), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))'''

        cv2.imwrite('CARTELA_' + str(quantidadeCartelas) + '_R' + str(idCartelas) + '.jpg', img)
        cv2.destroyWindow("bingo_cartela.jpg")
        quantidadeCartelas += 1

        print('------------------------')
