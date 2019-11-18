from mcpi.minecraft import Minecraft
from pyautogui import press, typewrite
import pyautogui
import time
import util

class Minecraft:
    def __init__(self):
        self.mc = Minecraft.create()
        self.mc.setting("world_immutable", True)
        self.mc_rect = util.get_screen_rect()

        # need to find
        self.mc_center_pos = [0, 0]
        self.health_pos = [0, 0]
        self.resume_buttion_pos = [0, 0]


    def create_duel_ring():
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

        # set torch and fire
        for space in range(1, 15, 6):
            self.mc.setBlock(x+1, y + 1, z+ space, 51)
            self.mc.setBlock(x + ring_size[0] - 1, y + 1, z+ space, 51)
            self.mc.setBlock(x+1, y + 1, z+ space, 50)
            self.mc.setBlock(x + ring_size[0] - 1, y + 1, z+ space, 50)

    def erase_blocks():
        x = 0
        y = 50
        z = 0
        erase_size = 100
        self.mc.setBlocks(x - erase_size, y-1, z - erase_size, x + erase_size, y + erase_size, z + erase_size, 0)

    def set_config():
        command = ['/op mingoooose', '/give mingoooose iron_sword']
        for comm in command:
            util.type_command(comm)

    def call_zombie():
        com = '/summon zombie 0 50 20'
        util.type_command(comm)

    def screen():
        util.get_screen(self.mc_rect)

# /op mingoooose
# /give mingoooose iron_sword
# /summon zombie 0 50 20
