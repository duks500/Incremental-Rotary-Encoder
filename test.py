import serial
import time


timeInterval = open('time_interval.txt','w')
distanceBetween = open('distance_between.txt','w')
arduinorSerialData = serial.Serial('/dev/ttyACM0', 9600)

first_time = 0
second_time = 0
firstOrNot = False

def writeToDile():
    global firstOrNot
    for x in range(2):
        if(firstOrNot == False):
            first_time = time.perf_counter()
            firstOrNot = True
        else:
            while(1==1):
                if(arduinorSerialData.inWaiting()>0):
                    myData = arduinorSerialData.readline()
                    # newTxtFile.write(myData)
                    second_time = time.perf_counter()
                    diffrentBetweenValue = round(float(diffrentBetweenTime(first_time,second_time)), 4)

                    timeInterval.write(str(diffrentBetweenValue))
                    timeInterval.write('\n')

                    distanceBetween.write(str(myData.decode("utf-8")))
                    distanceBetween.write('\n')                  

                    print (myData)
                    
                    first_time = second_time


def addTime():
    tlc = time.perf_counter()
    return tlc

def diffrentBetweenTime(first_time,second_time):
    diffTime = second_time - first_time
    return diffTime

writeToDile()