# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    # ガンマ定数の定義
    gamma = 2.0

    # ルックアップテーブルの生成
    """
    array([[0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
        ・・・・・・・・
           [0], dtype='uint8')
    のようなリストが生成される。
    """
    look_up_table = np.ones((256, 1), dtype = 'uint8' ) * 0

    for i in range(256):

        # ガンマ変換
        look_up_table[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)

    # 画像の読み込み
    img_src = cv2.imread("./image/sora2.jpg", 1)

    # ガンマ変換後の出力
    img_gamma = cv2.LUT(img_src, look_up_table)

    # 表示
    cv2.imshow("Show HSV Image", img_gamma)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
