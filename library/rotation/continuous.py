# Continuous rotation - rotate clockwise or counter-clockwise as long as the key is pressed

from library.rotation.constants import ROTATION_MIN

def clockwise_continuous(sprite):
    while sprite.key_pressed("q"):
        sprite.turn_right(ROTATION_MIN)

def counter_clockwise_continuous(sprite):
    while sprite.key_pressed("e"):
        sprite.turn_left(ROTATION_MIN)

def turn_clockwise_continuous(sprite, key="q"):
    sprite.when_key_pressed(key, clockwise_continuous)

def turn_counter_clockwise_continuous(sprite, key="e"):
    sprite.when_key_pressed(key, counter_clockwise_continuous)

def move_continous(sprite):
    turn_clockwise_continuous(sprite)
    turn_counter_clockwise_continuous(sprite)