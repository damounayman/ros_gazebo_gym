import numpy
import random

from numpy.lib.function_base import append

test = []
for i in range(20):
    goal_x = random.randrange(-12, 13) / 10.0
    rand = random.randint(0, 1)
    goal_y = 0.5 *rand -(1-rand)*0.5
    temp=[goal_x,goal_y]
    test.append(temp)

print(test)