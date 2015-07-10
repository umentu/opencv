# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':
    
    # 画像の読み込み
    img_src = cv2.imread("./image/karasu.jpg", 1)

    # 平均化する画素の周囲の大きさを指定する。
    # (25, 25) の場合、個々の画素の地点の周囲25×25マスの平均をとる。
    # 数値が大きいほどぼやける。
    average_square = (25, 25)

    # x軸方向の標準偏差
    sigma_x = 1

    # Gaussianオペレータを使用して平滑化
    img_gauss = cv2.GaussianBlur(img_src, average_square, sigma_x)

    # 表示
    cv2.imshow("Show GAUSS Image", img_gauss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
