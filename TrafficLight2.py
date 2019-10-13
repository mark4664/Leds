#!/usr/bin/python3

# Peter Normington
# 2019-10-10

from gpiozero import LED, Button
from time import sleep
import LEDBoard

Class TrafficLight:
    def __init__(self):
            # Set up the board configuration
            tl_pin_colour = {
            "Green":17,
            "Yellow":18,
            "Red":19,
        }
    tlboard = LEDBoard(tl_pin_colour.{})

    # Run util stopped by keyboard interrupt....Ctrl + C
    while True:            
        tlboard.test_led("Red",4)
        tlboard.test_led("Yellow",3)
        tlboard.test_led("Green",4)
        tlboard.test_led("Yellow",2)
