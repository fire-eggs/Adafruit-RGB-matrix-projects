# Adafruit RGB Matrix Projects

Projects for the Adafruit RGB Matrix HAT in Python.

## Adafruit Product

The Adafruit RGB Matrix HAT is a board for the Raspberry Pi to drive HUB75 type RGB LED Matrix boards. The product can be found at https://www.adafruit.com/product/2345

There are a lot of details about the product in a [PDF](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi.pdf?timestamp=1598718014).

## Requirements

A 32 x 32 LED matrix. These projects assume a single 32x32 matrix; some projects could be modified to take advantage of chained matrices.

Python.

These projects require two libraries:
1. Hzeller's LED-matrix library, `rgb-matrix`. Instructions to download and install can be found in the above PDF. You can also access the library from [here](https://github.com/hzeller/rpi-rgb-led-matrix).
2. Pillow, for the Image and ImageDraw libraries :  `pip install Pillow`

## Projects

### Analog Clock

This is a simple little project which displays the current system time as an analog clock.  For more details, see the README in the project folder.

### Colorful Game of Life

The demo projects included with the rgb-matrix library include a version of John Conway’s game of Life. The demo doesn’t really highlight the capabilities of the matrices, as it uses a single color.

I adapted Adam Zheleznyak’s [“colorful-life”]((https://github.com/adam-zheleznyak/colorful-life)) to work on the matrix. Living cells will have a color assigned and children cells’ colors are derived from their parents. 

For more details, see the README in the project folder.
