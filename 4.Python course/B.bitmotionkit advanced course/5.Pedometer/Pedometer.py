from microbit import *
import microbit
display.show(Image.HAPPY)
step = 0
x1 = accelerometer.get_y()

while True:
    x2 = accelerometer.get_y()
    if x2 - x1 > 150:
        step = step + 1
    x1 = x2
    microbit.sleep(500)
    if button_a.is_pressed():
        display.scroll(str(step))
