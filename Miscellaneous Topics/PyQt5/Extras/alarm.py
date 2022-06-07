import time
import winsound as w
import os

def alarm():
    while True:
        print("WARNING!!")
        time.sleep(0.5)
        w.Beep(5000, 200)
        w.Beep(3000, 200)
        w.Beep(5000, 200)
        w.Beep(3000, 200)

x = 5
for i in range(5):
    if x == 9:
        alarm()

    print("Info is updating")
    time.sleep(2)
    x+=2
