import RPi.GPIO as GPIO, time
from sonarA import *

try:
   setupSonar(sonarPin=8)
   while True:
       dist = getDistance()
       print dist
       time.sleep(1)

except KeyboardInterrupt:
       GPIO.cleanup()
