import colorsys
import math
import time

import unicornhathd as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
unicorn.brightness(0.5)
u_width,u_height=unicorn.get_shape()


# weeee waaaah
def blues_and_twos():

    
    step = 0
    while True:
        for y in range(u_height):
            for x in range(u_width): 

                i = x - (u_width/2)
                j = y - (u_height/2)

                xs = (math.sin((i + step) / 10.0) / 2.0) + 1.0
                ys = (math.cos((j + step) / 10.0) / 2.0) + 1.0

                scale = math.sin(step / 6.0) / 1.5
                r = math.sin((i * scale) / 1.0) + math.cos((j * scale) / 1.0)
                b = math.sin(i * scale / 2.0) + math.cos(j * scale / 2.0)
                g = r - .8
                g = 0 if g < 0 else g

                b -= r
                b /= 1.4
                
                r *= 255
                g = (b + g) * 255
                b = g * 255
                r = int(max(0, min(255, r)))
                g = int(max(0, min(255, g)))
                b = int(max(0, min(255, b)))
                unicorn.set_pixel(x, y, r, g, b)
        
        unicorn.show()
        time.sleep(0.03)
        step += 1

blues_and_twos()
