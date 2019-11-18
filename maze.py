from mcpi.minecraft import Minecraft
from pyautogui import press, typewrite
import pyautogui
import time

def create_ring(mc, pos):
    mc.player.setPos(0, 50, 0)
    pos = mc.player.getPos()
    ring_size = 51
    x = pos.x - int(ring_size/2)
    y = pos.y - 1
    z = pos.z - int(ring_size/2)
    mc.setBlocks(x, y, z, x + ring_size, y, z + ring_size, 42)
    #mc.setBlocks(x, y + ring_size, z, x + ring_size, y + ring_size, z + ring_size, 42)

    for i in range(ring_size):
        mc.setBlocks(x, y, z, x + ring_size, y+i, z, 42)
        mc.setBlocks(x, y, z, x, y+i, z + ring_size, 42)
        mc.setBlocks(x + ring_size, y, z, x + ring_size, y+i, z + ring_size, 42)
        mc.setBlocks(x, y, z + ring_size, x + ring_size, y+i, z + ring_size, 42)

    #set torch
    for space in range(1, 51, 7):
        mc.setBlock(x + space, y + 1, z + 1, 51)
        mc.setBlock(x + space, y + 1, z + ring_size - 1, 51)

        mc.setBlock(x + 1, y + 1, z + space, 51)
        mc.setBlock(x + ring_size - 1, y + 1, z + space, 51)

        mc.setBlock(x + space, y + 1, z + 1, 50)
        mc.setBlock(x + space, y + 1, z + ring_size - 1, 50)

        mc.setBlock(x + 1, y + 1, z + space, 50)
        mc.setBlock(x + ring_size - 1, y + 1, z + space, 50)

def erase_blocks(mc, pos):
    x = pos.x
    y = pos.y
    z = pos.z
    erase_size = 100
    mc.setBlocks(x - erase_size, y-1, z - erase_size, x + erase_size, y + erase_size, z + erase_size, 0)

mc = Minecraft.create()
mc.setting("world_immutable", True)
mc.player.setPos(0, 50, 0)
pos = mc.player.getPos()
create_ring(mc, mc.player.getPos())
