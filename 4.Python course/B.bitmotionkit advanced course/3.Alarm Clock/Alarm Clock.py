from microbit import *
import music


sun = Image("90909:"
            "09990:"
            "99999:"
            "09990:"
            "90909")

moon = Image("00990:"
             "09900:"
             "09900:"
             "09900:"
             "00990")


while True:
    value = display.read_light_level()
    if value < 20:
        pin2.write_analog(0)
        display.show(moon)
        music.stop()
    else:
        pin2.write_analog(536)
        display.show(sun)
        music.play(music.ENTERTAINER)
    value = 0
