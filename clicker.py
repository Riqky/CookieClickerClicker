import _thread
import time

from pynput import mouse
from pynput import keyboard
from pynput.mouse import Button, Controller
from typing import Tuple

def on_click(key):
    if key.char == "x":
        _thread.interrupt_main()

def click(delay: float, position: Tuple[int, int]) -> None:
    listener = keyboard.Listener(on_press=on_click)
    listener.start()

    clicker = Controller()
    clicker.position = position

    while True:
        clicker.click(Button.left)
        time.sleep(delay)


if __name__ == '__main__':
    _thread.start_new_thread(click, (0, (700, 600)))

    # listener = mouse.Listener(on_click=on_click)
    # listener.start()

    while True:
        pass
