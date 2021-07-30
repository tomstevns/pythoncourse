#!/usr/bin/env python

'''
Retrofying

USAGE:
    retrofyme.py
'''

import cv2
import numpy as np
import scipy.spatial as sp


def _c64_colors():
    # From https://upload.wikimedia.org/wikipedia/commons/6/65/Commodore64_palette.png
    # with Seashore, the 16 C64 colors
    black = [0, 0, 0]
    white = [255, 255, 255]
    red = [154, 76, 67]
    cyan = [122, 194, 200]
    purple = [157, 90, 165]
    green = [103, 171, 95]
    blue = [82, 73, 156]
    yellow = [202, 212, 137]
    a = [156, 103, 58]
    b = [106, 82, 12]
    c = [197, 126, 119]
    d = [99, 99, 99]
    e = [139, 139, 139]
    f = [164, 226, 157]
    g = [139, 130, 205]
    hc = [175, 175, 175]

    c64_colors = [black, white, red, cyan, purple, green, blue, yellow, a, b,
                  c, d, e, f, g, hc]
    return np.array(c64_colors)


def create_tree(colors):
    return sp.cKDTree(colors)


def query_tree(small_image, tree):
    h, w, d = small_image.shape

    small_image_lst = small_image.reshape(h * w, d)
    # get Euclidean distance and index of each C64 color in tree
    _, result = tree.query(small_image_lst)

    for idx, c in enumerate(_c64_colors()):
        small_image_lst[result == idx] = c
    return small_image_lst


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    w, h = (320, 200)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

    tree = create_tree(_c64_colors())

    while True:
        ret, img = cap.read()
        _ = query_tree(img, tree)

        img_large = cv2.resize(img, (1280, 800),
                               interpolation=cv2.INTER_NEAREST)
        cv2.imshow('Retrofied', img_large)

        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
