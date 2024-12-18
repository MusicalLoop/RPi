import colorsys
import math
import time

import unicornhathd as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
unicorn.brightness(0.5)
u_width,u_height=unicorn.get_shape()

def gradient():

    step = 0
    while True:
        for y in range(u_height):
            for x in range(u_width): 
    
                g = x * 16
                b = y * 16
                r = 255 - (x * 16)
                r = int(max(0, min(255, r)))
                g = int(max(0, min(255, g)))
                b = int(max(0, min(255, b)))
                unicorn.set_pixel(x, y, r, g, b)
        
        unicorn.show()
        time.sleep(0.03)
        step += 1

gradient()
