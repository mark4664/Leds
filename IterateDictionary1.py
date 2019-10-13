#!/usr/bin/python3

# IterateDictionary1.py
# MGB
# 2019-10-12

# Iteration of a dictionary


Leds = {'red': 17, 'yellow': 18, 'green': 19, 'blue': 20}

for eachLed in Leds.keys():
    print(eachLed, '->', Leds[eachLed])
    