import numpy as np
import time
import random
import pyautogui
from gym_game.envs.Minecraft import MyMinecraft
from gym_game.envs.util import press_key, click_point


###############################################
# modify here!!!
class Game:
    def __init__(self):
        self.mine = MyMinecraft()
        self.prev_health = 10
        self.cur_health = 10
        self.screen = None

    def action(self, action):
        # do action
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
            pyautogui.moveRel(-100, 0)
            click_point()
        elif action == 6:
            pyautogui.moveRel(100, 0)
            click_point()

    def evaluate(self):
        # return reward
        reward = 0.1

        # about targeting
        if self.mine.check_zombie():
            reward += 1

        # does strike or not
        """
        if self.mine.is_strike():
            reward += 10
        """
        # about health
        """
        self.cur_health = self.mine.get_health_bar()
        if self.cur_health < self.prev_health:
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

    def observe(self, device):
        # return observation data
        screen = self.mine.screen(device)
        self.screen = screen
        return screen

    def view(self):
        # render game
        pass
###############################################
