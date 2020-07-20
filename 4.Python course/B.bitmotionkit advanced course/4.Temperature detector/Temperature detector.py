from microbit import *
import microbit
import music


while True:
    value = temperature()
    microbit.sleep(500)
    if value > 10 and value < 30:
        pin2.write_analog(0)
        display.scroll(str(value))
    elif value >= 30 or value <= 10:
        pin2.write_analog(1023)
        music.play(music.ENTERTAINER)
        display.scroll(str(value))


