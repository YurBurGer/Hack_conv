import time
import drive as dr
fs=40
ts=40

for i in range(0,5):
    #dr.BCK(2*fs)
    #time.sleep(0.15)
    dr.BCK(fs)
    time.sleep(1)
    dr.STOP()
    time.sleep(0.2)
    dr.RGT(ts)
    time.sleep(0.25)
    dr.STOP()
    time.sleep(0.2)

for i in range(0,2):
    #dr.BCK(2*fs)
    #time.sleep(0.15)
    dr.BCK(fs)
    time.sleep(1)
    dr.STOP()
    time.sleep(0.2)
    dr.LFT(ts)
    time.sleep(0.42)
    dr.STOP()
    time.sleep(0.2)
    
dr.close_pins()
