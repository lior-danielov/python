def turn_right():
    if front_is_clear() or wall_in_front(): 
        
        turn_right()
    else:
        turn_right()
def skip_wall():
    turn_left()
    repeat 5:
        if front_is_clear():
            turn_right()
        else:
            turn_right()
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
