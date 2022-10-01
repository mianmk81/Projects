from adafruit_circuitplayground import cp
import time
import random


run_sequence = []
check_seqence = []
pixels = [6, 8, 1, 3]

'''
# Function: start
# Description: if you touch a pad it will light up a specific pixel associated with that pad and
#              it will also play tone associated with it.
# Parameters: number: None
# Return value: returns 1 if touched and returns -1 if not touched.
'''

def start():
    if cp.touch_A1:
        cp.pixels[6] = 0xFF0000
        cp.play_tone(1250, 0.1)
        time.sleep(0.3)
        cp.pixels[6] = 0x000000
        return 1
    elif cp.touch_A3:
        cp.pixels[8] = 0xFFFF00
        cp.play_tone(1500, 0.1)
        time.sleep(0.3)
        cp.pixels[8] = 0x000000
        return 1
    elif cp.touch_A4:
        cp.pixels[1] = 0x00FF00
        cp.play_tone(1000, 0.1)
        time.sleep(0.3)
        cp.pixels[1] = 0x000000
        return 1
    elif cp.touch_A6:
        cp.pixels[3] = 0x0000FF
        cp.play_tone(1750, 0.1)
        time.sleep(0.3)
        cp.pixels[3] = 0x000000
        return 1
    else:
        return -1
