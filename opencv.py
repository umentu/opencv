# -*- coding: utf-8 -*-

import cv2
import numpy as np

def main():

    gray = cv2.imread("./image/slack_botter.png", 0)
    edge = cv2.Canny(gray, 100, 300)
    cv2.imshow("Show Edge Image", edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()