import cv2
import numpy as np
import pyperclip
import pyautogui
from selenium import webdriver
#from matplotlib import pyplot as plt

class selcv():
    def __init__(self, chromedriver_path):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_argument("--window-size=1980x1020")
        self.driver = webdriver.Chrome(chromedriver_path, options=self.options)

    def driver_get(self,url):
        self.driver.get(url)

    def find_element_screen_shot(self, element_name, find_type, name):
        if(find_type == 'id'):
            element = self.driver.find_element_by_id(name)
        elif(find_type == 'class'):
            element = self.driver.find_element_by_class_name(name)
        elif(find_type == 'xpath'):
            element = self.driver.find_element_by_xpath(name)
        else:
            return('type: [id, class, xpath]')
        with open("img/"+element_name+".png", "wb") as file:
            file.write(element.screenshot_as_png)

    def find_element_by_tm(self, element_name):
        element_img = cv2.imread("img/"+element_name+".png")
        screen = np.array(pyautogui.screenshot())
        res = cv2.matchTemplate(screen, element_img, cv2.TM_CCOEFF_NORMED)
        w = element_img.shape[::-1][1]
        h = element_img.shape[::-1][2]
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        return top_left
        # for debug
        #bottom_right = (top_left[0] + w, top_left[1] + h)
        #cv2.rectangle(screen,top_left, bottom_right, 255, 2)
        #plt.imshow(screen,cmap = 'gray')
        #plt.show()

    def click_paste_text(temp, position, text):
        # temp = <selcv.selcv object at 0x0000020B4A9787F0>
        px = position[0]+20
        py = position[1]+20
        pyperclip.copy(text)
        pyautogui.click(x=px, y=py)
        pyautogui.hotkey('ctrl', 'v')

    def click(temp, position):
        px = position[0]+20
        py = position[1]+20
        pyautogui.click(x=px, y=py)
    