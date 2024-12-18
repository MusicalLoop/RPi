import math
import time

import unicornhathd as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
unicorn.brightness(0.5)
u_width,u_height=unicorn.get_shape()

# twisty swirly goodness
#def swirl(x, y, step):
def swirl():
   
    step = 0
    #f = 0
    #g = 0
    while True:
        for y in range(u_height):
            for x in range(u_width):
                f = x - (u_width/2)
                g = y - (u_height/2)
                
                dist = math.sqrt(pow(f, 2)+pow(g, 2)) / 2.0
                angle = (step / 10.0) + (dist * 1.5)
                s = math.sin(angle);
                c = math.cos(angle);
                
                xs = f * c - g * s;
                ys = f * s + g * c;
                
                r = abs(xs + ys)
                r = r * 64.0
                r -= 20
                
                #r =
                g =r + (s * 130)
                b = r + (c * 130)
                
                r = int(max(0, min(255, r)))
                g = int(max(0, min(255, g)))
                b = int(max(0, min(255, b)))
                unicorn.set_pixel(x, y, r, g, b)
        
        unicorn.show()
        time.sleep(0.03)
        step += 1

swirl()
