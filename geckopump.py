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

pump(10)
GPIO.cleanup()
