import cv2
from os import walk
import numpy as np
import time
import shutil, os


#primeiro faz essa parte, que diminui o tamanho da cartela, depois vamos salvar em um papel A4

def ajusteTamanho():
    # "escaneia" todas as cartelas geradas pelo 'gerador-cartelas'
    f = []
    for (dirpath, dirnames, filenames) in walk('cartelas-numeradas/'):
        f.extend(filenames)
        break

    # com todas as imagens lindas, começa a execução de diminiur a imagem e move-la
    for n, picture in enumerate(f):
        print(f'\nRedefinindo tamanho cartela: {n+1}')
        # caminho da foto
        pic = 'cartelas-numeradas/' + picture

        # lê e reduz 1.7 vezes a imagem (tamanho que vi que fica bom na A4)
        img = cv2.imread(pic)
        resized = cv2.resize(img, (int(img.shape[1]/1.7), int(img.shape[0]/1.7)), 3)

        # escreve a cartela reduzida dentro da pasta "cartelas-ajustadas-tamanho"
        cv2.imwrite(f'cartelas-ajustadas-tamanho/resized_{picture}', resized)
        time.sleep(0.5)

        shutil.move(f'cartelas-numeradas/{picture}', f'cartelas-usadas/{picture}')
    
    # obsoleto
    # for pic in f:
    #     if 'CARTELA_ANOTACOES' not in pic:
    #         shutil.move(f'cartelas-numeradas/{pic}', f'cartelas-usadas/{pic}')


def imprimirA4():
    # colocar a quantidade de folhas a4 que voce quer
    qntFolhasImpressao = 16
    
    for x in range(qntFolhasImpressao):
        print(f'\nimprimindo folha: {x+1}')

        # escaneia todas as imgs da pasta (ja ajustadas)
        f = []
        for (dirpath, dirnames, filenames) in walk('cartelas-ajustadas-tamanho/'):
            f.extend(filenames)
            break
        
        # le todas as cartelas e define elas em grupos de 4 | substituir FOR por WHILE
        tamReduzidoList = []
        contCartela = 0
        while contCartela < len(f):
            file = f[contCartela]
            # vai adicionar a lista de imagens, aquelas que tem "resized"  no nome, também que tenha "R" e que não seja repetido. Não irá adicionar imagens de anotações (obsoleto)
            if file.startswith('resized') and f'R{contCartela}' not in tamReduzidoList and 'resized_CARTELA_ANOTACOES' not in tamReduzidoList:
                # salvando em lista...
                tamReduzidoList.append(file)
                # se a quantidade de rodadas/folhas for igual à 4 ou maior, então para de salvar imgs
                if len(tamReduzidoList) >= 4:
                    break
            contCartela += 1
        
        # salvando imagem de anotações | obsoleto
        # anot = []
        # for n, a in enumerate(f):
        #     if a == 'resized_CARTELA_ANOTACOES.jpg':
        #         anot.append(a)

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

        # salva as imagens em outra pasta
        cv2.imwrite(f'cartelas-impressao/Jogo_CARTELA_{x}.jpg', img_tile)
        print(f"impressao feita: {x}")
        
        time.sleep(1.5)
        # move as imagens já utilizadas para outra pasta
        for pic in tamReduzidoList:
            print(f"impressao movida: {pic}")
            shutil.move(f'cartelas-ajustadas-tamanho/{pic}', f'cartelas-usadas/{pic}')
        
        tamReduzidoList.clear()
        f.clear()


def concat_vh(list_2d): 
    # retorna a imagem
    return cv2.vconcat([cv2.hconcat(list_h) for list_h in list_2d]) 


print("AJUSTANDO CARTELAS")
ajusteTamanho()

print("VAMOS COMEÇAR A IMPRIMIR AS CARTELAS")
imprimirA4()


