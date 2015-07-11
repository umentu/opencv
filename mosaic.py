# -*- coding: UTF-8 -*- 

import cv2
import math 
import numpy as np 
import os

if __name__ == '__main__':

    # 画像の読み込み
    img_src = cv2.imread("./image/karasu.jpg", 1)

    # 元の画像のサイズを取得
    size = img_src.shape[:2][::-1]

    # 画像全体を一度1/20に縮小
    img_tmp = cv2.resize(img_src, (int(size[0]/20), int(size[1]/20)))

    # 圧縮したものを再度本のサイズに拡大
    img_dst = cv2.resize(img_tmp, size, interpolation=cv2.INTER_NEAREST)

    # 表示
    cv2.imshow("Show MOSAIC Image", img_dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()