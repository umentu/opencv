# -*- coding: UTF-8 -*- 

import cv2
import math 
import numpy as np 
import os

def get_aspectratio(img_src):

    # 画素の行数、列数を取得
    rows, cols = img_src.shape

    x_min = cols
    x_max = 0
    y_min = rows
    y_max = 0

    # 各行ごとに操作
    for y in range(rows):
        # 各列ごとに操作
        for x in range(cols):
            if img_src[y, x] == 255:
                if x < x_min:
                    x_min = x
                elif x > x_max:
                    x_max = x
                if y < y_min:
                    y_min = y
                elif y > y_max:
                    y_max = y

    aspectratio = float(y_max - y_min) / float(x_max - x_min)

    return aspectratio

if __name__ == '__main__':
    
    # 画像の読み込み
    img_src = cv2.imread("./image/hoshi.png", 0)

    aspectratio = get_aspectratio(img_src)
    print(aspectratio)

