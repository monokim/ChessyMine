from mcpi.minecraft import Minecraft
from pyautogui import press, typewrite
import pyautogui
import time
import sys
import os
import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from util import type_command, click_point, get_screen_rect
from mornitor import Monitor

class MyMinecraft:
    def __init__(self):
        self.mc = Minecraft.create()
        self.mc.setting("world_immutable", True)
        self.mc_rect = get_screen_rect()
        self.monitor = Monitor.get_instance()

    def create_duel_ring(self):
        self.erase_blocks()
        self.mc.player.setPos(0, 50, 0)
        pos = self.mc.player.getPos()
        ring_size = [5, 14]
        x = int(pos.x) - 3
        y = int(pos.y) - 1
        z = int(pos.z) - 2

        # set bottom ring
        self.mc.setBlocks(x, y, z, x + ring_size[0], y, z + ring_size[1], 42)

        # set walls
        for i in range(10):
            self.mc.setBlocks(x, y, z, x + ring_size[0], y+i, z, 42)
            self.mc.setBlocks(x, y, z, x, y+i, z + ring_size[1], 42)
            self.mc.setBlocks(x + ring_size[0], y, z, x + ring_size[0], y+i, z + ring_size[1], 42)
            self.mc.setBlocks(x, y, z + ring_size[1], x + ring_size[0], y+i, z + ring_size[1], 42)

        """
        # set torch and fire
        for space in range(1, 15, 6):
            self.mc.setBlock(x, y + 1, z+ space, 51)
            self.mc.setBlock(x + ring_size[0], y + 1, z+ space, 51)
            self.mc.setBlock(x, y + 1, z+ space, 50)
            self.mc.setBlock(x + ring_size[0], y + 1, z+ space, 50)
        """

    def erase_blocks(self):
        x = 0
        y = 50
        z = 0
        erase_size = 100
        self.mc.setBlocks(x - erase_size, y-10, z - erase_size, x + erase_size, y + erase_size, z + erase_size, 0)

    def set_config(self):
        print("set_config")
        time.sleep(0.5)
        command = ['/clear', '/give @a iron_sword', '/time set 1000', '/weather clear']
        for comm in command:
            type_command(comm)

    def call_mob(self):
        print("call_mob")
        com = '/summon husk 0 50 10 {IsBaby:0}'
        type_command(com)

    def screen(self):
        return self.monitor.get_screen(pytorch=True)

    def press_resume(self):
        x1, y1, x2, y2 = self.mc_rect
        click_point([(x1+x2) / 2, y1 + (y2 - y1) / 3])

    def press_respawn(self):
        x1, y1, x2, y2 = self.mc_rect
        click_point([(x1+x2) / 2, y1 + 320])

    def get_health_bar(self):
        x, y, _, _ = self.mc_rect
        health = 0
        pos = [295, 490]
        image = self.monitor.get_screen()
        for i in range(0, 10):
            # left
            pixel = image[pos[1]][pos[0]]
            if (pixel == [255, 19, 19]).all():
                health += 0.5
            # right
            pos[0] += 5
            pixel = image[pos[1], pos[0]]
            if (pixel == [255, 19, 19]).all():
                health += 0.5
            # next
            pos[0] += 11
        return health

    def check_zombie(self):
        image = self.monitor.get_check_screen()
        arr = np.nonzero(image)
        avg_h = 0
        avg_w = 0
        if len(arr[0]) > 0:
            #avg_h = int(np.sum(arr[0]) / len(arr[0]))
            avg_w = int(np.sum(arr[1]) / len(arr[1]))
            if avg_w >= (self.mc_rect[2] / 2) - 100 and avg_w <= (self.mc_rect[2] / 2) + 100:
                return True

        return False

    def show_screen(self):
        self.monitor.show_screen()
