# -*- coding: utf-8 -*-

import cv2
import numpy as np

def get_lookuptable_r(x):
    """疑似カラー処理のR成分用"""
    
    if x < 128:
        return 0
    elif x < 192:
        return 4 * x - 512
    else:
        return 256
    
def get_lookuptable_g(x):
    """疑似カラー処理のG成分用"""
    
    if x < 64:
        return 4 * x 
    elif x < 192:
        return 256
    else:
        return -4 * x + 1024

def get_lookuptable_b(x):
    """疑似カラー処理のB成分用"""
    
    if x < 64:
        return 256
    elif x < 128:
        return -4 * x + 512
    else:
        return 0 



if __name__ == '__main__':

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
    look_up_table_r = np.ones((256, 1), dtype = 'uint8' ) * 0
    look_up_table_g = np.ones((256, 1), dtype = 'uint8' ) * 0
    look_up_table_b = np.ones((256, 1), dtype = 'uint8' ) * 0

    for i in range(256):

        各RGBごとのルックアップテーブルを作成
        look_up_table_r[i][0] = get_lookuptable_r(i)
        look_up_table_g[i][0] = get_lookuptable_g(i)
        look_up_table_b[i][0] = get_lookuptable_b(i)


    # 画像の読み込み
    img_src = cv2.imread("./image/sora2.jpg", 1)
    # 複数色のチャンネルを分割して配列で取得
    # img_bgr[0] に青, img_bgr[1]に緑,img_bgr[2]に赤が入る。

    # 読み込んだ画像のグレースケール化
    img_gry = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

    # 擬似カラー化
    img_pcp_r = cv2.LUT(img_gry, look_up_table_r)
    img_pcp_g = cv2.LUT(img_gry, look_up_table_g)
    img_pcp_b = cv2.LUT(img_gry, look_up_table_b)

    # 各擬似カラー化した画像をマージ
    img_mrg = cv2.merge((img_pcp_b,img_pcp_g,img_pcp_r))    

    # 表示
    cv2.imshow("Show Pseudo Color Processing Image", img_mrg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

