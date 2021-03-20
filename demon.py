from demonscii import demonDraw
import sys, random

class Bullet():
    def __init__(self, screen, paddle, ball):
        self.screen = screen
        self.paddle = paddle
        self.ball = ball
        self.y = 18
        self.prevY = self.y
        self.yVel = random.randint(3, 5)
        self.x = 0
        self.prevX = self.x
        self.life = True
        self.prevPixel = ' '
        self.prevPixel2 = ' '

    def place(self, x, y):
        if self.life == False:
            return
        self.screen.pixels[int(self.prevY)][int(self.prevX)] = self.prevPixel
        self.screen.pixels[y][x] = 'O'

    def collide(self):
        if self.x >= self.paddle.paddleX and self.x < self.paddle.paddleX + self.paddle.size and self.y >= self.screen.maxHeight:
            #do something to inform the paddle
            self.paddle.life -= 2
            return True
        if self.y > self.screen.maxHeight:
            self.life = False
            self.screen.pixels[int(self.prevY)][int(self.prevX)] = ' '
            return True
        return False

    def move(self):
        if self.life == False:
            return
        tempx = self.x
        tempy = self.y
        self.y += self.screen.interval * self.yVel
        if int(self.x) != int(tempx) or int(self.y) != int(tempy):
            self.prevX = int(tempx)
            self.prevY = int(tempy)
            self.prevPixel = self.prevPixel2
            self.prevPixel2 = self.screen.pixels[int(self.y)][int(self.x)]
        if self.y >= self.screen.maxWidth + 1:
            self.life = False
            self.screen.pixels[int(self.y)][int(self.x)] = ' '
        # if self.x >= self.screen.maxWidth or self.x <= 0:
        #     self.xVel *= -1
        if self.collide() == True:
            return
        self.place(int(self.x), int(self.y))


class Demon():
    def __init__(self, screen, paddle, ball):
        self.screen = screen
        self.paddle = paddle
        self.ball = ball
        self.sizeX = 65
        self.sizeY = 18
        self.screen.levelIsDemon = True
        self.x = (self.screen.maxWidth - 65) / 2
        self.y = 1
        self.life = 100
        self.bullets = []
    
    def place(self):
        a = []
        n = random.randint(0, 5)
        if n == 4:
            temp = Bullet(self.screen, self.paddle, self.ball)
            temp.x = random.randint(int(self.x), int(self.x) + 65)
            self.bullets.append(temp)
        self.x = max(self.paddle.paddleX - 25, 1)
        if self.x > self.screen.maxWidth - 65 + 1:
            self.x = self.screen.maxWidth - 65 + 1
        a = demonDraw()
        x = self.x
        y = self.y
        for i in self.bullets:
            i.move()
        for i in range(y, self.sizeY + y):
            for j in range(1, x):
                self.screen.pixels[i][j] = ' '
            for j in range(x + len(a[i - y]), self.screen.maxWidth + 1):
                self.screen.pixels[i][j] = ' '
            for j in range(x, x + len(a[i - y])):
                self.screen.pixels[i][j] = a[i - y][j - x]
    