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
global speed
speed = 0

while True:
    value = radio.receive()
    if value == 'A':
        if speed < 255:
            speed = speed + 5
            sleep(20)
        else:
            speed = 255
        superbit.motor_control(superbit.M1, speed, 0)
        superbit.motor_control(superbit.M3, speed, 0)
    elif value == 'B':
        if speed < 255:
            speed = speed + 5
            sleep(20)
        else:
            speed = 255
        superbit.motor_control(superbit.M1, -1*speed, 0)
        superbit.motor_control(superbit.M3, -1*speed, 0)
    elif value == 'C':
        superbit.motor_control(superbit.M1, -50, 0)
        superbit.motor_control(superbit.M3, 50, 0)
    elif value == 'D':
        superbit.motor_control(superbit.M1, 50, 0)
        superbit.motor_control(superbit.M3, -50, 0)
    elif value == '0':
        speed = 0
        angle = accelerometer.get_z()
        if angle >= -300 and angle <= 300:
            superbit.motor_control(superbit.M1, 0, 0)
            superbit.motor_control(superbit.M3, 0, 0)
        elif angle > 300:
            superbit.motor_control(superbit.M1, 30, 0)
            superbit.motor_control(superbit.M3, 30, 0)
        else:
            superbit.motor_control(superbit.M1, -30, 0)
            superbit.motor_control(superbit.M3, -30, 0)
    elif value == 'E':
        RGBLight_more_show(0, 4, 'Red')
    elif value == 'F':
        RGBLight_more_show(0, 4, 'Green')
    elif value == 'G':
        RGBLight_more_show(0, 4, 'Blue')
    elif value == 'H':
        RGBLight_more_show(0, 4, 'Yellow')
    elif value == 'I':
        RGBLight_more_show(0, 4, 'Black')
