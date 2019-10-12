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
        }
        
        self.pin_button = {                                                                                                                                                                                                                                                                                                                                                                                                                                                             
            "Master":21,
        }
        
        # LEDs keyed by colour
        self.led_c = {}
        for colour,pin in self.pin_colour.items():
            self.led_c[colour] = LED(pin)
        
        # Buttons keyed by name
        self.button = {}
        for name in self.pin_button.keys():
            self.button[name]=Button(self.pin_button[name])
    
    def test_led_c(self,colour,duration):
        self.led_c[colour].on()
        sleep(duration)
        self.led_c[colour].off()

    def test_all_leds_c(self,duration,rest_interval):
        for colour in self.pin_colour.keys():
            print ("Colour: ",colour,"\nDuration: ", duration,"\nRest Interval:",rest_interval)
            self.test_led_c(colour,duration)
            sleep(rest_interval)

    def test_button(self,name):
        print(name,self.button[name].value)

    def test_all_buttons_n(self):
        for name in self.pin_button.keys():
            self.test_button(name)

# Self tests
if __name__ == '__main__':
    print("LED test program")
    marksboard = LEDBoard()
    print("Testing the Green LED")
    marksboard.test_led_c("Green",3)
    sleep(3)
    print("Testing the Yellow LED")
    marksboard.test_led_c("Yellow",3)
    sleep(3)
    print("Testing the Red LED")
    marksboard.test_led_c("Red",3)
    sleep(3)
    print("Testing all LEDs by colour")
    marksboard.test_all_leds_c(2,1)
    sleep(3)
    print("Testing the button")
    marksboard.test_button("Master")
    print("All done!")