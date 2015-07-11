# -*- coding: UTF-8 -*- 

import cv2
import math 
import numpy as np 
import os
from PIL import Image

if __name__ == '__main__':

    # 顔判定で使うxmlファイルを指定する。
    cascade_path =  os.path.dirname(os.path.abspath(__file__)) + "/haarcascades/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_path)

    # 画像の読み込み
    img_src = cv2.imread("./image/yoshinobu.jpg", 1)

    # 結果を保存するための変数を用意しておく。
    img_edit = Image.open("./image/yoshinobu.jpg")

    # グレースケールに変換
    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

    #顔判定
    """ 
    minSize で顔判定する際の最小の四角の大きさを指定できる。
    (小さい値を指定し過ぎると顔っぽい小さなシミのような部分も判定されてしまう。)
    """
    faces  =  cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))

    # 顔があった場合
    if len(faces) > 0:

        # 複数の顔があった場合、１つずつ四角で囲っていく
        for face in faces:

            # 顔を切り抜く
            cut_face = img_edit.crop((face[0],
                                      face[1],
                                      face[0]+face[2],
                                      face[1]+face[3]))

            # 切り抜いた画像を1/20に縮小する。
            cut_face = cut_face.resize((int(face[2]/20), int(face[3]/20)), Image.LINEAR)

            # 縮小した画像を本のサイズに戻す。
            cut_face = cut_face.resize(face[2:], Image.LINEAR)

            # 元の画像に加工した顔画像を貼り付ける。
            img_edit.paste(cut_face, tuple(face[:2]))

    
    #pillow用のデータをOpenCVデータに変換
    img_dst = np.asarray(img_edit)

    # 表示
    cv2.imshow("Show MOSAIC FACES Image", img_dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
