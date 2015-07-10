# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    # 画像の読み込み
    img_src = cv2.imread("./image/kura.jpg", 1)

    # マスク画像の読み込み
    img_mask = cv2.imread("./image/heart.jpg", 0)

    img_masked = cv2.bitwise_not(img_src, img_src, mask=img_mask )


    # 表示
    cv2.imshow("Show MASK Image", img_masked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
