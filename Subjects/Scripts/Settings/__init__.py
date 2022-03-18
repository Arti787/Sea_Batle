from ..Context import Context
context = Context()

class Settings():
    def __init__(self):
        print("Settings")

    def test(self):
        print(context.mouse_click)
        while context.mouse_click == 1:
            print("клик")

