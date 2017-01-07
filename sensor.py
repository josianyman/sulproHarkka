import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library

class Sensor:

  def __init__(self, TRIG, ECHO):
    GPIO.setmode(GPIO.BCM)                    #Set GPIO pin numbering 

    self.TRIG = TRIG                          #Associate pin to TRIG
    self.ECHO = ECHO                          #Associate pin to ECHO

    GPIO.setup(self.TRIG,GPIO.OUT)            #Set pin as GPIO out
    GPIO.setup(self.ECHO,GPIO.IN)             #Set pin as GPIO in

  def trigg(self):
    GPIO.output(self.TRIG, False)             #Set TRIG as LOW
    time.sleep(0.01)                           #Delay of 0.01 sec
    GPIO.output(self.TRIG, True)              #Set TRIG as HIGH
    time.sleep(0.00001)                       #Delay of 0.00001 seconds
    GPIO.output(self.TRIG, False)             #Set TRIG as LOW
    return True

  def measure(self):
    self.trigg()
    pulse_start = time.time()
    while GPIO.input(self.ECHO)==0:               #Check whether the ECHO is LOW
      pulse_start = time.time()              #Saves the last known time of LOW pulse

    pulse_end = time.time() 
    while GPIO.input(self.ECHO)==1:               #Check whether the ECHO is HIGH
      pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
 
    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2) - 0.5            #Round to two decimal points
    return distance
