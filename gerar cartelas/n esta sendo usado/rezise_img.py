import cv2
from os import walk
import numpy as np
import time
import shutil, os

#programa certoooooooooooooooooooooooooooooooo

#primeiro fazer essa parte

# f = []
# for (dirpath, dirnames, filenames) in walk(r'D:\VSCODE\PycharmProjects\bingo\certo_bingo'):
#     # print(dirpath, '\n', filenames, '\n', dirnames)
#     f.extend(filenames)
#     break

# for n, a in enumerate(f):
#     if a.endswith('.jpg') and a.startswith('CARTELA'):

#         img = cv2.imread(a)
#         resized = cv2.resize(img, (int(img.shape[1]/2.2), int(img.shape[0]/2.2)), 3)

#         cv2.imwrite(f'resized{a}', resized)

# time.sleep(3)


#depois essa parte
for x in range(99):
    r = []
    for (dirpath, dirnames, filenames) in walk(r'D:\Area de Trabalho\tudo\pack bots\dizuBot\bot\bots-novos\BINGO-PYTHON\gerar cartelas'):
        # print(dirpath, '\n', filenames, '\n', dirnames)
        r.extend(filenames)
        break

    anot = []
    resizings = []
    for n, a in enumerate(r):
        # print(n, a)
        if a.startswith('resized'):
            resizings.append(a)
            print(a)
            # os.remove(a)
            # shutil.move(a, 'dest_folder')
            if len(resizings) >=5:
                break

    for n, a in enumerate(r):
        if a == 'resizedCARTELA_ANOTACOES.jpg':
            anot.append(a)
        

    print(resizings, anot)
    img1 = cv2.imread(resizings[0])
    img2 = cv2.imread(resizings[1])
    img3 = cv2.imread(resizings[2])
    img4 = cv2.imread(resizings[3])
    img5 = cv2.imread(resizings[4])
    img6 = cv2.imread(anot[0])

    # define a function for vertically 
    # concatenating images of the 
    # same size and horizontally 
    
    def concat_vh(list_2d): 
        
        # return final image 
        return cv2.vconcat([cv2.hconcat(list_h) 
                            for list_h in list_2d]) 

    # print(f, r, resizings)
    img_tile = concat_vh([[img1, img2, img3], 
                        [img4, img5, img6], 
                        ]) 

    # show the output image 
    cv2.imwrite(f'Jogo_CARTELA{x}.jpg', img_tile)
    for f in resizings:
        shutil.move(f, 'dest_folder')







