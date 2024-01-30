`def turn_right():
    if front_is_clear():
        move()
        turn_right()
    else:
        move()

def skip_wall():
    turn_left()
    repeat 5:
        if front_is_clear():
            turn_right()
        else:
            move()
    turn_right()
    
while not at_goal():
    if wall_in_front():
        skip_wall()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
