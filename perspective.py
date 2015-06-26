# -*- coding: utf-8 -*-

import cv2
import numpy as np

if __name__ == '__main__':

    # 画像読み込み
    img_src = cv2.imread("./image/hanabi.jpg", 1)

    # 画像サイズの取得(横, 縦)
    size = tuple(np.array([img_src.shape[1], img_src.shape[0]]))

    perspective1 = np.float32([[250, 500],
                              [750, 500],
                              [750, 250],
                              [250, 250]])

    perspective2 = np.float32([[250, 750],
                              [750, 750],
                              [650, 500],
                              [350, 500]])

    psp_matrix = cv2.getPerspectiveTransform(perspective1,perspective2)

    img_psp = cv2.warpPerspective(img_src, psp_matrix, size)

    cv2.imwrite("./image/hanabi_psp.jpg", img_psp)


    # 表示
    cv2.imshow("Show PERSPECTIVE TRANSFORM Image", img_psp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

