# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    # 画像の読み込み
    img_src = cv2.imread("./image/te.jpg", 1)

    # グレースケールに変換
    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

    # 二値変換
    thresh = 40
    max_pixel = 255
    ret, img_dst = cv2.threshold(img_gray,
                                 thresh,
                                 max_pixel,
                                 cv2.THRESH_BINARY)

    # 表示
    cv2.imshow("Show BINARIZATION Image", img_dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
