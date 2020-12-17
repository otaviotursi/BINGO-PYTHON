import cv2
from os import walk
import numpy as np
import time
import os


def qualquerCoisa():
    f = []
    for (dirpath, dirnames, filenames) in walk(r'D:\VSCODE\PycharmProjects\bingo\certo_bingo'):
        # print(dirpath, '\n', filenames, '\n', dirnames)
        f.extend(filenames)
        break

    for n, a in enumerate(f):
        if a.endswith('.jpg') and a.startswith('CARTELA'):

            img = cv2.imread(a)
            resized = cv2.resize(img, (int(img.shape[1]/2.2), int(img.shape[0]/2.2)), 3)
            
            cv2.imwrite(f'usado_resized{a}', resized)
            cv2.imwrite(f'usado_normal{a}', img)
            if a != 'CARTELA_ANOTACOES.jpg':
                os.remove(a)

    time.sleep(3)


    r = []
    for (dirpath, dirnames, filenames) in walk(r'D:\VSCODE\PycharmProjects\bingo\certo_bingo'):
        # print(dirpath, '\n', filenames, '\n', dirnames)
        r.extend(filenames)
        break

    resizings = []
    for n, a in enumerate(r):
        if a.startswith('usado_resized'):
            resizings.append(a)
            # print(n, a)

    img1 = cv2.imread(resizings[0])
    img2 = cv2.imread(resizings[1])
    img3 = cv2.imread(resizings[2])
    img4 = cv2.imread(resizings[3])
    img5 = cv2.imread(resizings[4])
    img6 = cv2.imread(resizings[5])

    # define a function for vertically 
    # concatenating images of the 
    # same size and horizontally 

    return (img1, img2, img3, img4, img5, img6)

def concat_vh(list_2d): 
    
    # return final image 
    return cv2.vconcat([cv2.hconcat(list_h) 
                        for list_h in list_2d]) 
# # image resizing 
# img1_s = cv2.resize(img1, dsize = (0,0), 
# 					fx = 0.5, fy = 0.5) 

# function calling 


# print(f, r, resizings)
for a in range(3):
    img1,img2,img3,img4,img5,img6 = qualquerCoisa()
    img_tile = concat_vh([[img1, img2, img3], 
                        [img4, img5, img6], 
                        ]) 

    # show the output image 
    cv2.imwrite(f'CARTnumeroCartela.jpg', img_tile)








