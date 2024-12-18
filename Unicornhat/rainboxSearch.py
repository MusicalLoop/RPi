import math
import time

import unicornhathd as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
unicorn.brightness(0.5)
u_width,u_height=unicorn.get_shape()

# rainbow search spotlights
def rainbow_search():
    
    step = 0
    while True:
        for y in range(u_height):
            for x in range(u_width):
                
                xs = math.sin((step) / 100.0) * 20.0
                ys = math.cos((step) / 100.0) * 20.0

                scale = ((math.sin(step / 60.0) + 1.0) / 5.0) + 0.2
                r = math.sin((x + xs) * scale) + math.cos((y + xs) * scale)
                g = math.sin((x + xs) * scale) + math.cos((y + ys) * scale)
                b = math.sin((x + ys) * scale) + math.cos((y + ys) * scale)
                
                r *= 255
                g *= 255
                b *= 255
                
                r = int(max(0, min(255, r)))
                g = int(max(0, min(255, g)))
                b = int(max(0, min(255, b)))
                unicorn.set_pixel(x, y, r, g, b)
                #print(r, g, b)
        
        unicorn.show()
        time.sleep(0.01)
        step += 1

rainbow_search()
