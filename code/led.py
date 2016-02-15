import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

while 1:
  GPIO.output(18, True)
  time.sleep(1)
  GPIO.output(18, False)
  time.sleep(1)
