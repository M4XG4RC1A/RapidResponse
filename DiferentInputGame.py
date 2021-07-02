import serial
from tkinter import *
import random
import time

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 9600

colors = {0:"Red",1:"Blue"}
UTFColor = {"R":"Red","B":"Blue"}

points = 0

print("Welcome to rapid response\nyou have 1 second for identify the color\n")
repeats = int(input('Number of Repetions: '))


for i in range(repeats):
    print("Be Careful")
    time.sleep(1)
    Val = random.randint(0,1)
    sel = colors[Val]
    print("\n"+sel+"\n")
    start = time.time()
    end = time.time()
    line = ""
    while(end-start < 1 and line==""):
        line = UTFColor[ser.readline()[:-2].decode('utf-8')]
        end = time.time()
    print("Your time: {}".format(end-start))
    print("Your choose: {}".format(line))
    if line == sel and end-start<1:
        print("You are Okey")
        points = points+1
    else:
        if (end-start>1):
            print("OUT OF TIME")
        else:
            print("You are Wrong")
    print("Points: {}\n\n".format(points))

print("Game End")
print("You Score: {}/{}".format(points,repeats))
