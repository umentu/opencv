# -*- coding: UTF-8 -*- 

import cv2
import math 
import numpy as np 
import os
from PIL import Image

class Face(object):
    """
    顔認識して色々遊ぶ関数
    """

    def get_faces(self, image, min_size=(100, 100)):
        """
        顔を取得するメソッド。
        image: cv2.imreadで読み取った変数
        min_size: 顔判定する最小サイズの指定。
        """

        cascade_path =  os.path.dirname(os.path.abspath(__file__)) + "/haarcascades/haarcascade_frontalface_alt.xml"
        cascade = cv2.CascadeClassifier(cascade_path)

        enclosed_faces = image

        #グレースケール
        frame_gray =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #顔判定
        """ 
        minSize で顔判定する際の最小の四角の大きさを指定できる。
        (小さい値を指定し過ぎると顔っぽい小さなシミのような部分も判定されてしまう。)
        """
        faces  =  cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=1, minSize=min_size)

        return faces

    def get_enclosed_faces(self, image, min_size=(100, 100)):
        """
        顔を四角で囲うメソッド。
        image: cv2.imreadで読み取った変数
        min_size: 顔判定する最小サイズの指定。        
        """

        # 出力結果を格納する変数
        enclosed_faces = image

        # 顔認識
        faces = self.get_faces(image, min_size)

        if len(faces) > 0:

            # 顔認識の枠の色
            color = (255, 0, 0)

            # 複数の顔があった場合、１つずつ四角で囲っていく
            for face in faces:

                # faceには(四角の左上のx座標, 四角の左上のy座標, 四角の横の長さ, 四角の縦の長さ) が格納されている。

                # 囲う四角の左上の座標
                coordinates = tuple(face[0:2])
                # (囲う四角の横の長さ, 囲う四角の縦の長さ)
                length = tuple(face[0:2] + face[2:4])

                # 四角で囲う処理
                cv2.rectangle(enclosed_faces, coordinates, length, color, thickness=3)

        return enclosed_faces


    def get_mosaic_faces(self, image, min_size=(100, 100), ratio=20):
        """
        顔をモザイクで覆うメソッド。
        image: cv2.imreadで読み取った変数
        min_size: 顔判定する最小サイズの指定。
        """

        # イメージをpillowで扱うことのできる形式に変換しておく。
        img_edit = Image.fromarray(image)

        # 顔認識
        faces = self.get_faces(image, min_size)

        # 顔があった場合。
        if len(faces) > 0:

            # 複数の顔があった場合、１つずつ四角で囲っていく。
            for face in faces:

                # 顔を切り抜く。
                cut_face = img_edit.crop((face[0],
                                          face[1],
                                          face[0]+face[2],
                                          face[1]+face[3]))

                # 切り抜いた画像を1/20に縮小する。
                cut_face = cut_face.resize((int(face[2]/ratio), int(face[3]/ratio)), Image.LINEAR)

                # 縮小した画像を本のサイズに戻す。
                cut_face = cut_face.resize(face[2:], Image.LINEAR)

                # 元の画像に加工した顔画像を貼り付ける。
                img_edit.paste(cut_face, tuple(face[:2]))

        
        #pillow用のデータをOpenCVデータに変換
        img_opencv = np.asarray(img_edit)

        return img_opencv


    def get_edge_faces(self, image, min_size=(100, 100)):
        """
        顔をエッジ化するメソッド。
        image: cv2.imreadで読み取った変数
        min_size: 顔判定する最小サイズの指定。
        """

        # イメージをpillowで扱うことのできる形式に変換しておく。
        img_edit = Image.fromarray(image)

        # 顔認識
        faces = self.get_faces(image, min_size)

        # 顔があった場合。
        if len(faces) > 0:

            # 複数の顔があった場合、１つずつ四角で囲っていく。
            for face in faces:

                # 顔の部分の左上のx,y座標(微調整)
                face_x = face[0] - 50
                face_y = face[1] - 100
                # 顔の部分の横の長さと縦の長さ(微調整)
                face_width = face[0]+face[2] + 50
                face_height = face[1]+face[3] + 100

                # 顔を切り抜く
                cut_face = img_edit.crop((face_x,
                                          face_y,
                                          face_width,
                                          face_height))

                # OpenCV用のデータに変換
                cut_face = np.asarray(cut_face)

                # 2次微分オペレータを使って画像のエッジを検出
                img_tmp = cv2.Laplacian(cut_face, cv2.CV_32F, 16)
                cut_face = cv2.convertScaleAbs(img_tmp)

                # pillow用のデータに変換
                cut_face = Image.fromarray(cut_face)

                # 元の画像に加工した顔画像を貼り付ける。
                img_edit.paste(cut_face, tuple((face_x, face_y)))

        #pillow用のデータをOpenCVデータに変換
        img_opencv = np.asarray(img_edit)

        return img_opencv

    def get_negaposi_faces(self, image, min_size=(100, 100)):
        """
        顔をネガポジ変換するメソッド。
        image: cv2.imreadで読み取った変数
        min_size: 顔判定する最小サイズの指定。
        """

        # イメージをpillowで扱うことのできる形式に変換しておく。
        img_edit = Image.fromarray(image)

        # 顔認識
        faces = self.get_faces(image, min_size)

        # 顔があった場合。
        if len(faces) > 0:

            # 複数の顔があった場合、１つずつ四角で囲っていく。
            for face in faces:

                # 顔の部分の左上のx,y座標(微調整)
                face_x = face[0] - 50
                face_y = face[1] - 100
                # 顔の部分の横の長さと縦の長さ(微調整)
                face_width = face[0]+face[2] + 50
                face_height = face[1]+face[3] + 100

                # 顔を切り抜く
                cut_face = img_edit.crop((face_x,
                                          face_y,
                                          face_width,
                                          face_height))

                # OpenCV用のデータに変換
                cut_face = np.asarray(cut_face)

                cut_face = 255 - cut_face

                # pillow用のデータに変換
                cut_face = Image.fromarray(cut_face)

                # 元の画像に加工した顔画像を貼り付ける。
                img_edit.paste(cut_face, tuple((face_x, face_y)))

        
        #pillow用のデータをOpenCVデータに変換
        img_opencv = np.asarray(img_edit)

        return img_opencv

    def get_smileman_faces(self, image, min_size=(100, 100)):
        """
        顔を笑い男マークにするメソッド。
        image: cv2.imreadで読み取った変数
        min_size: 顔判定する最小サイズの指定。
        """

        # イメージをpillowで扱うことのできる形式に変換しておく。
        img_edit = Image.fromarray(image)

        # 笑い男マーク呼び出し
        img_smileman = Image.open("./image/smileman.jpg")

        # OpenCV用のデータに変換
        img_smileman = np.asarray(img_smileman)

        # pillowではRGB、OpenCVではGBRのため、色の順番を並べ替え。
        img_bgr = cv2.split(img_smileman)
        img_smileman = cv2.merge((img_bgr[2], img_bgr[1], img_bgr[0]))

        # pillow用のデータに変換
        img_smileman = Image.fromarray(img_smileman)

        # 顔認識
        faces = self.get_faces(image, min_size)

        # 顔があった場合。
        if len(faces) > 0:

            # 複数の顔があった場合、１つずつ四角で囲っていく。
            for face in faces:

                # 顔の部分の左上のx,y座標(微調整)
                face_x = face[0] -50
                face_y = face[1]
                # 顔の部分の横の長さと縦の長さ(微調整)
                face_height = face[1]+face[3] - 50

                tmp_smileman = img_smileman.resize((face_height, face_height), Image.LINEAR)

                # 元の画像に加工した顔画像を貼り付ける。
                img_edit.paste(tmp_smileman, tuple((face_x, face_y)))

        #pillow用のデータをOpenCVデータに変換
        img_opencv = np.asarray(img_edit)

        return img_opencv


if __name__ == '__main__':
    
    face = Face()

    """
    image = cv2.imread("./image/physicists.jpg", 1)
    mosaic_faces = face.get_mosaic_faces(image, min_size=(10, 10))

    # 表示
    cv2.imshow("Show MOSAIC Image", mosaic_faces)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """

    # カメラからキャプチャー
    cap = cv2.VideoCapture(0)

    while(True):

        # 動画ストリームからフレームを取得
        ret, frame = cap.read()

        # モザイク処理
        # frame = face.get_mosaic_faces(frame, ratio=40)
        # cv2.imshow('MOSAIC FACE', frame)

        # エッジ
        frame = face.get_edge_faces(frame)
        cv2.imshow('EDGE FACE', frame)

        # ネガポジ変換
        # frame = face.get_negaposi_faces(frame)
        # cv2.imshow("NEGAPOSI FACE", frame)

        # 笑い男
        # frame = face.get_smileman_faces(frame)
        # cv2.imshow("SMILEMAN FACE", frame)


        # qを押したら終了。
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
