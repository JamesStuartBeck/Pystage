# basic movement - move your character 10 "unit" in a cardinal direction

def right(sprite):
    sprite.change_x_by(10)

def left(sprite):
    sprite.change_x_by(-10)

def up(sprite):
    sprite.change_y_by(10)

def down(sprite):
    sprite.change_y_by(-10)

def move_right(sprite):
    sprite.when_key_pressed("d", right)

def move_left(sprite):
    sprite.when_key_pressed("a", left)
    
def move_up(sprite):
    sprite.when_key_pressed("s", up)
    
def move_down(sprite):
    sprite.when_key_pressed("d", down)
    
def basic_movement(sprite):
    move_right(sprite)
    move_left(sprite)
    move_up(sprite)
    move_down(sprite)