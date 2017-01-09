import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)		#Set GPIO pin numbering
PIN = 25			#Associate pin 25 to PIN
GPIO.setup(PIN, GPIO.OUT)	#Set pin as out

class Loud ():
	def __init__(self, ns):
		self.ns = ns                    # Common namespace between processes
		self.t=0.3                               
                self.f=600
                self.beeps = {0 : self.beep0,
                              1 : self.beep1,
                              2 : self.beep2,
                              3 : self.beep3}


        def beep(self, t, f):
                ''' Beep of t seconds by frequency of f '''
                delay=1.0/f/2                           # Half periodic time t/2=1/f/2
                for _ in range(0,int(t*f)):
                        GPIO.output(PIN, True)	        #Set PIN HIGH
                        time.sleep(delay)		#Delay of half periodic time
                        GPIO.output(PIN, False)	        #Set PIN LOW
                        time.sleep(delay)		#Delay of half periodic time

        def beep0(self):
                ''' Continuous sound '''
                delay=1.0/self.f/2
                while self.ns.distance == 0:
                        for _ in range(0, 200):
                                GPIO.output(PIN, True)	        #Set PIN HIGH
                                time.sleep(delay)
                                GPIO.output(PIN, False)	        #Set PIN LOW
                                time.sleep(delay)
                        GPIO.output(PIN, True)
                        time.sleep(delay)
                        GPIO.output(PIN, False)
                        time.sleep(delay-0.00003)               # Delay of t/2-time_to_start_new_loop 

        def beep1(self):
                ''' Frequent sound '''
                while self.ns.distance == 1:
                        self.beep(self.t*0.6, self.f)
                        if self.ns.distance == 1:
                                time.sleep(self.t*0.6)
                        else:
                                return True

        def beep2(self):
                ''' Sparse sound '''
                while self.ns.distance == 2:
                        self.beep(self.t, self.f)
                        for i in range(2):
                                if self.ns.distance == 2:
                                        time.sleep(self.t*0.8)
                                else:
                                        return True

        def beep3(self):
                ''' Silent '''
                while self.ns.distance == 3:
                      time.sleep(0.2)
        
	def run(self):
                while True:
                        self.beeps[self.ns.distance]()          # Sound by distance
