from ..Context import Context
context = Context()

class Settings():
    def __init__(self):
        print("Settings")

    def test(self):
        test_file = open('why.txt','r')

        cords = test_file.read()

        print(cords)
        if context.mouse_click == 1:
            print("клик")

