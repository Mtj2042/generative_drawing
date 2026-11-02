# THINGS TO TRY ...

# 1. make a second circle which moves at a different speed
# 2. make a third circle which moves by a different amount
# 3. make a fourth circle which starts at a different point in the cycle

from py5canvas import *

def setup():
    create_canvas(800, 800)

def draw():
    #background(0,50)
    translate(center)
    fill(255)
    no_stroke()
    
    # y = sin(frame_count*0.01) * rand(150,200)
    # x = cos(frame_count*0.01) * rand(150,200)

    

    # xs = cos(frame_count*0.1) * 500
    # ys = sin(frame_count*0.1) * 500
    # xss = remap(seconds(),0,10,xs,0)
    # yss = remap(seconds(),0,10,ys,0)
    
    
    #circle(x, y, 10)

    #rect(y, x,10,10)
    fill(x,y,y)
    circle(xss, yss, 20)
    #background(0,50)
    
run()
