import os

class Brick():
    def __init__(self, size, screen, strength):
        self.screen = screen
        self.size = size
        self.strength = strength

class  TransparentB(Brick):
    def __init__(self):
        self.damn = "none given"
        self.strength = 0
    
class RedB(Brick):
    def __init__(self, size, screen):
        super().__init__(size, screen, 1)
    
    def place(self, x, y):
        self.x = x
        self.y = y
        for i in range(x, x + self.size):
            self.screen.pixels[y][i] = '1'
    
    def removeSelf(self):
        for i in range(self.x, self.x + self.size):
            self.screen.pixels[self.y][i] = ' '

    def weaken(self):
        self.strength -= 1
        self.son = TransparentB()
        for i in range(self.size):
            self.screen.bricks[self.y][self.x + i] = self.son
        self.removeSelf()

class GreenB(Brick):
    def __init__(self, size, screen):
        super().__init__(size, screen, 2)

    def place(self, x, y):
        self.x = x
        self.y = y
        for i in range(x, x + self.size):
            self.screen.pixels[y][i] = '2'
    
    def weaken(self):
        self.strength -= 1
        self.son = RedB(self.size, self.screen)
        for i in range(self.size):
            self.screen.bricks[self.y][self.x + i] = self.son
        self.son.place(self.x, self.y)

class BlueB(Brick):
    def __init__(self, size, screen):
        super().__init__(size, screen, 3)

    def place(self, x, y):
        self.x = x
        self.y = y
        for i in range(x, x + self.size):
            self.screen.pixels[y][i] = '3'
    
    def weaken(self):
        self.strength -= 1
        self.son = GreenB(self.size, self.screen)
        for i in range(self.size):
            self.screen.bricks[self.y][self.x + i] = self.son
        self.son.place(self.x, self.y)