import random, sys
from ball import Ball

class powerUps():
    def __init__(self, screen, paddle, parentX, parentY):
        self.size = 0
        self.screen = screen
        self.x = parentX
        self.y = parentY
        self.prevX = self.x
        self.prevY = self.y
        self.prevPixel = self.screen.pixels[parentY][parentX]
        self.paddle = paddle
        self.yVel = random.randint(3, 5)
        self.xVel = random.randint(3, 5)
        self.life = True
        self.prevPixel2 = ' '
    
    def setVel(self):
        self.xVel = self.ball.prevXVel
        self.yVel = self.ball.prevYVel

class ExpandPU(powerUps):
    def __init__(self, screen, paddle, parentX, parentY, ball):
        super().__init__(screen, paddle, parentX, parentY)
        self.ball = ball
    
    def place(self, x, y):
        if self.life == False:
            return
        self.screen.pixels[int(self.prevY)][int(self.prevX)] = self.prevPixel
        self.screen.pixels[y][x] = 'E'
    
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
        self.yVel += 10 * self.screen.interval
        tempx = self.x
        tempy = self.y
        self.y += self.screen.interval * self.yVel
        self.x += self.screen.interval * self.xVel
        if int(self.x) != int(tempx) or int(self.y) != int(tempy):
            self.prevX = int(tempx)
            self.prevY = int(tempy)
            self.prevPixel = self.prevPixel2
            self.prevPixel2 = self.screen.pixels[int(self.y)][int(self.x)]
 
        if self.x >= self.screen.maxWidth or self.x <= 0:
            self.xVel *= -1
        if self.collide() == True:
            return
        self.place(int(self.x), int(self.y))

class ShrinkPU(powerUps):
    def __init__(self, screen, paddle, parentX, parentY, ball):
        super().__init__(screen, paddle, parentX, parentY)
        self.ball = ball
    
    def place(self, x, y):
        if self.life == False:
            return
        self.screen.pixels[int(self.prevY)][int(self.prevX)] = self.prevPixel
        self.screen.pixels[y][x] = 'S'
    
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
        self.yVel += 10 * self.screen.interval
        tempx = self.x
        tempy = self.y
        self.y += self.screen.interval * self.yVel
        self.x += self.screen.interval * self.xVel
        if int(self.x) != int(tempx) or int(self.y) != int(tempy):
            self.prevX = int(tempx)
            self.prevY = int(tempy)
            self.prevPixel = self.prevPixel2
            self.prevPixel2 = self.screen.pixels[int(self.y)][int(self.x)]
 
        if self.x >= self.screen.maxWidth or self.x <= 0:
            self.xVel *= -1
        if self.collide() == True:
            return
        self.place(int(self.x), int(self.y))


class FastPU(powerUps):
    def __init__(self, screen, paddle, parentX, parentY, ball):
        super().__init__(screen, paddle, parentX, parentY)
        self.ball = ball
    
    def place(self, x, y):
        if self.life == False:
            return
        self.screen.pixels[int(self.prevY)][int(self.prevX)] = self.prevPixel
        self.screen.pixels[y][x] = 'F'
    
    def collide(self):
        if self.x >= self.paddle.paddleX and self.x < self.paddle.paddleX + self.paddle.size and self.y >= self.screen.maxHeight:
            #do something to inform the paddle
            if self.ball.isFast == False:
                self.ball.fast()
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
        self.yVel += 10 * self.screen.interval
        tempx = self.x
        tempy = self.y
        self.y += self.screen.interval * self.yVel
        self.x += self.screen.interval * self.xVel
        if int(self.x) != int(tempx) or int(self.y) != int(tempy):
            self.prevX = int(tempx)
            self.prevY = int(tempy)
            self.prevPixel = self.prevPixel2
            self.prevPixel2 = self.screen.pixels[int(self.y)][int(self.x)]
 
        if self.x >= self.screen.maxWidth or self.x <= 0:
            self.xVel *= -1
        if self.collide() == True:
            return
        self.place(int(self.x), int(self.y))
    
class GrabPU(powerUps):
    def __init__(self, screen, paddle, parentX, parentY, ball):
        super().__init__(screen, paddle, parentX, parentY)
        self.ball = ball
    
    def place(self, x, y):
        if self.life == False:
            return
        self.screen.pixels[int(self.prevY)][int(self.prevX)] = self.prevPixel
        self.screen.pixels[y][x] = 'G'
    
    def collide(self):
        if self.x >= self.paddle.paddleX and self.x < self.paddle.paddleX + self.paddle.size and self.y >= self.screen.maxHeight:
            #do something to inform the paddle
            if self.paddle.isGrabbing == False:
                self.life = False
                self.paddle.grab()
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
        self.yVel += 10 * self.screen.interval
        tempx = self.x
        tempy = self.y
        self.y += self.screen.interval * self.yVel
        self.x += self.screen.interval * self.xVel
        if int(self.x) != int(tempx) or int(self.y) != int(tempy):
            self.prevX = int(tempx)
            self.prevY = int(tempy)
            self.prevPixel = self.prevPixel2
            self.prevPixel2 = self.screen.pixels[int(self.y)][int(self.x)]
 
        if self.x >= self.screen.maxWidth or self.x <= 0:
            self.xVel *= -1
        if self.collide() == True:
            return
        self.place(int(self.x), int(self.y))

