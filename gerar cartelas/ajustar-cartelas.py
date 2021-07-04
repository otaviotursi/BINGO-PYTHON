import cv2
from os import walk
import numpy as np
import time
import shutil, os

#programa certoooooooooooooooooooooooooooooooo

#primeiro faz essa parte, que diminui o tamanho da cartela, depoois vamos imprimir em um papel A4

def ajusteTamanho():
    # verifica todas as imgs da pasta
    f = []
    for (dirpath, dirnames, filenames) in walk('cartelas-numeradas/'):
        f.extend(filenames)
        break

    for picture in (f):

        # caminho da foto
        pic = 'cartelas-numeradas/' + picture

        # lê e reduz 2.2 vezes a imagem
        img = cv2.imread(pic)
        resized = cv2.resize(img, (int(img.shape[1]/1.7), int(img.shape[0]/1.7)), 3)

        # escreve a cartela reduzida dentro da pasta "cartelas-ajustadas-tamanho"
        cv2.imwrite(f'cartelas-ajustadas-tamanho/resized_{picture}', resized)
        time.sleep(0.5)
    
    for pic in f:
        if 'CARTELA_ANOTACOES' not in pic:
            shutil.move(f'cartelas-numeradas/{pic}', f'cartelas-usadas/{pic}')


def imprimirA4():
    qntFolhasImpressao = 40
    
    for x in range(qntFolhasImpressao):
        print(f'\nimprimindo folha: {x}')
        # verifica todas as imgs da pasta
        f = []
        for (dirpath, dirnames, filenames) in walk('cartelas-ajustadas-tamanho/'):
            f.extend(filenames)
            break
        
        # le todas as cartelas definidas de 5 em 5, supondo que são 5 rodadas
        tamReduzidoList = []
        for n, a in enumerate(f):
            # vai adicionar a lista de imagens, aquelas que tem "resized"  no nome, também que tenha "R" e que não seja repedido e não adicionar imagens de anotações
            if a.startswith('resized') and f'R{n}' not in tamReduzidoList and 'resized_CARTELA_ANOTACOES' not in tamReduzidoList:
                # salvando...
                tamReduzidoList.append(a)
                # se a quantidade de rodadas/folhas chegar a 5, então para de salvar imgs
                if len(tamReduzidoList) >= 4:
                    break
        
        # salvando imagem de anotações
        anot = []
        for n, a in enumerate(f):
            if a == 'resized_CARTELA_ANOTACOES.jpg':
                anot.append(a)

        # lendo as imagens
        img1 = cv2.imread(f'cartelas-ajustadas-tamanho/{tamReduzidoList[0]}')
        img2 = cv2.imread(f'cartelas-ajustadas-tamanho/{tamReduzidoList[1]}')
        img3 = cv2.imread(f'cartelas-ajustadas-tamanho/{tamReduzidoList[2]}')
        img4 = cv2.imread(f'cartelas-ajustadas-tamanho/{tamReduzidoList[3]}')
        print(f'folhas: {tamReduzidoList[0]} / {tamReduzidoList[1]} / {tamReduzidoList[2]} / {tamReduzidoList[3]}')
        # ajusta as imagens na folha 
        img_tile = concat_vh([[img1, img2, ], 
                        [img3, img4,], 
                        ]) 

        # imprime as imagens
        cv2.imwrite(f'cartelas-impressao/Jogo_CARTELA_{x}.jpg', img_tile)
        print(f"impressao feita: {x}")
        
        time.sleep(1.5)
        # move as magens já utilizadas para outra pasta
        for pic in tamReduzidoList:
            print(f"impressao movida: {pic}")
            shutil.move(f'cartelas-ajustadas-tamanho/{pic}', f'cartelas-usadas/{pic}')
        
        tamReduzidoList.clear()
        f.clear()


def concat_vh(list_2d): 
    # return final image 
    return cv2.vconcat([cv2.hconcat(list_h) for list_h in list_2d]) 


ajusteTamanho()

# está setado para 5 cartelas + 1 de anotações por folha A4
imprimirA4()


