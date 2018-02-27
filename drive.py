import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#IN1,2,3,4
IN=[35,36,37,38]
#init pins
GPIO.setup(IN,GPIO.OUT,initial=GPIO.LOW)
#HIGH to move
L=[IN[1],IN[2]]
R=[IN[0],IN[3]]
F=[IN[1],IN[3]]
B=[IN[0],IN[2]]
#enable PWM
PWM_en=False
#make pwm instance
PWM=[31,32]
GPIO.setup(PWM,GPIO.OUT)
freq=25000

p1=GPIO.PWM(PWM[0],freq)
p2=GPIO.PWM(PWM[1],freq)
p1.start(0)
p2.start(0)
def STOP():
    GPIO.output(IN,GPIO.LOW)
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)
    
def FWD(speed=None):
    STOP()
    if speed is not None:
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)
    GPIO.output(F,GPIO.HIGH)
    
def BCK(speed=None):
    STOP()
    if speed is not None:
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)
    GPIO.output(B,GPIO.HIGH)

def LFT(speed=None):
    STOP()
    if speed is not None:
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)
    GPIO.output(L,GPIO.HIGH)

def RGT(speed=None):
    STOP()
    if speed is not None:
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)
    GPIO.output(R,GPIO.HIGH)
    
#try:
#    move=[FWD,BCK]
#    for f in move:
#        f(95)
#        time.sleep(1)
#        STOP()
#        time.sleep(1)
#    move=[LFT,RGT]
#    for f in move:
#        f(50)
#        time.sleep(1)
#        STOP()
#        time.sleep(1)
#except KeyboardInterrupt:
#    pass

def close_pins():
    p1.stop()
    p2.stop()
    GPIO.cleanup()
