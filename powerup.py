import random

class powerUps():
    def __init__(self, screen, paddle, parentX, parentY):
        self.size = 0
        self.screen = screen
        self.x = parentX
        self.y = parentY
        self.prevX = self.x
        self.prevY = self.y
        self.prevPixel = ' '
        self.paddle = paddle
        self.vel = random.randint(3, 5)
        self.life = True

class ExpandPU(powerUps):
    def __init__(self, screen, paddle, parentX, parentY):
        super().__init__(screen, paddle, parentX, parentY)
    
    def place(self, x, y):
        if self.life == False:
            return
        self.prevPixel = self.screen.pixels[y][x]
        self.screen.pixels[y][x] = 'E'
        self.screen.pixels[int(self.prevY)][int(self.prevX)] = self.prevPixel
    
    def collide(self):
        if self.x >= self.paddle.paddleX and self.x < self.paddle.paddleX + self.paddle.size and self.y >= self.screen.maxHeight:
            #do something to inform the paddle
            if self.paddle.isExpanded == False:
                self.paddle.expand()
                self.life = False
                self.screen.pixels[int(self.prevY)][int(self.prevX)] = ' '
            else:
                self.life = False
                self.screen.pixels[int(self.prevY)][int(self.prevX)] = ' '
            return True
        elif self.y > self.screen.maxHeight:
            self.life = False
            self.screen.pixels[int(self.prevY)][int(self.prevX)] = ' '
        return False

    def move(self):
        if self.life == False:
            return
        self.prevY = self.y
        self.y += self.screen.interval * self.vel
        if self.collide() == True:
            return
        self.place(int(self.x), int(self.y))

class ShrinkPU(powerUps):
    def __init__(self, screen, paddle, parentX, parentY):
        super().__init__(screen, paddle, parentX, parentY)
    
    def place(self, x, y):
        if self.life == False:
            return
        self.prevPixel = self.screen.pixels[y][x]
        self.screen.pixels[y][x] = 'S'
        self.screen.pixels[int(self.prevY)][int(self.prevX)] = self.prevPixel
    
    def collide(self):
        if self.x >= self.paddle.paddleX and self.x < self.paddle.paddleX + self.paddle.size and self.y >= self.screen.maxHeight:
            #do something to inform the paddle
            if self.paddle.isShrunk == False:
                self.paddle.shrink()
                self.life = False
                self.screen.pixels[int(self.prevY)][int(self.prevX)] = ' '
            else:
                self.life = False
                self.screen.pixels[int(self.prevY)][int(self.prevX)] = ' '
            return True
        if self.y > self.screen.maxHeight:
            self.life = False
            self.screen.pixels[int(self.prevY)][int(self.prevX)] = ' '
            return True
        return False

    def move(self):
        if self.life == False:
            return
        self.prevY = self.y
        self.y += self.screen.interval * self.vel
        if self.collide() == True:
            return
        self.place(int(self.x), int(self.y))