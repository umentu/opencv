# -*- coding: utf-8 -*-

import cv2

if __name__ == '__main__':
    
    # 画像読み込み
    img_src = cv2.imread("./image/karasu.jpg", 1)
    # 複数色のチャンネルを分割して配列で取得
    # img_bgr[0] に青, img_bgr[1]に緑,img_bgr[2]に赤が入る。
    img_bgr = cv2.split(img_src)

    # 青->赤, 緑->青, 青->緑
    img_cng = cv2.merge((img_bgr[1],img_bgr[2],img_bgr[0]))

    # 表示
    cv2.imshow("Show Image", img_bgr[2])
    cv2.waitKey(0)
    cv2.destroyAllWindows()    