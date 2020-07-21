import sys
import time
import RPi.GPIO as GPIO

mode = GPIO.getmode() 

Pump = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(Pump, GPIO.OUT)

def pump(x): 
  GPIO.output(Pump, GPIO.HIGH)
  print("Pumping: " + str(x))
  time.sleep(x)
  GPIO.output(Pump, GPIO.LOW)

while 1:
  pump(8)
  time.sleep(86400)

GPIO.cleanup()
