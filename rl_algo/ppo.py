
import gym
import envs
import numpy as np
import os
import sys

from stable_baselines3 import PPO
from stable_baselines3.ppo import MlpPolicy
from stable_baselines3.common.env_util import make_vec_env

import matplotlib.pyplot as plt
import rospy
from gym import wrappers

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":

    env_name='TurtleBot3_Env-v0'
    rospy.init_node(env_name.replace('-', '_'))
    env = gym.make("TurtleBot3_Env-v0")
    cdir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(cdir)
    print(cdir)
    outdir = cdir + "/data"
    env = wrappers.Monitor(env, outdir, force=True)
    env = make_vec_env(lambda:env, n_envs=1)
    model = PPO(MlpPolicy, env, learning_rate=0.001, n_steps=40, verbose=1, tensorboard_log="./ppo_turtle_tensorboard/")
    model.learn(total_timesteps=10000)
    model.save("ppo_turtle")
    plt.show()

    #del model