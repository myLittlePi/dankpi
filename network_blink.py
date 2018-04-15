#!/usr/bin/env python
import blinkt
import requests
import time
import threading
import random

RED = 255,0,0
GREEN = 0,180,0
YELLOW = 55,55,0
WHITE = 120,120,120


def random_color():
    return random.randint(0,255), random.randint(0,255), random.randint(0,255)


def show_color(x, color, t=0.2):
    blinkt.set_clear_on_exit()
    blinkt.set_pixel(x,color[0], color[1], color[2],t)
    blinkt.show()


def request_vg(is_success):
    is_success[0] = requests.get("http://vg.no").status_code == requests.codes.ok


show_color(0,WHITE)

is_internet = [False]
t = threading.Thread(target=request_vg, args=(is_internet,))
t.start()

for i in range(50):
    show_color(1, random_color())
    if(is_internet[0]):
        break
    time.sleep(0.1)

show_color(1, GREEN if is_internet[0] else YELLOW)

t.join()
request_result_color = GREEN if is_internet else RED

show_color(2, request_result_color)
time.sleep(90)
