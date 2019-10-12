#!/usr/bin/python3

# Peter Normington
# 2019-10-11
                                                                                                                                                           
from gpiozero import LED, Button
from time import sleep          

class LEDBoard:
    def __init__(self):
        
        self.pin_colour = {
            "Green":17,
            "Yellow":18,
            "Red":19,
            "Blue":20,
        }
        
        self.pin_button = {                                                                                                                                                                                                                                                                                                                                                                                                                                                             
            "Master":21,
        }
        
        # LEDs keyed by colour
        self.led_c = {}
        # LEDs keyed by pin number
       # self.led_p = {}
        for colour in self.pin_colour.keys():
            self.led_c[colour] = LED(self.pin_colour[colour])
        #    self.led_p[self.pin_colour[colour]] = LED(self.pin_colour[colour])
        # Buttons keyed by name     
        self.button = {}
        for name in self.pin_button.keys():
            self.button[name]=Button(self.pin_button[name])
    
    def test_led_c(self,colour,duration):
        self.led_c[colour].on()
        sleep(duration)
        self.led_c[colour].off()

    def test_all_leds_c(self,duration):
        for colour in self.pin_colour.keys():
            test_led_c(self,colour,duration)

    #def test_led_p(self,pin,duration):
    #    self.led_p[pin].on()
    #    sleep(duration)
    #    self.led_p[pin].off()

    #def test_all_leds_p(self,duration):
    #    for colour in self.pin_colour.values():
    #        test_led_p(self,colour,duration)

    def test_button(self,name):
        print(name,self.button[name].value)

    def test_all_buttons_n(self):
        for name in pin_button.keys():
            self.test_button(name)

# Self tests
if __name__ == '__main__':
    print("LED test program")
    marksboard = LEDBoard()
    print("Testing the Green LED")
    marksboard.test_led_c("Green",1)
    sleep(3)
    print("Testing all LEDs by colour")
    marksboard.test_all_leds_c(0.75)
    sleep(3)
    #print("Testing the LED on pin 18")
   # marksboard.test_led_p(18,1)
    #sleep(3)
    #print("Testing all LEDs by pin number")
   # marksboard.test_all_leds_p(0.75)
   # sleep(3)
    print("Testing the button")
    marksboard.test_button("Master")
    print("All done!")