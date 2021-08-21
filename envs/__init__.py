from gym.envs.registration import register

register(id='Turtlebot3Env-v0',
    entry_point='envs.turtlebot3_env:TurtleBot3Env'
)

from gym.envs.registration import register

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
