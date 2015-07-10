# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':
    
    # 画像の読み込み
    img_src = cv2.imread("./image/karasu.jpg", 1)

    # 平均化する画素の周囲の大きさを指定する。
    # 25の場合、個々の画素の地点の周囲25×25マスの平均をとる。
    # 数値が大きいほどぼやける。
    average_square_size = 25

    # 色空間に関する標準偏差
    sigma_color = 1

    # 距離空間に関する標準偏差
    sigma_metric = 1

    # Bilateralオペレータを使用して平滑化
    img_bilateral = cv2.bilateralFilter(img_src, 
                                 average_square_size,
                                 sigma_color,
                                 sigma_metric)

    # 表示
    cv2.imshow("Show BILATERAL Image", img_bilateral)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
