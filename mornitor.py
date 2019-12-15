import cv2
import pyautogui
import numpy as np
import torch

class Monitor:
    __instance = None
    def get_instance():
        if Monitor.__instance == None:
            Monitor()
        return Monitor.__instance

    def __init__(self, device, region):
        if Monitor.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Monitor.__instance = self

        self.play_flag = False
        self.device = device
        self.region = region
        self.screen = np.array(pyautogui.screenshot(region=self.region))
        self.gray = None
        self.thres = None

    def caputre_screen(self):
        self.screen = np.array(pyautogui.screenshot(region=self.region))

    def get_screen(self, pytorch=False, size=(256, 256)):
        if pytorch == True:
            image = cv2.resize(self.screen, size).transpose((2, 0, 1))
            image = np.ascontiguousarray(image, dtype=np.float32) / 255
            return torch.from_numpy(image).unsqueeze(0).to(self.device)
        else:
            return self.screen

    def get_check_screen(self):
        scale = 2
        frame = cv2.resize(self.screen, (int(self.screen.shape[1]/scale), int(self.screen.shape[0]/scale)))
        frame = frame[0:int(frame.shape[0]*85/100), 0:int(frame.shape[1]*75/100)]
        H, W, _ = frame.shape
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        self.gray = gray
        blurred = cv2.GaussianBlur(gray, (11, 11), 0)
        _, thres = cv2.threshold(blurred, 40, 255, cv2.THRESH_BINARY)
        kernel = np.ones((7, 7), np.uint8)
        dilate = cv2.dilate(thres, kernel)
        erode = cv2.erode(dilate, kernel)
        self.thres = erode
        return erode

    def show_screen(self):
        """
        cv2.imshow('gray', self.gray)
        cv2.imshow('thres', self.thres)
        if self.play_flag:
            cv2.waitKey(1)
        else:
            cv2.waitKey(0)
            self.play_flag = True
        """
