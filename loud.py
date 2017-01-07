import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)		#Set GPIO pin numbering
PIN = 25			#Associate pin 25 to PIN
GPIO.setup(PIN, GPIO.OUT)	#Set pin as out

class Loud ():
	def __init__(self, ns):
		self.ns = ns
		self.t=0.3                                #Set loud duration
                self.f=700
                self.beeps = {0 : self.beep0,
                              1 : self.beep1,
                              2 : self.beep2,
                              3 : self.beep3}


        def beep(self, t, f):
                for _ in range(0,int(t*f)):
                        GPIO.output(PIN, True)	        #Set PIN HIGH
                        time.sleep(1.0/f/2)		#Delay of t=1/f s
                        GPIO.output(PIN, False)	        #Set PIN LOW
                        time.sleep(1.0/f/2)		#Delay of t=1/f

        def beep0(self):
                while self.ns.distance == 0:
                      self.beep(self.t, self.f)  

        def beep1(self):
                while self.ns.distance == 1:
                        self.beep(self.t, self.f)
                        if self.ns.distance == 1:
                                time.sleep(self.t)
                        else:
                                return True

        def beep2(self):
                while self.ns.distance == 2:
                        self.beep(self.t, self.f)
                        for i in range(2):
                                if self.ns.distance == 2:
                                        time.sleep(self.t)
                                else:
                                        return True

        def beep3(self):
                while self.ns.distance == 3:
                      time.sleep(self.t)
        
	def run(self):
                while True:
                        self.beeps[self.ns.distance]()
