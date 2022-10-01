#Class:
import random

class Die:
    number_of_faces = 6

    def __init__(self, num_faces = 6):
        self.number_of_faces = num_faces

    def roll(self):
        return random.randint(1, self.number_of_faces)


#rolls a random dice when reseted





#Code:
import board
import time
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.circle import Circle
import die

# Use the built-in Display object
display = board.DISPLAY

# Make the display context
splash = displayio.Group()
display.show(splash)

# Make a background color fill
color_bitmap = displayio.Bitmap(160, 128, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF
bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
splash.append(bg_sprite)

# Add text to the screen
text = "Hello World!"
font = terminalio.FONT
color = 0x0000FF
text_area = label.Label(font, text=text, color=color)
text_area.x = 20
text_area.y = 40
splash.append(text_area)
text_area.hidden = True

# Add a circle to the screen
circle1 = Circle(26, 21, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle1)
circle1.hidden = True

circle2 = Circle(79, 21, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle2)
circle2.hidden = True

circle3 = Circle(132, 21, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle3)
circle3.hidden = True

circle4 = Circle(79, 63, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle4)
circle4.hidden = True

circle5 = Circle(26, 105, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle5)
circle5.hidden = True

circle6 = Circle(79, 105, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle6)
circle6.hidden = True

circle7 = Circle(132, 105, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle7)
circle7.hidden = True

def roll():
    die1 = die.Die(6)
    roll = die1.roll()
    if roll == 1:
        circle4.hidden = False
    if roll == 2:
        circle3.hidden = False
        circle5.hidden = False
    if roll == 3:
        circle3.hidden = False
        circle4.hidden = False
        circle5.hidden = False
    if roll == 4:
        circle1.hidden = False
        circle3.hidden = False
        circle5.hidden = False
        circle7.hidden = False
    if roll == 5:
        circle1.hidden = False
        circle3.hidden = False
        circle4.hidden = False
        circle5.hidden = False
        circle7.hidden = False
    if roll == 6:
        circle1.hidden = False
        circle2.hidden = False
        circle3.hidden = False
        circle5.hidden = False
        circle6.hidden = False
        circle7.hidden = False

roll()
# while loop needed to see the output
while True:
    pass

#rolls the ranam dice when pressed A

import board
import time
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.circle import Circle
import die
from digitalio import DigitalInOut
from gamepadshift import GamePadShift
pad = GamePadShift(DigitalInOut(board.BUTTON_CLOCK),DigitalInOut(board.BUTTON_OUT),DigitalInOut(board.BUTTON_LATCH))


# Use the built-in Display object
display = board.DISPLAY

# Make the display context
splash = displayio.Group()
display.show(splash)

# Make a background color fill
color_bitmap = displayio.Bitmap(160, 128, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF
bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
splash.append(bg_sprite)

# Add text to the screen
text = "Hello World!"
font = terminalio.FONT
color = 0x0000FF
text_area = label.Label(font, text=text, color=color)
text_area.x = 20
text_area.y = 40
splash.append(text_area)
text_area.hidden = True



# Add a circle to the screen
circle1 = Circle(26, 21, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle1)
circle1.hidden = True

circle2 = Circle(79, 21, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle2)
circle2.hidden = True

circle3 = Circle(132, 21, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle3)
circle3.hidden = True

circle4 = Circle(79, 63, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle4)
circle4.hidden = True

circle5 = Circle(26, 105, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle5)
circle5.hidden = True

circle6 = Circle(79, 105, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle6)
circle6.hidden = True

circle7 = Circle(132, 105, 17, fill=0xFF0000, outline=0x000000)
splash.append(circle7)
circle7.hidden = True



def roll():
    die1 = die.Die(6)
    roll = die1.roll()
    circle1.hidden = True
    circle2.hidden = True
    circle3.hidden = True
    circle4.hidden = True
    circle5.hidden = True
    circle6.hidden = True
    circle7.hidden = True
    if roll == 1:
        circle4.hidden = False
    if roll == 2:
        circle3.hidden = False
        circle5.hidden = False
    if roll == 3:
        circle3.hidden = False
        circle4.hidden = False
        circle5.hidden = False
    if roll == 4:
        circle1.hidden = False
        circle3.hidden = False
        circle5.hidden = False
        circle7.hidden = False
    if roll == 5:
        circle1.hidden = False
        circle3.hidden = False
        circle4.hidden = False
        circle5.hidden = False
        circle7.hidden = False
    if roll == 6:
        circle1.hidden = False
        circle2.hidden = False
        circle3.hidden = False
        circle5.hidden = False
        circle6.hidden = False
        circle7.hidden = False

# while loop needed to see the output
while True:
    pressed = pad.get_pressed()
    if pressed & 2 > 0:
        roll()
        print("A was pressed")
    time.sleep(0.2)



 
