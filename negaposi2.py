# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    # 画像の読み込み
    img_src = cv2.imread("./image/sora2.jpg", 1)

    # 画像のネガポジ化
    img_negaposi = 255 - img_src

    # 表示
    cv2.imshow("Show NEGAPOSI Image", img_negaposi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
