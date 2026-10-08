from py5canvas import *

def setup():
    create_canvas(512, 512)

def draw():
    background(255)
    num_rows = 10
    num_cols = 10
    row_height = height / num_rows
    col_width = width / num_cols
    fill(0).stroke(255)
    for i in range(num_rows):
        for j in range(num_cols+1):
            y = i * row_height
            # *2 is a "bug" but looks cool, *1 will fill all squares
            x = (j*col_width  + frame_count*(1+i)) % (width + col_width*2) - col_width 
            rectangle(x, y, row_height, row_height)

run()