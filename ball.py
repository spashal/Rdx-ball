import os, sys, random

gameOver = False
class Ball():
    def __init__(self, screen, paddle, fake):
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
        self.isFast = False
        self.alive = True
    
    def brickollision(self):
        if self.yVel < 0 and self.screen.bricks[int(self.y - 1)][int(self.x)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y - 1)][int(self.x)].strength
            self.screen.bricks[int(self.y - 1)][int(self.x)].weaken()
            temp = self.y
            self.y = self.prevY
            self.prevY = temp
            self.yVel *= -1
            return True
        elif int(self.y) < self.screen.maxHeight and self.yVel > 0 and self.screen.bricks[int(self.y + 1)][int(self.x)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y - 1)][int(self.x)].strength
            self.screen.bricks[int(self.y + 1)][int(self.x)].weaken()
            temp = self.y
            self.y = self.prevY
            self.prevY = temp
            self.yVel *= -1
            return True
        elif self.xVel > 0 and self.screen.bricks[int(self.y)][int(self.x + 1)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y - 1)][int(self.x)].strength
            self.screen.bricks[int(self.y)][int(self.x + 1)].weaken()
            temp = self.x
            self.x = self.prevX
            self.prevX = temp
            self.xVel *= -1
            return True
        elif self.xVel < 0 and self.screen.bricks[int(self.y)][int(self.x - 1)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y - 1)][int(self.x)].strength
            self.screen.bricks[int(self.y)][int(self.x - 1)].weaken()
            temp = self.x
            self.x = self.prevX
            self.prevX = temp
            self.xVel *= -1
            return True
        return False    

    def move(self):
        if self.alive == False:
            return
        if self.isFast == True and self.fastTime + 10 < self.screen.time:
            self.isFast = False
            self.xVel = self.originalVelX
            self.yVel = self.originalVelY

        if self.brickollision() == True:
            self.place()
            return
        self.prevX = self.x
        self.prevY = self.y
        if self.launched == False:
            self.x = self.paddle.paddleX + (self.paddle.size) / 2
        else:
            self.x += self.waitTime * self.xVel
            self.y += self.waitTime * self.yVel
            if self.x < 1 or self.x > self.screen.maxWidth + 1 and self.y < self.screen.maxHeight:
                self.x = self.prevX
                self.xVel *= -1
            # colliding with the paddle
            elif self.y >= self.screen.maxHeight:
                if self.paddle.paddleX <= self.x and self.paddle.paddleX + self.paddle.size > self.x:
                    # if there is a paddle grab power up in action
                    if self.paddle.isGrabbing == True:
                        self.launched = False
                        self.x = self.paddle.paddleX + (self.paddle.size) / 2
                        self.y = self.screen.maxHeight - 1
                        self.place()
                        return
                    self.y = self.prevY
                    self.xVel += (self.paddle.paddleX + int(self.paddle.size/2)) - self.x
                    # self.xVel *= -1
                    self.yVel *= -1
                elif self.y >= (self.screen.maxHeight + 1):
                    if self.screen.balls > 1:
                        self.alive = False
                        return
                    self.gameOver = True
                    os.system("clear")
                    self.screen.display()
                    return
            elif self.y < 1:
                self.y = self.prevY
                self.yVel *= -1
        self.place()
    
    def place(self):
        self.screen.pixels[int(self.prevY)][int(self.prevX)] = ' '
        self.screen.pixels[int(self.y)][int(self.x)] = '@'

    def launch(self):
        self.screen.balls += 1
        self.launched = True
        self.xVel = random.randint(-5, 5)
        self.yVel = -4
        self.originalVelX = self.xVel
        self.originalVelY = self.yVel

    def fast(self):
        self.isFast = True
        self.xVel *= 1.5
        self.yVel *= 1.5
        self.fastTime = self.screen.time
        self.move()

    def tempBall(self, x, y):
        self.screen.balls += 1
        self.launched = True
        self.x = x
        self.y = y
        self.x = 1
        self.y = 1
        while self.x * self.y != 0:
            self.xVel = random.randint(-3, 3)
            self.yVel = random.randint(-3, 3)
        self.move()