import pyautogui
from pynput.mouse import Listener, Button
import threading

def switchscreenright():
     pyautogui.hotkey("winleft", "ctrlleft", "left")

def switchscreenleft():
    pyautogui.hotkey("winleft", "ctrlleft", "right")

def switchscreenrightstart(x, y, button, pressed):
    if pressed and button == Button.x1:
        switchscreenleft()  

def switchscreenleftstart(x, y, button, pressed):
    if pressed and button == Button.x2:
        switchscreenright()


def Listenerright(): 
    with Listener(on_click=switchscreenrightstart) as listener:
        listener.join() 

def Listenerleft(): 
    with Listener(on_click=switchscreenleftstart) as listener:
        listener.join() 

thread_right = threading.Thread(target=Listenerright)
thread_left = threading.Thread(target=Listenerleft)

thread_right.start()
thread_left.start()

thread_right.join()
thread_left.join()