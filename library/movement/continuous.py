# Continuous movement - as long as the key is pressed, you will move in that direction

from library.movement.constants import DISTANCE_SMALL

def right_continuous(sprite):
    while sprite.key_pressed("d"):
        sprite.change_x_by(DISTANCE_SMALL)

def left_continuous(sprite):
    while sprite.key_pressed("a"):
        sprite.change_x_by(-DISTANCE_SMALL)

def up_continuous(sprite):
    while sprite.key_pressed("w"):
        sprite.change_y_by(DISTANCE_SMALL)

def down_continuous(sprite):
    while sprite.key_pressed("d"):
        sprite.change_y_by(-DISTANCE_SMALL)

def move_right_continuous(sprite, key="d"):
    sprite.when_key_pressed(key, right_continuous)

def move_left_continuous(sprite, key="a"):
    sprite.when_key_pressed(key, left_continuous)

def move_up_continuous(sprite, key="w"):
    sprite.when_key_pressed(key, up_continuous)

def move_down_continuous(sprite, key="s"):
    sprite.when_key_pressed(key, down_continuous)

def move_continous(sprite):
    move_right_continuous(sprite)
    move_left_continuous(sprite)
    move_up_continuous(sprite)
    move_down_continuous(sprite)