from mcpi.minecraft import Minecraft
from pyautogui import press, typewrite
import pyautogui
import time

from gym_game.envs.util import type_command, click_point, get_screen_rect, get_screen, get_screen_color

class MyMinecraft:
    def __init__(self):
        self.mc = Minecraft.create()
        self.mc.setting("world_immutable", True)
        self.mc_rect = get_screen_rect()

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

        # set torch and fire
        for space in range(1, 15, 6):
            self.mc.setBlock(x, y + 1, z+ space, 51)
            self.mc.setBlock(x + ring_size[0], y + 1, z+ space, 51)
            self.mc.setBlock(x, y + 1, z+ space, 50)
            self.mc.setBlock(x + ring_size[0], y + 1, z+ space, 50)

    def erase_blocks(self):
        x = 0
        y = 50
        z = 0
        erase_size = 100
        self.mc.setBlocks(x - erase_size, y-10, z - erase_size, x + erase_size, y + erase_size, z + erase_size, 0)

    def set_config(self):
        print("set_config")
        time.sleep(0.5)
        command = ['1qqq', '/give mingoooose iron_sword', '/time set 13000', '/weather clear']
        for comm in command:
            type_command(comm)

    def call_mob(self):
        print("call_mob")
        com = '/summon zombie 0 50 10 {IsBaby:0}'
        type_command(com)

    def screen(self, device):
        return get_screen(self.mc_rect, device=device)

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
        image = get_screen_color(self.mc_rect)
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

    def is_strike(self):
        return false
        image = get_screen_color(self.mc_rect)
        w, h, _ = image.shape
        for y in range(h):
            for x in range(w):
                pixel = image[y][x]
                if (pixel == [59,14,6]).all() or (pixel == [57, 11, 5]).all():
                    print("strike")
                    return True
        print("no strike")
        return False

    def check_zombie(self):
        image = get_screen_color(self.mc_rect)
        h, w, c = image.shape
        center = [int(h / 2), int(w / 2)]
        area = 50
        r_avg = 0
        g_avg = 0
        b_avg = 0
        for h in range(center[0] - area, center[0] + area):
            for w in range(center[1] - area, center[1] + area):
                r, g, b = image[h][w]
                r_avg += r
                g_avg += g
                b_avg += b

        r_avg /= (area * area * 2 * 2)
        g_avg /= (area * area * 2 * 2)
        b_avg /= (area * area * 2 * 2)

        if r_avg < 80 and g_avg < 80 and b_avg < 80:
            #print("zombie detected")
            return True

        #print("not detected")
        return False

# /op mingoooose
# /give mingoooose iron_sword
# /summon zombie 0 50 20
