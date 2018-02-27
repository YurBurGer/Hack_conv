import time
import drive as dr
fs=97
ts=40
dr.setup_pins()
for i in range(0,2):
    dr.FWD(fs)
    time.sleep(3)
    dr.STOP()
    time.sleep(0.2)
    dr.RGT(ts)
    time.sleep(0.4)
    dr.STOP()
    time.sleep(0.2)
    dr.FWD(fs)
    time.sleep(1)
    dr.STOP()
    time.sleep(0.2)
    dr.LFT(ts)
    time.sleep(0.5)
    dr.STOP()
    time.sleep(0.2)
    dr.FWD(fs)
    time.sleep(2)
    dr.STOP()
    time.sleep(0.2)
dr.close_pins()
