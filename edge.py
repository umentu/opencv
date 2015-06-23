# -*- coding: utf-8 -*-

import cv2

if __name__ == '__main__':

    # 画像の読み込み
    gray = cv2.imread("./image/slack_botter.png", 0)
    # エッジの抽出
    edge = cv2.Canny(gray, 0, 200)

    # 表示
    cv2.imshow("Show Image", edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
