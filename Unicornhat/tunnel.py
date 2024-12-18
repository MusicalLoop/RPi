import colorsys
import math
import time

import unicornhathd as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
unicorn.brightness(0.5)
u_width,u_height=unicorn.get_shape()

# zoom tunnel
#def tunnel(x, y, step):
def tunnel():
    
    step = 0
    x = 0
    y = 0
    
    while True:
        for i in range(600):
            for h in range(u_height):
                for w in range(u_width):
                    speed = step / 100.0
                    x -= (u_width/2)
                    y -= (u_height/2)
                    
                    xo = math.sin(step / 27.0) * 2
                    yo = math.cos(step / 18.0) * 2
                    
                    x += xo
                    y += yo
                    
                    if y == 0:
                        if x < 0:
                            angle = -(math.pi / 2)
                        else:
                            angle = (math.pi / 2)
                    else:
                        angle = math.atan(x / y)
                    
                    if y > 0:
                        angle += math.pi
                    
                    angle /= 2 * math.pi # convert angle to 0...1 range
                    
                    shade = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) / 2.1
                    shade = 1 if shade > 1 else shade
                    
                    
                    angle += speed
                    depth = speed + (math.sqrt(math.pow(x, 2) + math.pow(y, 2)) / 10)
                    
                    col1 = colorsys.hsv_to_rgb((step % 255) / 255.0, 1, .8)
                    col2 = colorsys.hsv_to_rgb((step % 255) / 255.0, 1, .3)
                    
                    
                    col = col1 if int(abs(angle * 6.0)) % 2 == 0 else col2
                    
                    td = .3 if int(abs(depth * 3.0)) % 2 == 0 else 0
                    
                    col = (col[0] + td, col[1] + td, col[2] + td)
                    
                    col = (col[0] * shade, col[1] * shade, col[2] * shade)
                    
                    #return (col[0] * 255, col[1] * 255, col[2] * 255)
                    r = col[0] * 255
                    g = col[1] * 255
                    b = col[2] * 255
                    
                    r = int(max(0, min(255, r)))
                    g = int(max(0, min(255, g)))
                    b = int(max(0, min(255, b)))
                    unicorn.set_pixel(w, h, r, g, b)
            
            unicorn.show()
            step += 1
            time.sleep(0.1)
    
tunnel()