class MultiplierPU(powerUps):
    def __init__(self, screen, paddle, parentX, parentY, ball):
        super().__init__(screen, paddle, parentX, parentY)
        self.ball = ball
    
    def place(self, x, y):
        if self.life == False:
            return
        self.screen.pixels[int(self.prevY)][int(self.prevX)] = self.prevPixel
        self.screen.pixels[y][x] = 'M'
    
    def collide(self):
        
        if self.x >= self.paddle.paddleX and self.x < self.paddle.paddleX + self.paddle.size and self.y >= self.screen.maxHeight:
            #do something to inform the paddle
            self.life = False

            n = random.randint(2, 4)
            for i in range(n):
                temp = Ball(self.screen, self.paddle, True)
                temp.tempBall(self.ball.x, self.ball.y)
                self.ball.daughters.append(temp)
                self.screen.powerUps.append(temp)
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
        self.yVel += 10 * self.screen.interval
        tempx = self.x
        tempy = self.y
        self.y += self.screen.interval * self.yVel
        self.x += self.screen.interval * self.xVel
        if int(self.x) != int(tempx) or int(self.y) != int(tempy):
            self.prevX = int(tempx)
            self.prevY = int(tempy)
            self.prevPixel = self.prevPixel2
            self.prevPixel2 = self.screen.pixels[int(self.y)][int(self.x)]
 
        if self.x >= self.screen.maxWidth or self.x <= 0:
            self.xVel *= -1
        if self.collide() == True:
            return
        self.place(int(self.x), int(self.y))

class DummyPU(powerUps):
    def __init__(self, screen, paddle, parentX, parentY, ball):
        super().__init__(screen, paddle, parentX, parentY)
        self.ball = ball
    
    def move(self):
        pass

class ThruBallPU(powerUps):
    def __init__(self, screen, paddle, parentX, parentY, ball):
        super().__init__(screen, paddle, parentX, parentY)
        self.ball = ball
    
    def place(self, x, y):
        if self.life == False:
            return
        self.screen.pixels[int(self.prevY)][int(self.prevX)] = self.prevPixel
        self.screen.pixels[y][x] = 'T'
    
    def collide(self):
        if self.x >= self.paddle.paddleX and self.x < self.paddle.paddleX + self.paddle.size and self.y >= self.screen.maxHeight:
            #do something to inform the paddle
            if self.ball.thru == False:
                self.life = False
                self.ball.thruBall()
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
        self.yVel += 10 * self.screen.interval
        tempx = self.x
        tempy = self.y
        self.y += self.screen.interval * self.yVel
        self.x += self.screen.interval * self.xVel
        
        if int(self.x) != int(tempx) or int(self.y) != int(tempy):
            self.prevX = int(tempx)
            self.prevY = int(tempy)
            self.prevPixel = self.prevPixel2
            self.prevPixel2 = self.screen.pixels[int(self.y)][int(self.x)]
 
        if self.x >= self.screen.maxWidth or self.x <= 0:
            self.xVel *= -1
        if self.collide() == True:
            return
        self.place(int(self.x), int(self.y))

class FireBallPU(powerUps):
    def __init__(self, screen, paddle, parentX, parentY, ball):
        super().__init__(screen, paddle, parentX, parentY)
        self.ball = ball
    
    def place(self, x, y):
        if self.life == False:
            return
        self.screen.pixels[int(self.prevY)][int(self.prevX)] = self.prevPixel
        self.screen.pixels[y][x] = 'B'
    
    def collide(self):
        if self.x >= self.paddle.paddleX and self.x < self.paddle.paddleX + self.paddle.size and self.y >= self.screen.maxHeight:
            #do something to inform the paddle
            self.life = False
            self.ball.fireball()
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
        self.yVel += 10 * self.screen.interval
        tempx = self.x
        tempy = self.y
        self.y += self.screen.interval * self.yVel
        self.x += self.screen.interval * self.xVel
        if int(self.x) != int(tempx) or int(self.y) != int(tempy):
            self.prevX = int(tempx)
            self.prevY = int(tempy)
            self.prevPixel = self.prevPixel2
            self.prevPixel2 = self.screen.pixels[int(self.y)][int(self.x)]
 
        if self.x >= self.screen.maxWidth or self.x <= 0:
            self.xVel *= -1
        if self.collide() == True:
            return
        self.place(int(self.x), int(self.y))