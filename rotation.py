# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    # 画像読み込み
    img_src = cv2.imread("./image/slack_botter.png", 1)

    # 画像の中心位置
    # 今回は画像サイズの中心をとっている
    center = tuple(np.array([img_src.shape[1] * 0.5, img_src.shape[0] + 0.5]))

    # 画像サイズの取得(横, 縦)
    size = tuple(np.array([img_src.shape[1], img_src.shape[0]]))

    # 回転させたい角度
    # ラジアンではなく角度(°)
    angle = 45.0

    # 拡大比率
    scale = 1.0

    # 回転変換行列の算出
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    # アフィン変換
    img_rot = cv2.warpAffine(img_src, rotation_matrix, size, flags=cv2.INTER_CUBIC)

    # 表示
    cv2.imshow("Show ROTATION Image", img_rot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
