from pystage.en import Stage

def intro(sprite):
    for i in range(4):
        sprite.move(10)
        sprite.wait(1)
        sprite.think("Loading...")
        sprite.turn_left(90)
        sprite.wait(1)
        sprite.think("")
    sprite.say("Hello!")
    sprite.wait(3)
    sprite.say("")

# Basic Movement

# Parameterized Movement

# Continuous Movement

# Basic Rotation

# Parameterized Rotation

# Continuous Rotation

def game():
    stage = Stage()
    stage.add_backdrop("grid")
    zombie = stage.add_a_sprite()
    zombie.when_program_starts(intro)
    stage.play()

game()
