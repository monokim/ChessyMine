import cv2
import pyautogui
import numpy as np
import time
import torch
import win32gui

def get_screen_color(screen):
    image = pyautogui.screenshot(region=screen)
    image = np.array(image)
    return image

def get_screen(screen, size=(256, 256), device = None):
    image = pyautogui.screenshot(region=screen)
    image = np.array(image)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, size).transpose((2, 0, 1))
    image = np.ascontiguousarray(image, dtype=np.float32) / 255
    return torch.from_numpy(image).unsqueeze(0).to(device)

def get_screen_rect(caption='Minecraft 1.11.2'):
    hwnd = win32gui.FindWindow(None, caption)
    rect = win32gui.GetWindowRect(hwnd)
    screen_rect = (rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1])
    return rect

def click_point(pos=None):
    pyautogui.click(pos)

def press_key(key):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)

def type_command(comm):
    for c in comm:
        pyautogui.press(c, pause=0.05)
    pyautogui.press('enter')
