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
        
        # LEDs are keyed by colour
        self.led = {}
        for colour,pin in self.pin_colour.items():
            self.led[colour] = LED(pin)
        
        # Buttons are keyed by name
        self.button = {}
        for name,pin in self.pin_button.items():
            self.button[name]=Button(pin)
    
    def test_led(self,colour,duration):
        self.led[colour].on()
        sleep(duration)
        self.led[colour].off()

    def test_all_leds(self,duration,rest_interval):
        for colour in self.pin_colour.keys():
            print ("Colour: ",colour,"\nDuration: ", duration,"\nRest Interval:",rest_interval)
            self.test_led(colour,duration)
            sleep(rest_interval)

    def test_button(self,name):
        print(name,self.button[name].value)

    def test_all_buttons(self):
        for name in self.pin_button.keys():
            self.test_button(name)

# Self tests
if __name__ == '__main__':
    print("LED and button test program")
    marksboard = LEDBoard()
    print("Testing the Green LED")
    marksboard.test_led("Green",3)
    sleep(3)
    print("Testing the Yellow LED")
    marksboard.test_led("Yellow",3)
    sleep(3)
    print("Testing the Red LED")
    marksboard.test_led("Red",3)
    sleep(3)
    print("Testing all LEDs by colour")
    marksboard.test_all_leds(2,1)
    sleep(3)
    print("Testing the button after one second")
    sleep(1)
    marksboard.test_button("Master")
    print("All done!")
