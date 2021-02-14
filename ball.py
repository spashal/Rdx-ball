import os
gameOver = False
class Ball():
    def __init__(self, screen, paddle):
        self.screen = screen
        self.waitTime = 0.05
        self.gameOver = False
        self.paddle = paddle
        self.y = self.screen.maxHeight - 1
        self.x = (self.screen.maxWidth + 1) / 2
        self.xVel = 0   
        self.yVel = 0
        self.prevX = self.x
        self.prevY = self.y
        self.launched = False

    def move(self):
        self.prevX = self.x
        self.prevY = self.y
        if self.launched == False:
            self.x = self.paddle.paddleX + (self.paddle.size) / 2
        else:
            print("1")
            self.x += self.waitTime * self.xVel
            self.y += self.waitTime * self.yVel
            if self.x < 1 or self.x > self.screen.maxWidth + 1:
                self.x = self.prevX
                self.xVel *= -1
            elif self.y > self.screen.maxHeight:
                if self.paddle.paddleX > self.x or self.paddle.paddleX + self.paddle.size < self.x:
                    self.gameOver = True
                    return
                else:
                    self.y = self.prevY
                    self.yVel *= -1
            elif self.y < 1:
                self.y = self.prevY
                self.yVel *= -1
        self.place()
    
    def place(self):
        self.screen.pixels[int(self.prevY)][int(self.prevX)] = ' '
        self.screen.pixels[int(self.y)][int(self.x)] = '@'

    def launch(self):
        self.launched = True
        self.xVel = (self.x - (self.paddle.paddleX + self.paddle.size) / 2) * 6
        self.yVel = -5