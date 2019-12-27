import time
import pyautogui
import win32gui

def get_screen_rect(caption='Minecraft 1.11.2'):
    hwnd = win32gui.FindWindow(None, caption)
    rect = win32gui.GetWindowRect(hwnd)
    screen_rect = (rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1])
    return rect

def click_point(pos=None, left=True):
    if left:
        pyautogui.click(pos)
    else:
        pyautogui.rightClick(pos)

def press_key(key):
    pyautogui.press(key, pause=0.01)

def type_command(comm):
    for c in comm:
        pyautogui.press(c, pause=0.05)
    pyautogui.press('enter')

class Timer():
    def __init__(self):
        self.times = []
        self.cnt = 0

    def set_timer(self, name="timer"):
        flag = False
        for i, t in enumerate(self.times):
            if t[1] == name:
                flag = True
                t[0] = time.time()
                break

        if flag == False:
            self.times.append([time.time(), name])

    def print_time(self, name="timer"):
        flag = False
        for i, t in enumerate(self.times):
            if t[1] == name:
                flag = True
                print(name + " takes (%.5f)s" % (time.time() - t[0]))
                break

        if flag == False:
            raise Exception("There is no timer")

    def delete_timer(self, name = None):
        for i, t in enumerate(self.times):
            if t[1] == name:
                self.times.pop(i)
                break
