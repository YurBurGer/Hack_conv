import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#IN1,2,3,4
IN=[35,36,37,38]
#init pins
GPIO.setup(IN,GPIO.OUT,initial=GPIO.LOW)
#HIGH to move
B=[IN[1],IN[2]]
F=[IN[0],IN[3]]
R=[IN[1],IN[3]]
L=[IN[0],IN[2]]
#enable PWM
PWM_en=False
#make pwm instance
PWM=[31,32]
GPIO.setup(PWM,GPIO.OUT)
freq=25000

p1=GPIO.PWM(PWM[0],freq)
p2=GPIO.PWM(PWM[1],freq)
def STOP():
    GPIO.output(IN,GPIO.LOW)
    p1.stop()
    p2.stop()
    
def FWD(speed=None):
    STOP()
    if speed is not None:
        p1.start(speed)
        p2.start(speed)
    GPIO.output(F,GPIO.HIGH)
    
def BCK(speed=None):
    STOP()
    if speed is not None:
        p1.start(speed)
        p2.start(speed)
    GPIO.output(B,GPIO.HIGH)

def LFT(speed=None):
    STOP()
    if speed is not None:
        p1.start(speed)
        p2.start(speed)
    GPIO.output(L,GPIO.HIGH)

def RGT(speed=None):
    STOP()
    if speed is not None:
        p1.start(speed)
        p2.start(speed)
    GPIO.output(R,GPIO.HIGH)
    
try:
    move=[FWD,BCK]
    for f in move:
        f(95)
        time.sleep(1)
        STOP()
        time.sleep(1)
    move=[LFT,RGT]
    for f in move:
        f(50)
        time.sleep(1)
        STOP()
        time.sleep(1)
except KeyboardInterrupt:
    pass

p1.stop()
p2.stop()
GPIO.cleanup()
