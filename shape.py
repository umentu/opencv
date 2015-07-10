# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':
    
    # シャープの度合い
    k = 10.0
    # シャープ化するためのオペレータ
    shape_operator = np.array([[0,        -k, 0],
                  [-k, 1 + 4 * k, -k],
                  [0,         -k, 0]])


    # 画像の読み込み
    img_src = cv2.imread("./image/hanabi.jpg", 3)

    # 作成したオペレータを基にシャープ化
    img_tmp = cv2.filter2D(img_src, -1, shape_operator)
    img_shape = cv2.convertScaleAbs(img_tmp)

    # 表示
    cv2.imshow("Show SHAPE Image", img_shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
