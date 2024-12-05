from pynput.mouse import Listener,Controller,Button
import os
import threading
import time
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
class Clicker(threading.Thread):
    def __init__(self,button):
        super().__init__()
        self.running = False
        self.p_running = True
        self.button = button
    def run(self):
        while self.p_running:
            time.sleep(0.1)
            while self.running:
                mouse.click(self.button)
                time.sleep(0.05) # change to adjust the cps(clik per second)
mouse = Controller()
click_right = Clicker(Button.right)
click_left = Clicker(Button.left)
click_left.start()
click_right.start()

def on_click(x,y,button,pressed):
    if pressed:
        if button.name == "x1":
            click_right.running = True
        if button.name == "x2":
            click_left.running = True
    else:
        if button.name == 'x1':
            click_right.running = False
        if button.name == 'x2':
            click_left.running = False

with Listener(on_click=on_click) as listener:
    listener.join()
