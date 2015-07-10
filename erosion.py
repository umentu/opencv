# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    # 画像の読み込み
    img_src = cv2.imread("./image/sunaarashi.jpg", 1)

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

    # 8近傍で縮小処理
    img_erosion = cv2.erode(img_src,
                              neiborhood8,
                              iterations=1)

    # 表示
    cv2.imshow("Show EROSION Image", img_erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
