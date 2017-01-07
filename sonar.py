from loud import Loud
from distance import Distance
from multiprocessing import Process
import time
from sensor import Sensor
from math import sqrt

sensorPorts = [{'TRIG' : 23, 'ECHO' : 24},
               {'TRIG' : 22, 'ECHO' : 16},
               {'TRIG' : 17, 'ECHO' : 27}] 

sensors = []

for s in sensorPorts:
    print(s['TRIG'], s['ECHO'])
    sensors.append(Sensor(s['TRIG'], s['ECHO']))

def toInt(distance):
    i=int(sqrt(distance/6))
    if i > 2:
        return 3
    else:
        return i
        

distance=[]
for test in sensors:
    dist0 = toInt(test.measure())
    distance.append(dist0)
    print(dist0)
    print(type(dist0))
    time.sleep(0.1)
    
dist=Distance(min(distance))

def runLoud():
    beep=Loud(dist)
    beep.start()

def runSonar(): 
    while True:
        for i in range(3):
            distance[i] = toInt(sensors[i].measure())
            dist.setDistance(min(distance))
            time.sleep(0.1)

runLoud()

runSonar()
