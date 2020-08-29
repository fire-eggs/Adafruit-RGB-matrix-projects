# Analog Clock for the Adafruit RGB Matrix
#
#requires Pillow (Image, ImageDraw)
# pip install Pillow
# Requires the AdaFruit rgbmatrix library
#
# A 32x32 matrix doesn't allow for complete
# symmetry. The center point is at (15,15), so
# there are 15 "pixels" on the left/top, 
# and 16 on the right/bottom.
# So these values aren't perfect.

import Image
import ImageDraw
import time
import datetime
import math

from rgbmatrix import Adafruit_RGBmatrix

def draw_ticks():
    # draw hour ticks
    draw.point((15,0), fill=(255,0,0)) # 12
    draw.point((15,1), fill=(255,0,0)) # 12
    draw.point((31,15),fill=(255,0,0)) #  3
    draw.point((15,31),fill=(255,0,0)) #  6
    draw.point((0,15), fill=(255,0,0)) #  9

    draw.point((24,2), fill=(255,0,0)) #  1
    draw.point((30,8), fill=(255,0,0)) #  2

    draw.point((30,24), fill=(255,0,0)) # 4
    draw.point((24,30), fill=(255,0,0)) # 5

    draw.point(( 8,30), fill=(255,0,0)) # 7
    draw.point(( 2,24), fill=(255,0,0)) # 8

    draw.point(( 2,8), fill=(255,0,0)) # 10
    draw.point(( 8,2), fill=(255,0,0)) # 11
    
def draw_hour(which, color):
    # Draw the clock's hour hand.
    #
    if (which == 1):
        draw.line((15,15,20, 7), fill=color) # 1
    elif (which == 2):
        draw.line((15,15,23,11), fill=color) # 2
    elif (which == 3):
        draw.line((23,15,15,15), fill=color) # 3
    elif (which == 4):
        draw.line((15,15,23,20), fill=color) # 4
    elif (which == 5):
        draw.line((15,15,19,22), fill=color) # 5
    elif (which == 6):
        draw.line((15,22,15,15), fill=color) # 6
    elif (which == 7):
        draw.line((15,15,11,22), fill=color) # 7
    elif (which == 8):
        draw.line((15,15, 9,19), fill=color) # 8
    elif (which == 9):
        draw.line(( 8,15,15,15), fill=color) # 9
    elif (which == 10):
        draw.line((15,15, 9,11), fill=color) # 10
    elif (which == 11):
        draw.line((15,15,11, 7), fill=color) # 11
    elif (which == 12):
        draw.line((15, 7,15,15), fill=color) # 12

def draw_clock(hr, minute):
    # Draw the clock to the bitmap.
    # The colors for the clock hands are specified here.
    #
    draw.rectangle((0,0,32,32), fill=(0,0,0))

    draw_ticks()
    draw_minute(minute, (64,0,128))
    draw_hour(hr, (0,128,0)) # draw hour last to overlay minute

def draw_minute(minute, color):
    # Using trigonometry, draw a line representing the minute hand
    #
    # issue: minute==45 does not line up with 9 mark
    # minute hand for 10,20,30,35,45 not ideal
    #
    min_x = math.sin(math.radians(minute * 6)) * 15
    min_y = math.cos(math.radians(minute * 6)) * 15
    draw.line((15,15,min_x + 16, 16-min_y),color)

#*****************
# Program start
#*****************

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 1)

# Establish a bitmap to draw to. The bitmap is then set
# to the matrix to be shown. [Essentially "off-screen" drawing]
image = Image.new("RGB", (32, 32))
draw  = ImageDraw.Draw(image)

# Get the system time.
now = datetime.datetime.now()
hr = now.time().hour
if hr > 12:
    hr -= 12
minute = now.time().minute

draw_clock(hr, minute)
matrix.Clear()
matrix.SetImage(image.im.id, 0, 0)

time.sleep(5)
matrix.Clear()

