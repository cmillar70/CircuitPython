import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    print("Make it Blue!")
    dot.fill((0, 0, 255))
    time.sleep(0.5)
    print("Make it Yellow")
    dot.fill((255, 255, 0))
    time.sleep(0.5)
