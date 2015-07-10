# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    # 画像読み込み
    img_src = cv2.imread("./image/sora.jpg", 1)

    # グレースケール
    img_gry = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

    # ヒストグラムの均一化
    img_eqh = cv2.equalizeHist(img_gry)

    # ヒストグラム表示用のイメージを作成
    img_histgram = np.zeros([100, 256]).astype("uint8")
    rows, cols = img_histgram.shape

    # 度数分布を求める

    # 次元ごとの度数分布のサイズ
    hdims = [256]

    # 各次元の度数分布の最小値と最大値
    hranges = [0, 256]

    histgram = cv2.calcHist([img_eqh], [0], None, hdims, hranges)

    # 度数の最大値を取得
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(histgram)

    for i in range(0, 255):

        # 算出した度数分布の値を取得する
        v = histgram[i]

        # 描画する
        cv2.line(img_histgram,
                 (i, rows),
                 (i, rows - rows * (v / max_val)),
                 (255, 255, 255))

    # 表示
    # cv2.imshow("Show GRAY Image", img_gry)
    # cv2.imshow("Show EQUALIZE HISTGRAM Image", img_eqh)
    cv2.imshow("Show HISTGRAM Image", img_histgram)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
