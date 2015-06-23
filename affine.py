# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    # 画像読み込み
    img_src = cv2.imread("./image/slack_botter.png", 0)

    # 画像サイズの取得(横, 縦)
    size = tuple(np.array([img_src.shape[1], img_src.shape[0]]))

    # 回転させたい角度
    rad = np.pi / 4
    # x軸方向に平行移動させたい距離
    move_x = 0
    # y軸方向に平行移動させたい距離
    move_y = img_src.shape[0] * -0.5

    matrix = [
                [np.cos(rad),  -1 * np.sin(rad), move_x],
                [np.sin(rad),   np.cos(rad), move_y]
            ]

    affine_matrix = np.float32(matrix)


    img_afn = cv2.warpAffine(img_src, affine_matrix, size, flags=cv2.INTER_LINEAR)

    # 表示
    cv2.imshow("Show AFFINE Image", img_afn)
    cv2.waitKey(0)
    cv2.destroyAllWindows()