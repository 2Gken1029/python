#! python3
# openCVCode.py - openCVを動かすためのサンプルプログラム

import cv2
import math
import numpy as np

file_src = 'sample.png'

img_src = cv2.imread(file_src, 1) # 入力画像の読み込み

cv2.namedWindow('sample')

cv2.imshow('sample', img_src) # 入力画像を表示

print('キー入力待ち．．．')

while True:
    key = cv2.waitKey(0) # キー入力待ち
    if(key == 13): # Enterキー
        cv2.destroyAllWindows()
        break
    else:
        print('終了するならEnterキー')
        print('キー入力待ち...')