import os
import pyautogui as pg

def screenshot():
    pg.screenshot('my_screenshot.png')

def open_browser():
    os.system("sensible-browser")

def calculator():
    os.system("gnome-calculator")

def shutdown():
    os.system("init 0")

def reboot():
    os.system("reboot")

def close():
    x, y = pg.locateCenterOnScreen('close.png')
    pg.click(x, y)

def minimize():
    x, y = pg.locateCenterOnScreen('minimize.png')
    pg.click(x, y)

def maximize():
    x, y = pg.locateCenterOnScreen('maximize.png')
    pg.click(x, y)
