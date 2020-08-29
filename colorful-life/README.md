"Colorful Life" for the AdaFruit RGB Matrix

To run:

`sudo python clrLife.py`

The number of generations is hard-coded as 1000 (see `numFrames`). You can interrupt (Ctrl-C) at any time.

Things to try:

- Hard_boundary true or false. How many generations work well for the two different values?
- Infinite cycle: when the number of frames is reached, reset and start again.
- Other rules. Adam Zheleznyak's code includes the possibility of using alternative "rules" for the game.
  The current rule is hard-coded (see `rule`). Investigate changing the rule from his [examples file](https://github.com/adam-zheleznyak/colorful-life/blob/master/examples.py).

TODO
Picture!
Video!
