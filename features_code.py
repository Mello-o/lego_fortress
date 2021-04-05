from gpiozero import LED
from time import sleep

led_positions = [17, 27, 22]
leds = [LED(l) for l in led_positions]

while True:
    
    for l in leds:
        l.on()
        sleep(0.1)
        l.off()
        sleep(0.1)