import signal as sig
import RPi.GPIO as gpio
from time import  sleep
from lcd import LCD
from screen import Screen

#gpio.setup(5, GPIO.IN)
#gpio.setup(6, GPIO.IN)
#gpio.setup(19, GPIO.IN)

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

screen = Screen(['poopy', 'is xander'], lcd)
screen.removeString(0)
screen.display();
sleep(1);
screen.addString("gay?")
screen.display();

while run:
    sleep(1)
    
lcd.close()
print('Done')