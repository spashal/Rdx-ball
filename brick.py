import os
from powerup import powerUps, ExpandPU, ShrinkPU, FastPU, GrabPU, MultiplierPU

class Brick():
    def __init__(self, size, screen, strength, paddle, ball):
        self.paddle = paddle
        self.screen = screen
        self.size = size
        self.strength = strength
        self.ball = ball

class  TransparentB(Brick):
    def __init__(self):
        self.damn = "none given"
        self.strength = 0
    
class RedB(Brick):
    def __init__(self, size, screen, paddle, ball):
        super().__init__(size, screen, 1, paddle, ball)
    
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
        self.giftE = MultiplierPU(self.screen, self.paddle, self.x+1, self.y, self.ball)
        self.giftE.move()
        self.screen.powerUps.append(self.giftE)

class GreenB(Brick):
    def __init__(self, size, screen, paddle, ball):
        super().__init__(size, screen, 2, paddle, ball)

    def place(self, x, y):
        self.x = x
        self.y = y
        for i in range(x, x + self.size):
            self.screen.pixels[y][i] = '2'
    
    def weaken(self):
        self.strength -= 1
        self.son = RedB(self.size, self.screen, self.paddle, self.ball)
        for i in range(self.size):
            self.screen.bricks[self.y][self.x + i] = self.son
        self.son.place(self.x, self.y)

class BlueB(Brick):
    def __init__(self, size, screen, paddle, ball):
        super().__init__(size, screen, 3, paddle, ball)

    def place(self, x, y):
        self.x = x
        self.y = y
        for i in range(x, x + self.size):
            self.screen.pixels[y][i] = '3'
    
    def weaken(self):
        self.strength -= 1
        self.son = GreenB(self.size, self.screen, self.paddle, self.ball)
        for i in range(self.size):
            self.screen.bricks[self.y][self.x + i] = self.son
        self.son.place(self.x, self.y)

class UnbreakableB(Brick):
    def __init__(self, size, screen, paddle, ball):
        super().__init__(size, screen, 4, paddle, ball)
    
    def place(self, x, y):
        self.x = x
        self.y = y
        for i in range(x, x + self.size):
            self.screen.pixels[y][i] = '4'
    
    # a function that is there as a dummy
    def weaken(self):
        pass