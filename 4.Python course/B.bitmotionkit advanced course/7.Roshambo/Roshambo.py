from microbit import *
import microbit
import random

scissors = Image("99009:"
                 "99090:"
                 "00900:"
                 "99090:"
                 "99009")

stone = Image("00000:"
              "09990:"
              "09090:"
              "09990:"
              "00000")

cloth = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999")

display.show(Image.HAPPY)

while True:
    x, y, z = accelerometer.get_values()
    if x+y+z > 900:
        microbit.sleep(800)
        value = random.randint(0, 2)
        if value == 0:
            display.show(scissors)
        elif value == 1:
            display.show(stone)
        elif value == 2:
            display.show(cloth)
