# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    # 画像の読み込み
    img_src = cv2.imread("./image/kinoko.jpg", 1)

    # RGBからHSVに変換
    img_hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)

    # 表示
    cv2.imshow("Show HSV Image", img_hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
