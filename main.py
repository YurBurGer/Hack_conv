import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
IN=[35,36,37,38]
#HIGH to move
F=[IN[1],IN[2]]
B=[IN[0],IN[3]]
L=[IN[1],IN[2]]
R=[IN[0],IN[3]]
def STOP
def FWD():
    GPIO.output(IN,GPIO.LOW)
    GPIO.output(FWD,HIGH)
GPIO.setup(IN,GPIO.OUT,initial=GPIO.LOW)
GPIO.output(FWD,GPIO.HIGH)
time.sleep(3)
GPIO.cleanup()
