#!/usr/bin/python3

# Script name: LedCheck1.py
# Check LEDs and push button are working / wired up correctly
# Each LED should flash on for 3/4 of a second and the state of the push button should be
# printed.
# MGB
# 2019-10-10

from gpiozero import LED, Button    #Using gpiozero library
from time import sleep                     #Use sleep funtion for timing, time is in seconds

grn_led=LED(17)       # Assign pin 17 to the green led.
yel_led=LED(18)        # Assign pin 18 to the yellow led.
red_led=LED(19)       # Assign pin 19 to the red led.
blu_led=LED(20)       # Assign pin 20 to the blue led.
pb1=Button(21)        # Assign pin 21 to push button 1.

print("LED Test programme")

while True:            # Run util stopped by keyboard interrupt....Ctrl + C
    grn_led.on()      # Turn LED ON, set output pin to +3.3v
    sleep(0.75)        # Wait 3/4 of a second
    grn_led.off()      # Turn LED OFF, set output pin to 0v
    yel_led.on()       # Repeat for the other LEDs
    sleep(0.75)
    yel_led.off()
    red_led.on()
    sleep(0.75)
    red_led.off()
    blu_led.on()
    sleep(0.75)
    blu_led.off()
    print("PB1",pb1.value) # Read the value of push button and print it.


print("All done!")