import os, random, sys
from powerup import powerUps, ExpandPU, ShrinkPU, FastPU, GrabPU, MultiplierPU, DummyPU, ThruBallPU, FireBallPU

class Brick():
    def __init__(self, size, screen, strength, paddle, ball):
        self.paddle = paddle
        self.screen = screen
        self.size = size
        self.strength = strength
        self.ball = ball
        self.ar = [-1, 0, 1]
        self.x = 0
        self.y = 0
    
    def assignPowerUps(self):
        num = random.randint(0, 6)
        temp = DummyPU(self.screen, self.paddle, self.x, self.y, self.ball)
        if num == 0:
            temp = ExpandPU(self.screen, self.paddle, self.x + 1, self.y, ball)
        elif num == 1:
            temp = ShrinkPU(self.screen, self.paddle, self.x + 1, self.y, ball)
        elif num == 2:
            temp = FastPU(self.screen, self.paddle, self.x + 1, self.y, self.ball)
        elif num == 3:
            temp = GrabPU(self.screen, self.paddle, self.x + 1, self.y, self.ball)
        elif num == 4:
            temp = MultiplierPU(self.screen, self.paddle, self.x + 1, self.y, self.ball)
        elif num == 5:
            temp = ThruBallPU(self.screen, self.paddle, self.x + 1, self.y, self.ball)
        elif num == 6:
            temp = FireBallPU(self.screen, self.paddle, self.x + 1, self.y, self.ball)
        return temp


class  TransparentB(Brick):
    def __init__(self):
        self.damn = "none given"
        self.strength = 0
    
    def destroyed(self):
        pass
 
    
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
        self.giftE = self.assignPowerUps()
        self.giftE.setVel()
        self.giftE.move()
        self.screen.powerUps.append(self.giftE)
    
    def destroyed(self):
        self.strength = 0
        self.son = TransparentB()
        for i in range(self.size):
            self.screen.bricks[self.y][self.x + i] = self.son
        self.removeSelf()


class GreenB(Brick):
    def __init__(self, size, screen, paddle, ball):
        super().__init__(size, screen, 2, paddle, ball)

    def place(self, x, y):
        self.x = x
        self.y = y
        for i in range(x, x + self.size):
            self.screen.pixels[y][i] = '2'
    
    def removeSelf(self):
        for i in range(self.x, self.x + self.size):
            self.screen.pixels[self.y][i] = ' '
    
    def weaken(self):
        self.strength -= 1
        self.son = RedB(self.size, self.screen, self.paddle, self.ball)
        for i in range(self.size):
            self.screen.bricks[self.y][self.x + i] = self.son
        self.son.place(self.x, self.y)
        self.giftE = self.assignPowerUps()
        self.giftE.setVel()
        self.giftE.move()
        self.screen.powerUps.append(self.giftE)

    def destroyed(self):
        self.strength = 0
        self.son = TransparentB()
        for i in range(self.size):
            self.screen.bricks[self.y][self.x + i] = self.son
        self.removeSelf()


class BlueB(Brick):
    def __init__(self, size, screen, paddle, ball):
        super().__init__(size, screen, 3, paddle, ball)

    def place(self, x, y):
        self.x = x
        self.y = y
        for i in range(x, x + self.size):
            self.screen.pixels[y][i] = '3'
    
    def removeSelf(self):
        for i in range(self.x, self.x + self.size):
            self.screen.pixels[self.y][i] = ' '
    
    def weaken(self):
        self.strength -= 1
        self.son = GreenB(self.size, self.screen, self.paddle, self.ball)
        for i in range(self.size):
            self.screen.bricks[self.y][self.x + i] = self.son
        self.son.place(self.x, self.y)
        self.giftE = self.assignPowerUps()
        self.giftE.setVel()
        self.giftE.move()
        self.screen.powerUps.append(self.giftE)      

    def destroyed(self):
        self.strength = 0
        self.son = TransparentB()
        for i in range(self.size):
            self.screen.bricks[self.y][self.x + i] = self.son
        self.removeSelf()  


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
    
    def destroyed(self):
        pass


class BomberB(Brick):
    def __init__(self, size, screen, paddle, ball):
        super().__init__(size, screen, 5, paddle, ball)
    
    def place(self, x, y):
        self.x = x
        self.y = y
        for i in range(self.size):
            self.screen.pixels[self.y][self.x + i] = '5'
    
    def blast(self):
        for k in range(self.size):
           for i in range(3):
                for j in range(3):
                    if self.x + k + self.ar[i] > 0 and self.x + k + self.ar[i] < self.screen.maxWidth and self.y + self.ar[j] > 0 and self.ar[j] + self.y < self.screen.maxHeight:
                        if self.screen.bricks[self.y + self.ar[j]][self.x + self.ar[i] + k].strength != 4:
                            self.screen.score += self.screen.bricks[self.y + self.ar[j]][self.x + self.ar[i] + k].strength
                            if self.screen.bricks[self.y + self.ar[j]][self.x + self.ar[i] + k].strength == 5:
                                self.screen.bricks[self.y + self.ar[j]][self.x + self.ar[i] + k].strength = 0
                                self.screen.bricks[self.y + self.ar[j]][self.x + self.ar[i] + k].destroyed() 
                            self.screen.bricks[self.y + self.ar[j]][self.x + self.ar[i] + k].strength = 0
        
    def weaken(self):
        self.blast()
        os.system('afplay explosion.mp3 &')
    
    def destroyed(self):
        self.strength = 0
        self.weaken()
        self.son = TransparentB()
        for i in range(self.size):
            self.screen.bricks[self.y][self.x + i] = self.son


class ChainReactionB(Brick):
    def __init__(self, size, screen, paddle, ball):
        super().__init__(size, screen, 6, paddle, ball)
    
    def place(self, x, y):
        self.x = x
        self.y = y
        for i in range(self.size):
            self.screen.pixels[self.y][self.x + i] = '6'
    

    def blast(self):
        self.strength = 0
        for k in range(self.size):
            for i in range(3):
                for j in range(3):
                    if (self.x + k + self.ar[i]) > 0 and (self.x + k + self.ar[i]) < self.screen.maxWidth and (self.y + self.ar[j]) > 0 and (self.ar[j] + self.y) < self.screen.maxHeight:
                        if self.screen.bricks[self.y + self.ar[j]][self.x + self.ar[i] + k].strength == 6:
                            self.screen.score += self.screen.bricks[self.y + self.ar[j]][self.x + self.ar[i] + k].strength
                            self.screen.bricks[self.y + self.ar[j]][self.x + self.ar[i] + k].blast()
    
    def weaken(self):
        self.blast()
        os.system('afplay explosion.mp3 &')

    def destroyed(self):
        self.strength = 0
        self.weaken()
        self.son = TransparentB()
        for i in range(self.size):
            self.screen.bricks[self.y][self.x + i] = self.son
    