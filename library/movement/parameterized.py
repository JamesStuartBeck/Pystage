# Parameterized movement - move your character x "units" in a cardinal direction

from library.movement.constants import DISTANCE_LARGE

def right_parameterized(sprite):
    sprite.change_x_by(DISTANCE_LARGE)

def left_parameterized(sprite):
    sprite.change_x_by(-DISTANCE_LARGE)

def up_parameterized(sprite):
    sprite.change_y_by(DISTANCE_LARGE)

def down_parameterized(sprite):
    sprite.change_y_by(-DISTANCE_LARGE)

def move_right_parameterized(sprite, key="d"):
    sprite.when_key_pressed(key, right_parameterized)

def move_left_parameterized(sprite, key="a"):
    sprite.when_key_pressed(key, left_parameterized)

def move_up_parameterized(sprite, key="w"):
    sprite.when_key_pressed(key, up_parameterized)

def move_down_parameterized(sprite, key="s"):
    sprite.when_key_pressed(key, down_parameterized)

def move_continous(sprite):
    move_right_parameterized(sprite)
    move_left_parameterized(sprite)
    move_up_parameterized(sprite)
    move_down_parameterized(sprite)