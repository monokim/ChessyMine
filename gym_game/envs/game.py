import numpy as np
import time
import random
from gym_game.envs.Minecraft import MyMinecraft
from gym_game.envs.util import press_key, click_point

###############################################
# modify here!!!
class Game:
    def __init__(self):
        self.mine = MyMinecraft()
        self.prev_health = 10
        self.cur_health = 10

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
            x1, y1, x2, y2 = self.mine.mc_rect
            click_point([(x1+x2) * 45 / 100, (y1 + y2) / 2])
        elif action == 6:
            x1, y1, x2, y2 = self.mine.mc_rect
            click_point([(x1+x2) * 55 / 100, (y1 + y2) / 2])

    def evaluate(self):
        # return reward
        reward = 0.1
        self.cur_health = self.mine.get_health_bar()
        if self.cur_health < self.prev_health:
            reward -= 10
        self.prev_health = self.cur_health
        return reward

    def is_done(self):
        # return episode is done or not
        if self.cur_health == 0:
            return True
        return False

    def observe(self):
        # return observation data
        return self.mine.screen()

    def view(self):
        # render game
        pass
###############################################
