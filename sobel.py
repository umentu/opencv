# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':
    
    # 画像の読み込み
    img_src = cv2.imread("./image/kura.jpg", 1)

    # 横方向のSobelオペレータのエッジ検出
    img_tmp = cv2.Sobel(img_src, cv2.CV_32F, 1, 0)

    img_sobel = cv2.convertScaleAbs(img_tmp)

    # 表示
    cv2.imshow("Show SOBEL Image", img_sobel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
