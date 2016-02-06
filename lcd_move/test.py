import signal as sig
import RPi.GPIO as gpio
from time import  sleep
from lcd import LCD
from screen import Screen

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(5, GPIO.IN)
gpio.setup(6, GPIO.IN)
gpio.setup(19, GPIO.IN)

run = True

def on_exit(a,b):
    global run
    run = False
    
sig.signal(sig.SIGINT,on_exit)
print("Ctrl+C to exit")

# see comments in lcd.py
lcd = LCD(22,21,17,23,25,24)

# change these line to test
# 1st line = 0
# 2nd line = 1
#lcd.set_cursor(0,2) # line,column
#lcd.send_string('Xander Newlun')

screen = Screen(['Dog', 'Cat', 'Moose', 'Potatoes'], lcd)
screen.display();

while True:
	if !gpio.input(5):
		screen.moveDown()
		screen.display()
	elif !gpio.input(6):
		screen.moveUp()
		screen.display()

while run:
    sleep(1)
    
lcd.close()
print('Done')