import gym
from gym import spaces
import numpy as np
from gym_game.envs.game import Game
import time
from util import Timer

class Env(gym.Env):
    metadata = {'render.modes' : ['human']}
    def __init__(self):
        ###############################################
        # modify here!!!
        self.action_space = spaces.Discrete(7)
        ###############################################
        self.game = Game()
        self.memory = []
        self.counter = 0
        self.timer = Timer()

    def set_device(self, device):
        self.device = device

    def reset(self):
        self.counter = 0
        del self.game
        self.game = Game()
        self.init_minecraft_process()
        obs = self.game.observe(self.device)
        return obs

    def step(self, action):
        self.game.action(action)
        reward = self.game.evaluate()
        done = self.game.is_done()
        obs = self.game.observe(self.device)

        self.counter += 1
        if self.counter > 50:
            self.game.mine.call_mob()
            self.counter = 0

        return obs, reward, done, {}

    def render(self, mode="human", close=False):
        self.game.view()
        pass

    def save_memory(self, file):
        np.save(file, self.memory)
        print(file + " saved")

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def init_minecraft_process(self):
        #self.game.mine.press_resume()
        time.sleep(1)
        self.game.mine.press_respawn()
        self.game.mine.press_respawn()
        self.game.mine.erase_blocks()
        time.sleep(1)
        self.game.mine.create_duel_ring()
        self.game.mine.set_config()
        self.game.mine.call_mob()
