# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    # 画像の読み込み
    img_src = cv2.imread("./image/te.jpg", 0)

    # 4近傍の定義
    neiborhood4 = np.array([[0, 1, 0],
                            [1, 1, 1],
                            [0, 1, 0]],
                            np.uint8)

    # 8近傍の定義
    neiborhood8 = np.array([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]],
                            np.uint8)

    # 近傍8のオープニング
    img_dst = cv2.morphologyEx(img_src, cv2.MORPH_OPEN, neiborhood8)

    # 近傍8のクロージング
    img_dst = cv2.morphologyEx(img_dst, cv2.MORPH_CLOSE, neiborhood8)

    # 表示
    cv2.imshow("Show OPENING_CLOSING Image", img_dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
