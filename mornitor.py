import cv2
import pyautogui
import numpy as np
import torch

class Monitor():
    def __init__(self, device, region):
        self.device = device
        self.region = region
        self.screen = None

    def caputre_screen(self):
        self.screen = np.array(pyautogui.screenshot(region=self.region))

    def get_screen(self, pytorch=False, size=(256, 256)):
        if self.screen == None:
            self.caputre_screen()

        if pytorch == True:
            image = cv2.resize(self.screen, size).transpose((2, 0, 1))
            image = np.ascontiguousarray(image, dtype=np.float32) / 255
            return torch.from_numpy(image).unsqueeze(0).to(self.device)
        else:
            return self.screen

    def get_check_screen(self):
        frame = cv2.resize(self.screen, (int(self.screen.shape[1]/scale), int(self.screen.shape[0]/scale)))
        frame = frame[0:int(frame.shape[0]*85/100), 0:int(frame.shape[1]*75/100)]
        H, W, _ = frame.shape
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        blurred = cv2.GaussianBlur(gray, (11, 11), 0)
        _, thres = cv2.threshold(blurred, 40, 255, cv2.THRESH_BINARY)
        kernel = np.ones((7, 7), np.uint8)
        dilate = cv2.dilate(thres, kernel)
        erode = cv2.erode(dilate, kernel)
        return erode
