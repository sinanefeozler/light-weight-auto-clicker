from pynput.mouse import Listener,Controller,Button
import os
import threading
import time

def clearConsole():
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')

class Clicker(threading.Thread):
    def __init__(self,button):
        super().__init__()
        self.running = False
        self.button = button
        self.macro = False
    
    def run(self):
        while True:
            time.sleep(0.1)
            while self.running and self.macro:
                mouse.click(self.button)
                time.sleep(0.05)

mouse = Controller()
click_right = Clicker(Button.right)
click_left = Clicker(Button.left)
click_left.start()
click_right.start()

print(f"Right macro : {click_right.macro}\nLeft macro : {click_left.macro}")
def on_click(x,y,button,pressed):
    if pressed:
        if button.name == "right":
            click_right.running = True
        if button.name == "left":
            click_left.running = True
        if button.name == "button9": # change this to adjust the starter
            if click_left.macro:
                click_left.macro = False
            else:
                click_left.macro = True
            clearConsole()
            print(f"Right macro : {click_right.macro}\nLeft macro : {click_left.macro}")
        if button.name == "button8": # change this to adjust the starter
            if click_right.macro:
                click_right.macro = False
            else:
                click_right.macro = True
            clearConsole()
            print(f"Right macro : {click_right.macro}\nLeft macro : {click_left.macro}")
    else:
        if button.name == 'right':
            click_right.running = False
        if button.name == 'left':
            click_left.running = False

with Listener(on_click=on_click) as listener:
    listener.join()
