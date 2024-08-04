import board
from analogio import AnalogIn
import time
import neopixel

np = neopixel.NeoPixel(board.NEOPIXEL, 30, brightness=0.3, auto_write=False)

temperature = AnalogIn(board.A8)

def Rescale(value, input_min, input_max, output_min, output_max):
    input_range = input_max - input_min
    out_range = output_max - output_min
    normal = (value - input_min) / input_range
    output_val = normal * out_range + output_min
    return output_val


while True:
    Temp = Rescale(temperature.value, 0, 65535, 0, 3.3)
    C = (Temp * 100) - 50
    C_to_F = (C * 9) / 5 + 32
    print((int(C), int(C_to_F)))
    if C_to_F < 70:
        np[0] = 0x0000FF
        np.show()
    elif C_to_F > 70 and C_to_F < 74:
        np[0] = 0x0000FF
        np[1] = 0x00ff00
        np.show()
    elif C_to_F > 75 and C_to_F < 79:
        np[0] = 0x0000ff
        np[1] = 0x00ff00
        np[2] = 0xffff00
        np.show()
    elif C_to_F > 80 and C_to_F < 84:
        np[0] = 0x0000ff
        np[1] = 0x00ff00
        np[2] = 0xffff00
        np[3] = 0xFF4000
        np.show()
    if C_to_F > 84:
        np[0] = 0x0000ff
        np[1] = 0x00ff00
        np[2] = 0xffff00
        np[3] = 0xFF4000
        np[4] = 0xff0000
        np.show()
    time.sleep(1)
