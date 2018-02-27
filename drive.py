import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#IN1,2,3,4
IN=[35,36,37,38]
#init pins
GPIO.setup(IN,GPIO.OUT,initial=GPIO.LOW)
#HIGH to move
F=[IN[1],IN[2]]
B=[IN[0],IN[3]]
L=[IN[1],IN[3]]
R=[IN[0],IN[2]]
#enable PWM
PWM_en=False
#make pwm instance
PWM=[31,32]
GPIO.setup(PWM,GPIO.OUT)
freq=10000
p=GPIO.PWM(PWM[0],freq)


def STOP():
    GPIO.output(IN,GPIO.LOW)
    p.stop()


def FWD(speed=None):
    STOP()
    if speed is not None:
        p.start(speed)
    GPIO.output(F,GPIO.HIGH)


def BCK(speed=None):
    STOP()
    if speed is not None:
        p.start(speed)
    GPIO.output(B,GPIO.HIGH)


def LFT(speed=None):
    STOP()
    if speed is not None:
        p.start(speed)
    GPIO.output(L,GPIO.HIGH)

def RGT(speed=None):
    STOP()
    if speed is not None:
        p.start(speed)
    GPIO.output(R,GPIO.HIGH)

if __name__ == '__main__':
    try:
        move=[FWD,BCK,LFT,RGT]
        for f in move:
            f()
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

    p.stop
    GPIO.cleanup()
