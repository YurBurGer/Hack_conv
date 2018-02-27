import time
import drive
fs=97
ts=40
for i in range(0,2):
    FWD(fs)
    time.sleep(3)
    STOP()
    time.sleep(0.2)
    RGT(ts)
    time.sleep(0.4)
    STOP()
    time.sleep(0.2)
    FWD(fs)
    time.sleep(1)
    STOP()
    time.sleep(0.2)
    LFT(ts)
    time.sleep(0.5)
    STOP()
    time.sleep(0.2)
    FWD(fs)
    time.sleep(2)
    STOP()
    time.sleep(0.2)

