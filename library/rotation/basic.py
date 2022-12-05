# basic rotation - rotate your character 90 degress colockwise or counter-clockwise

def clockwise(sprite):
    sprite.turn_right(90)

def counter_clockwise(sprite):
    sprite.turn_left(90)

def turn_clockwise(sprite):
    sprite.when_key_pressed("q", clockwise)

def turn_counter_clockwise(sprite):
    sprite.when_key_pressed("e", counter_clockwise)
    
def basic_movement(sprite):
    turn_clockwise(sprite)
    turn_counter_clockwise(sprite)