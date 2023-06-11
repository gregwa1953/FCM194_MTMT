# https://microcontrollerslab.com/hc-sr04-ultrasonic-sensor-raspberry-pi-pico-micropython-tutorial/

from hcsr04 import HCSR04
from time import sleep

sensor = HCSR04(trigger_pin=2, echo_pin=3, echo_timeout_us=10000)
button = machine.Pin(20,machine.Pin.IN,machine.Pin.PULL_UP)   # set pin 20 as INPUT with PULL_UP
while True:
    distance = sensor.distance_cm()
    #print('Distance:', distance, 'cm')
    cm2in=distance/2.54
    print(f"Distance {distance} cm - {cm2in} in")
    if button.value() == 0:
        print("Button Pressed")
        break        
    sleep(1)
