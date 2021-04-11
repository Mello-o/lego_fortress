from gpiozero import LED, Buzzer, LightSensor
from time import sleep

led_positions = [17, 27, 22]
leds = [LED(l) for l in led_positions]
buzzer = Buzzer(23)
ldr = LightSensor(21)

while True:
    
    if ldr.value > 0.1:
       for l in leds:
           l.on()
           buzzer.beep(on_time = 0.1)
           sleep(0.1)
           l.off()
           sleep(0.1)
           buzzer.off()