# Analog Clock for the Adafruit RGB Matrix

To run:

`sudo python clock.py`

The current system time is displayed as an analog clock on the matrix. It is shown for five seconds.

The RGB Matrix takes a fair amount of power, and using `sleep` in the code may take a fair amount of CPU power. 
If you want to use the clock for a long time (e.g. as a "real clock") I suggest using a shell loop to show the
time, then sleep for a while. E.g. you might show the time, then sleep for 30 seconds, thus the time will be
shown for five seconds, then the matrix turns off for 30 seconds. The included `clockloop.sh` file is sort of
an example of this idea.

## A blurry picture, 4:42:

![blurry picture 4:42](pix_04_43.png)

## Things to try:

- The color for the hands and hour markers are hard-coded, try your own colors or random changes!
- Add an am / pm indicator
- "Night mode": use duller colors at "night".
