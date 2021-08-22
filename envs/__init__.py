from gym.envs.registration import register
import random
register(
    id='TurtleBot3-v0',
    entry_point='envs.turtlebot3_env:TurtleBot3Env'
)

goal_list = [   [0.505, 2.005],
                [1.005, 2.505],
                [2.005, 2.505],
                [2.505, 2.005],
                [2.505, 1.005],
                [2.005, 0.505],
                [1.005, 0.505],
                [0.505, 1.005]] 

max_env_size = 3

register(
    id='TurtleBot3_Circuit_Simple-v0',
    entry_point='envs.turtlebot3_env:TurtleBot3Env',
    kwargs={'goal_list': goal_list, 'max_env_size': max_env_size}
)

goal_list = [   [0.505, 4.005],
                [1.005, 4.505],
                [2.005, 4.505],
                [2.505, 4.005],
                [2.505, 3.005],
                [3.005, 2.505],
                [4.005, 2.505],
                [4.505, 2.005],
                [4.505, 1.005],
                [4.005, 0.505],
                [1.005, 0.505],
                [0.505, 1.005],
                [0.505, 2.5]]

max_env_size = 5

register(
    id='TurtleBot3_Circuit_Simple_Continuous-v0',
    entry_point='envs.turtlebot3_env:TurtleBot3Env',
    kwargs={'goal_list': goal_list, 'max_env_size': max_env_size, 'continuous': True}
)


goal_list = []
for i in range(20):
    goal_x = random.randrange(-12, 13) / 10.0
    rand = random.randint(0, 1)
    goal_y = 0.5 *rand -(1-rand)*0.5
    temp=[goal_x,goal_y]
    goal_list.append(temp)

max_env_size = 5

register(
    id='TurtleBot3_Env-v0',
    entry_point='envs.turtlebot3_env:TurtleBot3Env',
    kwargs={'goal_list': goal_list, 'max_env_size': max_env_size, 'continuous': True}
)