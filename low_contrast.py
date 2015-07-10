# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    # ルックアップテーブルの生成
    min_table = 100
    max_table = 192
    diff_table = max_table - min_table
    look_up_table = np.arange(256, dtype = 'uint8' )

    for i in range(0, 255):

        look_up_table[i] = min_table + i * (diff_table) / 255

    # 画像の読み込み
    img_src = cv2.imread("./image/akai_tsuki.jpg", 1)

    # コントラストを低減
    img_contrast = cv2.LUT(img_src, look_up_table)

    # 表示
    cv2.imshow("Show LOW CONTRAST Image", img_contrast)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
