# Parameterized rotation - rotate your character x degrees clockwqise or counter-clockwise

from library.rotation.constants import ROTATION_LARGE

def clockwise_parameterized(sprite):
    sprite.turn_right(ROTATION_LARGE)

def counter_clockwise_parameterized(sprite):
    sprite.turn_left(ROTATION_LARGE)

def move_right_parameterized(sprite, key="q"):
    sprite.when_key_pressed(key, clockwise_parameterized)

def move_left_parameterized(sprite, key="e"):
    sprite.when_key_pressed(key, counter_clockwise_parameterized)

def move_continous(sprite):
    move_left_parameterized(sprite)
    move_right_parameterized(sprite)
