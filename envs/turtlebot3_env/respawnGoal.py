#!/usr/bin/env python
#################################################################################
# Copyright 2018 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#################################################################################

# Authors: Gilbert, Eduardo #
import rospy
import random
import time
import os
from gazebo_msgs.srv import SpawnModel, DeleteModel
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Pose

class Respawn():
    def __init__(self):
        self.goal_position = Pose()
        self.goal_x_list = None
        self.goal_y_list = None
        self.len_goal_list = None
        self.index = None
        self.last_index = None
        self.init_goal_x = None
        self.init_goal_y = None
        self.goal_position.position.x = None
        self.goal_position.position.y = None
        self.modelPath = os.path.dirname(os.path.realpath(__file__))
        self.modelPath = self.modelPath.replace('ros_gazebo_gym/envs/turtlebot3_env',
                                                'ros_gazebo_gym/envs/turtlebot3_env/turtlebot3_square/goal_box/model.sdf')
        self.f = open(self.modelPath, 'r')
        self.model = self.f.read()
        self.modelName = 'goal'
        self.sub_model = rospy.Subscriber('gazebo/model_states', ModelStates, self.checkModel)
        self.check_model = False


    def checkModel(self, model):
        self.check_model = False
        for i in range(len(model.name)):
            if model.name[i] == "goal":
                self.check_model = True

    def respawnModel(self):
        while True:
            if not self.check_model:
                rospy.wait_for_service('gazebo/spawn_sdf_model')
                spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
                spawn_model_prox(self.modelName, self.model, 'robotos_name_space', self.goal_position, "world")
                rospy.loginfo("Goal position : %.1f, %.1f", self.goal_position.position.x,
                              self.goal_position.position.y)
                break
            else:
                pass

    def deleteModel(self):
        while True:
            if self.check_model:
                rospy.wait_for_service('gazebo/delete_model')
                del_model_prox = rospy.ServiceProxy('gazebo/delete_model', DeleteModel)
                del_model_prox(self.modelName)
                break
            else:
                pass

    def initIndex(self):
        self.index = 0
        self.goal_position.position.x = self.init_goal_x
        self.goal_position.position.y = self.init_goal_y
        self.last_index = self.index

    def setGoalList(self, goal_list):
        self.goal_x_list = [p[0] for p in goal_list]
        self.goal_y_list = [p[1] for p in goal_list]
        self.len_goal_list = len(self.goal_x_list)
        self.init_goal_x = self.goal_x_list[0]
        self.init_goal_y = self.goal_y_list[0]
        self.initIndex()

    def getPosition(self, position_check=False):

        if position_check:
            self.deleteModel()
            self.index = (self.last_index + 1) % self.len_goal_list
            self.last_index = self.index

            self.goal_position.position.x = self.goal_x_list[self.index]
            self.goal_position.position.y = self.goal_y_list[self.index]
            #time.sleep(0.5)
            self.respawnModel()
        else:
            self.respawnModel()
        print(f'New goal position: {self.goal_position.position.x:.2f}, {self.goal_position.position.y:.2f}')

        return self.goal_position.position.x, self.goal_position.position.y
