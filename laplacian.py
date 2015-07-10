# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':
    
    # 画像の読み込み
    img_src = cv2.imread("./image/kura.jpg", 3)

    # 2次微分オペレータを使って画像のエッジを検出
    img_tmp = cv2.Laplacian(img_src, cv2.CV_32F, 8)
    img_lap = cv2.convertScaleAbs(img_tmp)

    # 表示
    cv2.imshow("Show LAPLACIAN Image", img_lap)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
