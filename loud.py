import threading
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)		#Set GPIO pin numbering
PIN = 25			#Associate pin 25 to PIN
GPIO.setup(PIN, GPIO.OUT)	#Set pin as out


class Loud (threading.Thread):
        '''
        def getF(self):
                print(self.distance.getDistance())
                return int(-23.23*self.distance.getDistance()+5050)
        '''
	def __init__(self, distance):
		threading.Thread.__init__(self)
		self.distance = distance
		self.t=0.3                                #Set loud duration
                self.f=700
                self.beeps = {0 : self.beep0,
                              1 : self.beep1,
                              2 : self.beep2,
                              3 : self.beep3}
                
        '''	
        def setMin(self, distance):
                self.distance = distance
                self.f = int(-23.23*distance+5050)
                print("distance set", distance)
        '''

        def beep(self, t, f):
                print("Piip")
                for _ in range(0,int(t*f)):
                        GPIO.output(PIN, True)	        #Set PIN HIGH
                        time.sleep(1.0/f/2)		#Delay of t=1/f s
                        GPIO.output(PIN, False)	        #Set PIN LOW
                        time.sleep(1.0/f/2)		#Delay of t=1/f

        def beep0(self):
                while self.distance.getDistance() == 0:
                      self.beep(self.t, self.f)  

        def beep1(self):
                while self.distance.getDistance() == 1:
                        self.beep(self.t, self.f)
                        if self.distance.getDistance() == 1:
                                time.sleep(self.t)
                        else:
                                return True

        def beep2(self):
                while self.distance.getDistance() == 2:
                        self.beep(self.t, self.f)
                        for i in range(2):
                                if self.distance.getDistance() == 2:
                                        time.sleep(self.t)
                                else:
                                        return True

        def beep3(self):
                while self.distance.getDistance() == 3:
                      time.sleep(self.t)
        
	def run(self):
                while True:
                        print("Matka muuttu")
                        if self.distance.getDistance()==1:
                                self.beep1()
                        self.beeps[self.distance.getDistance()]()
