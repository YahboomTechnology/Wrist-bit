# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import tinybit
import radio
import neopixel

Red = (255, 0, 0)
Orange = (255, 165, 0)
Yellow = (255, 255, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Violet = (148, 0, 211)
White = (255, 255, 255)
Black = (0, 0, 0)
color_lib = {'Red': Red, 'Orange': Orange, 'Yellow': Yellow, 'Green': Green,
             'Blue': Blue, 'Violet': Violet, 'White': White, 'Black': Black}

def RGBLight_more_show(first, num, color):
    global np
    np.clear()
    for i in range(first, first + num):
        np[i] = color_lib[color]
    np.show()

np = neopixel.NeoPixel(pin12, 2)
display.show(Image.HAPPY)
radio.on()
radio.config(group=1)
while True:
    incoming = radio.receive()
    if incoming == 'A':
        tinybit.car_run(100, 100)
    elif incoming == 'B':
        tinybit.car_back(100, 100)
    elif incoming == 'C':
        tinybit.car_spinleft(100, 100)
    elif incoming == 'D':
        tinybit.car_spinright(100, 100)
    elif incoming == '0':
        tinybit.car_stop()

    if incoming == 'E':
        tinybit.car_HeadRGB(255, 0, 0)
        RGBLight_more_show(0, 2, 'Red')
    elif incoming == 'F':
        tinybit.car_HeadRGB(0, 255, 0)
        RGBLight_more_show(0, 2, 'Green')
    elif incoming == 'G':
        tinybit.car_HeadRGB(0, 0, 255)
        RGBLight_more_show(0, 2, 'Blue')
    elif incoming == 'I':
        tinybit.car_HeadRGB(0, 0, 0)
        RGBLight_more_show(0, 2, 'Black')
