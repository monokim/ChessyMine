from mcpi.minecraft import Minecraft
from pyautogui import press, typewrite
import pyautogui
import time

def create_ring(mc):
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


def create_duel_ring(mc):
    mc.player.setPos(0, 50, 0)
    pos = mc.player.getPos()
    ring_size = [5, 14]
    x = int(pos.x) - 3
    y = int(pos.y) - 1
    z = int(pos.z) - 2
    mc.setBlocks(x, y, z, x + ring_size[0], y, z + ring_size[1], 42)
    for i in range(10):
        mc.setBlocks(x, y, z, x + ring_size[0], y+i, z, 42)
        mc.setBlocks(x, y, z, x, y+i, z + ring_size[1], 42)
        mc.setBlocks(x + ring_size[0], y, z, x + ring_size[0], y+i, z + ring_size[1], 42)
        mc.setBlocks(x, y, z + ring_size[1], x + ring_size[0], y+i, z + ring_size[1], 42)


    for space in range(1, 15, 3):
        for yy in range(1, 10, 2):
            mc.setBlock(x-1, y + yy, z + space, 42)
            mc.setBlock(x + ring_size[0]+1 , y + yy, z+ space, 42)

            mc.setBlock(x, y + yy, z+ space, 51)
            mc.setBlock(x + ring_size[0] , y + yy, z+ space, 51)

            mc.setBlock(x, y + yy, z+ space, 50)
            mc.setBlock(x + ring_size[0], y + yy, z+ space, 50)


def erase_blocks(mc):
    x = 0
    y = 50
    z = 0
    erase_size = 100
    mc.setBlocks(x - erase_size, y-1, z - erase_size, x + erase_size, y + erase_size, z + erase_size, 0)

mc = Minecraft.create()
mc.setting("world_immutable", True)
erase_blocks(mc)
create_duel_ring(mc)
#create_ring(mc, mc.player.getPos())

# /op mingoooose
# /give mingoooose iron_sword
# /summon zombie 0 50 20
