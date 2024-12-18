import colorsys
import math
import time

import unicornhathd as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
unicorn.brightness(0.5)
u_width,u_height=unicorn.get_shape()

# roto-zooming checker board
def checker():
    
    step = 0
    f = 0
    g = 0
    while True:
        for y in range(u_height):
            for x in range(u_width):    
                f = x - (u_width/2)
                g = y - (u_height/2)

                angle = (step / 10.0)
                s = math.sin(angle);
                c = math.cos(angle);

                xs = f * c - g * s;
                ys = f * s + g * c;

                xs -= math.sin(step / 200.0) * 40.0
                ys -= math.cos(step / 200.0) * 40.0

                scale = step % 20
                scale /= 20
                scale = (math.sin(step / 50.0) / 8.0) + 0.25;

                xs *= scale
                ys *= scale

                xo = abs(xs) - int(abs(xs))
                yo = abs(ys) - int(abs(ys))
                l = 0 if (math.floor(xs) + math.floor(ys)) % 2 else 1 if xo > .1 and yo > .1 else .5

                r, g, b = colorsys.hsv_to_rgb((step % 255) / 255.0, 1, l)
                
                r *= 255
                g *= 255
                b *= 255
                r = int(max(0, min(255, r)))
                g = int(max(0, min(255, g)))
                b = int(max(0, min(255, b)))
                unicorn.set_pixel(x, y, r, g, b)
        
        unicorn.show()
        time.sleep(0.03)
        step += 1

checker()
    
