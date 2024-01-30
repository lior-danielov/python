from player import Player

tim = Player("Tim")
# tim._lives = 2
tim.lives = 3

# print(tim)

# modify the player class, so that the player score is increased
# by 1,000 every time their level increases by 1.
# So, if they jump 2 levels, they'll get a bonus of 2,000 added
# to their score. if the player drops a level, they'll lose 1,000 Pts.
# They cannot go below level 1.
tim.level = 2
print(tim)

tim.level += 5
print(tim)

tim.level -= 3
print(tim)

