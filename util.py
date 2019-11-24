import cv2
import pyautogui
import numpy as np
import time
import torch
import win32gui

def get_screen(screen, size=(96, 96)):
    image = pyautogui.screenshot(region=screen)
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, size)
    image = np.ascontiguousarray(image, dtype=np.float32) / 255
    image = torch.from_numpy(image).unsqueeze(0).unsqueeze(0)
    return image

def get_screen_rect(caption='Minecraft 1.11.2'):
    hwnd = win32gui.FindWindow(None, caption)
    rect = win32gui.GetWindowRect(hwnd)
    return rect

def click_point(pos=None):
    pyautogui.click(pos)

def press_key(key):
    pyautogui.keyDown(key)
    time.sleep(0.1)
    pyautogui.keyUp(key)

def type_command(comm):
    for c in comm:
        pyautogui.press(c)
    pyautogui.press('enter')

def get_pixel(pos = None):
    image = pyautogui.screenshot()
    image = np.array(image)
    if pos == None:
        pos = pyautogui.position()
    pixel = image[pos[1], pos[0]]
    return [pixel[0], pixel[1], pixel[2]]
