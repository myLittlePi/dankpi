#!/usr/bin/env python

import picamera
from picamera.array import PiRGBArray
import time
import sys
import numpy as np
import cv2
import blinkt

def take_pic():
    output = None
    with picamera.PiCamera() as camera:
        output = PiRGBArray(camera)
        camera.capture(output, format="rgb")
        camera.capture("test.bmp")
        print('Captured %dx%d image' % (output.array.shape[1], output.array.shape[0]))
        return output


def find_major_colors(pic_array, n_colors=8):
    pic_32 = np.float32(pic_array)
    pixels = pic_32.reshape((-1,3))
    print pic_32.shape
    print pixels.shape

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, .10)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, labels, centroids = cv2.kmeans(pixels, n_colors, criteria, 3, flags)

    palette = np.uint8(centroids)
    return palette


def show_colors(colors):
    def show_color(x, color, t=0.2):
        blinkt.set_clear_on_exit()
        blinkt.set_pixel(x,color[0], color[1], color[2],t)
        blinkt.show()
    for i, c in enumerate(colors):
        show_color(i, c)


pic = take_pic()
print "finding major colors"
major_colors = find_major_colors(pic.array)
print major_colors

show_colors(major_colors)
time.sleep(20)
