class Graphic:
    def __init__(self):
        self.x = 0
        self.y = 0


class Rectangle(Graphic):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height


class Button:
    def __init__(self, button):
        if button == 'left' or button == 'right':
            self.button = button
        else:
            self.button = 'undefined'


class MouseEvent(Button):
    def __init__(self, button, x, y):
        super().__init__(button)
        self.create_rectangle(x, y)
        print(
            f'{self.button} button is clicked on x: {x}, y: {y}. Area of rectangle from zero point is {self.rectangle.width * self.rectangle.height}.')

    def create_rectangle(self, x, y):
        self.rectangle = Rectangle(x, y)


click = MouseEvent('left', 10, 20)
