import numpy as np
import time
import random
import pyautogui
from . import Minecraft

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from util import press_key, click_point


###############################################
# modify here!!!
class Game:
    def __init__(self):
        self.mine = Minecraft.MyMinecraft()
        self.prev_health = 10
        self.cur_health = 10

    def action(self, action):
        # do action
        move = 30
        if action == 0:
            press_key('w')
        elif action == 1:
            press_key('s')
        elif action == 2:
            press_key('a')
        elif action == 3:
            press_key('d')
        elif action == 4:
            click_point()
        elif action == 5:
            click_point(left=False)
        elif action == 6:
            pyautogui.moveRel(-move, 0)
        elif action == 7:
            pyautogui.moveRel(move, 0)
        elif action == 8:
            pyautogui.moveRel(0, -move)
        elif action == 9:
            pyautogui.moveRel(0, move)

    def evaluate(self):
        # return reward
        reward = 0.1

        # about targeting
        """
        if self.mine.check_zombie():
            print("detected")
            reward += 1
        else:
            print("not detected")
        # does strike or not

        if self.mine.is_strike():
            reward += 10
        # about health
        self.cur_health = self.mine.get_health_bar()
        if self.prev_health - self.cur_health >= 1:
            reward -= 10
            self.prev_health = self.cur_health

        """

        return reward

    def is_done(self):
        # return episode is done or not
        #if self.cur_health == 0:
        if self.mine.get_health_bar() == 0:
            return True
        return False

    def observe(self):
        # return observation data
        return self.mine.screen()

    def view(self):
        # render game
        self.mine.show_screen()
        #pass
###############################################
