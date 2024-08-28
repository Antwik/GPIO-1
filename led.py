from gpiozero import LED
from time import sleep

led = LED(17)
 
number=int(input("Please Enter a number : ")) 
while number > 0:
    print("led running..." + str(number))
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    number-=5