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

    # 移動平均を計算して出力する。
    img_blur = cv2.blur(img_src, average_square)

    # 表示
    cv2.imshow("Show BLUR Image", img_blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
