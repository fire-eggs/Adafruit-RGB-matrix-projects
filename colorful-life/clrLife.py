# John Conway's 'game of life' for the Adafruit RGB LED Matrix ...
# in color!
#
import Image
import ImageDraw
import time
import colorsys

from colorful_life import *
from rgbmatrix import Adafruit_RGBmatrix

def drawFrame(grid, h, w):
    draw.rectangle((0,0,32,32), fill=(0,0,0))
    
    for y in range(h):
        for x in range(w):
            if grid[x][y] == None:
                continue
            rgb = colorsys.hls_to_rgb(grid[x][y].value, 0.5, 0.5)
            rgb2 = tuple(int(round(i*255)) for i in rgb)
            draw.point((x,y), fill=rgb2)
            
    matrix.SetImage(image.im.id, 0, 0)
    time.sleep(0.25)

numFrames = 1000
rand_grid = random_colors(random_grid(32,32))

matrix = Adafruit_RGBmatrix(32, 1)
image = Image.new("RGB", (32, 32))
draw  = ImageDraw.Draw(image)

color_variation = 0.05
hard_boundary = False
rule=[[3],[2,3]]
interval=300 # ???
cell_size=0.2 # ???
for i in range(numFrames):
    drawFrame(rand_grid, 32, 32)
    rand_grid = colorful_life_step(rand_grid, color_variation, hard_boundary, rule)

matrix.Clear()

