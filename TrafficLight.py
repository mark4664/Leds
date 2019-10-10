#!/usr/bin/python3

# Script name: TrafficLight.py
# Uses the red yellow and green LEDs to simulate a road traffic light
# 
# MGB
# 2019-10-10

from gpiozero import LED, Button    #Using gpiozero library
from time import sleep                     #Use sleep funtion for timing, time is in seconds

grn_led=LED(17)       # Assign pin 17 to the green led.
yel_led=LED(18)        # Assign pin 18 to the yellow led.
red_led=LED(19)       # Assign pin 19 to the red led.
blu_led=LED(20)       # Assign pin 20 to the blue led.
pb1=Button(21)        # Assign pin 21 to push button 1.

print("Traffic Light simulation programme")

while True:            # Run util stopped by keyboard interrupt....Ctrl + C
    red.on()             # Turn LED ON, set output pin to +3.3v
    sleep(4)             # Wait 3 seconds
    yel_led.on()       # Repeat for the other LEDs
    sleep(1)
    red_led.off()
    yel_led.off()
    grn_led.on()
    sleep(4)
    grn_led.off()
    yel_led.on()
    sleep(1.5)
    yel_led.off()
 

print("All done!")