from mcpi.minecraft import Minecraft
from pyautogui import press, typewrite
import pyautogui
import time

class Minecraft:
    def __init__(self):
        self.mc = Minecraft.create()
        self.mc.setting("world_immutable", True)

    def create_duel_ring():
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

def erase_blocks(mc):
    x = 0
    y = 50
    z = 0
    erase_size = 100
    mc.setBlocks(x - erase_size, y-1, z - erase_size, x + erase_size, y + erase_size, z + erase_size, 0)

erase_blocks(mc)
create_duel_ring(mc)

# /op mingoooose
# /give mingoooose iron_sword
# /summon zombie 0 50 20
