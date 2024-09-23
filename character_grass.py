from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_rectangle():
    x, y = 0, 90
    while x < 750:  
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 5
        delay(0.01)
    
    while y < 550:  
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 5
        delay(0.01)
    
    while x > 50:  
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 5
        delay(0.01)
    
    while y > 90:  
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 5
        delay(0.01)


def move_circle():
    cx, cy = 400, 300  
    radius = 200  
    for degree in range(0, 360, 5):
        clear_canvas_now()
        grass.draw_now(400, 30)
        x = cx + radius * math.cos(math.radians(degree)) 
        y = cy + radius * math.sin(math.radians(degree))  
        character.draw_now(x, y)
        delay(0.01)


while True:
    move_rectangle()
    move_circle()    

close_canvas()
