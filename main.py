import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#IN1,2,3,4
IN=[35,36,37,38]
#HIGH to move
F=[IN[1],IN[2]]
B=[IN[0],IN[3]]
L=[IN[1],IN[3]]
R=[IN[0],IN[2]]

def STOP():
    GPIO.output(IN,GPIO.LOW)

def FWD():
    STOP()
    GPIO.output(F,GPIO.HIGH)

def BCK():
    STOP()
    GPIO.output(B,GPIO.HIGH)

def LFT():
    STOP()
    GPIO.output(L,GPIO.HIGH)

def RGT():
    STOP()
    GPIO.output(R,GPIO.HIGH)

GPIO.setup(IN,GPIO.OUT,initial=GPIO.LOW)

try:
    move=[FWD,BCK,LFT,RGT]
    for f in move:
        f()
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
