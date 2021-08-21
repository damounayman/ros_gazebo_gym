import gym
import envs
from stable_baselines3 import PPO
import rospy

env_name='TurtleBot3_Circuit_Simple-v0'
rospy.init_node(env_name.replace('-', '_'))
env = gym.make("TurtleBot3_Circuit_Simple-v0")

observation = env.reset()

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)

    if done:
        observation = env.reset()

env.close()