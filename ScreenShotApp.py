import time
import pyautogui


def screenshot():
    name = int(round(time.time()*1000))
    name = 'C:/Users/User/python/Projects/screenshot data/{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()


screenshot()

