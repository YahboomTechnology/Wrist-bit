from microbit import *
import neopixel
import microbit

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

display.show(Image.HAPPY)
np = neopixel.NeoPixel(pin1, 1)
while True:
    RGBLight_more_show(0, 1, 'Red')
    microbit.sleep(1000)
    RGBLight_more_show(0, 1, 'Green')
    microbit.sleep(1000)
    RGBLight_more_show(0, 1, 'Blue')
    microbit.sleep(1000)
    RGBLight_more_show(0, 1, 'White')
    microbit.sleep(1000)