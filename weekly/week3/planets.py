from py5canvas import *

def setup():
    create_canvas(400, 400)

def draw():
    random_seed(101)
    background(0)
    # Origin at center
    translate(width/2, height/2)
    # Sun
    fill(255, 128, 0)
    circle(0, 0, 40)

    for i in range(5):
        dist = 70 + i*30
        no_fill()
        stroke(255, 50)
        circle(0, 0, dist*2)

        no_stroke()
        push_matrix() # Save current transformation
        rotate(radians(random(0, 360)) + frame_count*random(0.001, 0.05))
        translate(dist, 0)
        fill(0, 150, 200)
        circle(0, 0, random(5, 10))
        pop_matrix() # Restore last saved transformation

run()