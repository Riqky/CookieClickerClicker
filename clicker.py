import _thread
from pynput import mouse
from pynput.mouse import Button, Controller


def click(delay: float, position: tuple[int, int]) -> None:
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    clicker = Controller()
    clicker.position = position

    while True:
        clicker.click(Button.left)


def on_click(x, y, button, pressed):
    if button == mouse.Button.right:
        _thread.interrupt_main()


if __name__ == '__main__':
    #for i in range(0, 10):
    _thread.start_new_thread(click, (0, (700, 600)))

    # listener = mouse.Listener(on_click=on_click)
    # listener.start()

    while True:
        pass
