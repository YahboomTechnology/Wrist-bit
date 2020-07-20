from microbit import *
import neopixel
import radio
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
    gesture = accelerometer.current_gesture()
    if gesture == "face up" and button_a.is_pressed() is False and button_b.is_pressed() is False:
        radio.send('0')
        display.show(Image.NO)
    elif gesture == "shake":
        RGBLight_more_show(0, 1, 'Black')
        radio.send('I')
    elif gesture == "up":
        radio.send('D')
        display.show(Image.ARROW_S)
    elif gesture == "down":
        radio.send('C')
        display.show(Image.ARROW_N)
    elif gesture == "left":
        radio.send('B')
        display.show(Image.ARROW_W)
    elif gesture == "right":
        radio.send('A')
        display.show(Image.ARROW_E)
    if button_a.is_pressed() is True and button_b.is_pressed() is False:
        sleep(100)
        if button_a.is_pressed() is True and button_b.is_pressed() is False:
            radio.send('E')
            RGBLight_more_show(0, 1, 'Red')
    elif button_a.is_pressed() is False and button_b.is_pressed() is True:
        sleep(100)
        if button_a.is_pressed() is False and button_b.is_pressed() is True:
            radio.send('F')
            RGBLight_more_show(0, 1, 'Green')
    elif button_a.is_pressed() is True and button_b.is_pressed() is True:
        sleep(100)
        if button_a.is_pressed() is True and button_b.is_pressed() is True:
            radio.send('G')
            RGBLight_more_show(0, 1, 'Blue')


display.show(Image.HEART)
np = neopixel.NeoPixel(pin1, 1)
radio.on()
radio.config(group=1)

while True:
    send_control()


