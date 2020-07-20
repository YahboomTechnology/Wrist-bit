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

radio.on()
radio.config(group=1)
display.show(Image.HAPPY)
np = neopixel.NeoPixel(pin12, 4)
while True:
    value = radio.receive()
    if value == 'A':
        superbit.motor_control_dual(superbit.M1, superbit.M3, 255, 255, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, 255, 255, 0)
    elif value == 'B':
        superbit.motor_control_dual(superbit.M1, superbit.M3, -255, -255, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, -255, -255, 0)
    elif value == 'C':
        superbit.motor_control_dual(superbit.M1, superbit.M3, -100, 100, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, -100, 100, 0)
    elif value == 'D':
        superbit.motor_control_dual(superbit.M1, superbit.M3, 100, -100, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, 100, -100, 0)
    elif value == 'E':
        RGBLight_more_show(0, 4, 'Red')
        superbit.motor_control_dual(superbit.M1, superbit.M3, -255, 255, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, 255, -255, 0)
    elif value == 'F':
        RGBLight_more_show(0, 4, 'Green')
        superbit.motor_control_dual(superbit.M1, superbit.M3, 255, -255, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, -255, 255, 0)
    elif value == 'G':
        RGBLight_more_show(0, 4, 'Blue')
        superbit.motor_control_dual(superbit.M1, superbit.M3, 50, 50, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, 255, -255, 0)
    elif value == 'I':
        RGBLight_more_show(0, 4, 'Black')
    elif value == '0':
        superbit.motor_control_dual(superbit.M1, superbit.M3, 0, 0, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, 0, 0, 0)
