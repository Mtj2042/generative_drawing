from py5canvas import *

num_frames = 200
num_shapes = 10


def setup():
    create_canvas(400, 400)
    num_movie_frames(num_frames)
    frame_rate(60)
    rect_mode(CENTER)


def draw_object(x, y, size, theta):
    push_matrix()
    translate(x, y)
    rotate(theta)
    square(0, 0, size)
    pop_matrix()


def draw():
    global img
    random_seed(232)
    background(0)
    stroke(255)
    fill(255, 70)

    size = 50
    spacing = 60
    n = 10

    # try making the squares tumble while always touching the line below?
    #  line(0, height / 2 + size / 2, width, height / 2 + size / 2)

    # Leave space for two shapes behind the scenes
    # one on the left and one on the right
    wrap_dist = width + spacing * 2

    # Get a value between 0 and 1 for the whole animation
    t = frame_count / num_frames

    # Draw multiple shapes
    for i in range(n):
        # Position of the shape along range
        x = remap(i, 0, n, 0, wrap_dist)

        # pass rotation to object
        phase = i * PI / 9
        theta = t * TWO_PI + phase

        # Add add the offset and modulo to animate and wrap around
        # subtracts `w` to hide the first object on the left
        draw_object((t * wrap_dist + x) % wrap_dist - spacing, height / 2, size, theta)


run()
