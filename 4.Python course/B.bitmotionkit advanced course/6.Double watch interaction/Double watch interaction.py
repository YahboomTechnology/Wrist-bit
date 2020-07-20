from microbit import *
import radio
import neopixel
import microbit
watch = Image("00900:"
              "09990:"
              "09090:"
              "09990:"
              "00900")

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


def send_control():
    global flag
    global send
    if button_a.is_pressed() is True and button_b.is_pressed() is False:
        microbit.sleep(100)
        if button_a.is_pressed() is True and button_b.is_pressed() is False:
            flag = flag + 1
            if flag > 5:
                flag = 0
    elif button_a.is_pressed() is False and button_b.is_pressed() is True:
        microbit.sleep(100)
        if button_a.is_pressed() is False and button_b.is_pressed() is True:
            send = 1
    elif button_a.is_pressed() is True and button_b.is_pressed() is True:
        microbit.sleep(100)
        if button_a.is_pressed() is True and button_b.is_pressed() is True:
            RGBLight_more_show(0, 1, "Black")

    x, y, z = accelerometer.get_values()
    if x+y+z > 900:
        microbit.sleep(1000)
        if flag == 5:
            radio.send('Z')

def display_send():
    global flag
    global send
    if flag == 1:
        display.show(Image.ARROW_N)
        if send == 1:
            radio.send('N')
            send = 0
    elif flag == 2:
        display.show(Image.ARROW_S)
        if send == 1:
            radio.send('S')
            send = 0
    elif flag == 3:
        display.show(Image.ARROW_E)
        if send == 1:
            radio.send('E')
            send = 0
    elif flag == 4:
        display.show(Image.ARROW_W)
        if send == 1:
            radio.send('W')
            send = 0
    elif flag == 5:
        display.show(Image.CHESSBOARD)
    elif flag == 0:
        display.show(watch)

flag = 0
send = 0
np = neopixel.NeoPixel(pin1, 1)
display.show(watch)
radio.on()
radio.config(group=1)

while True:
    send_control()
    display_send()
    value = radio.receive()
    if value == 'Z':
        flag = 0
        pin2.write_analog(1023)
        microbit.sleep(1000)
        pin2.write_analog(0)
    elif value == "N":
        flag = 1
        RGBLight_more_show(0, 1, 'Red')
    elif value == "S":
        flag = 2
        RGBLight_more_show(0, 1, 'Green')
    elif value == "E":
        flag = 3
        RGBLight_more_show(0, 1, 'Blue')
    elif value == "W":
        flag = 4
        RGBLight_more_show(0, 1, 'Violet')
