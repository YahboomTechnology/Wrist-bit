from microbit import *
import superbit
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

np = neopixel.NeoPixel(pin12, 4)
display.show(Image.HAPPY)
radio.on()
radio.config(group=1)
superbit.servo270(superbit.S1, 0)

while True:
    incoming = radio.receive()
    if incoming == 'A':
        superbit.motor_control(superbit.M1, 255, 0)
        superbit.motor_control(superbit.M3, 255, 0)
    elif incoming == 'B':
        superbit.motor_control(superbit.M1, -255, 0)
        superbit.motor_control(superbit.M3, -255, 0)
    elif incoming == 'C':
        superbit.motor_control(superbit.M1, -100, 0)
        superbit.motor_control(superbit.M3, 100, 0)
    elif incoming == 'D':
        superbit.motor_control(superbit.M1, 100, 0)
        superbit.motor_control(superbit.M3, -100, 0)
    elif incoming == '0':
        superbit.motor_control(superbit.M1, 0, 0)
        superbit.motor_control(superbit.M3, 0, 0)
    elif incoming == 'E':
        superbit.servo270(superbit.S1, 0)
        RGBLight_more_show(0, 4, 'Red')
    elif incoming == 'F':
        RGBLight_more_show(0, 4, 'Green')
    elif incoming == 'H':
        superbit.servo270(superbit.S1, 60)
        RGBLight_more_show(0, 4, 'Yellow')
    elif incoming == 'I':
        RGBLight_more_show(0, 4, 'Black')