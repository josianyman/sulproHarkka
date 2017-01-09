from loud import Loud
from distance import Distance
from multiprocessing import Process, Manager
import time
from sensor import Sensor
from math import sqrt

sensorPorts = [{'TRIG' : 23, 'ECHO' : 24},
               {'TRIG' : 22, 'ECHO' : 16},
               {'TRIG' : 17, 'ECHO' : 27}] 

sensors = []

for s in sensorPorts:
    sensors.append(Sensor(s['TRIG'], s['ECHO']))

def toInt(distance):
    '''Convert distance in cm to int with scale 0...3'''
    if distance < 8:
        return 0
    elif distance < 22:
        return 1
    elif distance < 55:
        return 2
    else:
        return 3

distance=[]
for test in sensors:
    dist0 = toInt(test.measure())       # Measure all sensors
    distance.append(dist0)
    time.sleep(0.1)

def runLoud(ns):
    beep=Loud(ns)
    beep.run()
    
manager = Manager()
ns = manager.Namespace()
ns.distance = min(distance) 

p=Process(target=runLoud, args=[ns]) 
p.start()                               # Start loud in separate process

def runSonar(ns): 
    while True:
        for i in range(3):
            distance[i] = toInt(sensors[i].measure())   # Measure distance and save it to array
            ns.distance=min(distance)                   # Share minimium distance to loud process
            time.sleep(0.07)                            # Wait for ultrasonic reflections before new measure

runSonar(ns)
