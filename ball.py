import os, sys, random

gameOver = False
class Ball():
    def __init__(self, screen, paddle, fake):
        self.screen = screen
        self.waitTime = 0.05
        self.gameOver = False
        self.paddle = paddle
        self.screen.balls += 1
        self.y = self.screen.maxHeight - 1
        self.x = (self.screen.maxWidth + 1) / 2
        self.xVel = 0   
        self.yVel = 0
        self.prevX = self.x
        self.prevY = self.y
        self.launched = False
        self.isFast = False
        self.alive = True
        self.thru = False
        self.thruTime = 0.00
        self.isColliding = False
        self.real = False
        self.daughters = []
        self.bricksFallAfter = 2
        self.lastTimeBricksFell = 0
        self.fireballTime = 0
        self.isFireball = False
        self.brickSize = 3
        self.worthReflecting = False
        self.prevXVel = 0
        self.prevYVel = 0
        self.thereIsADemon = False
    
    def brickollision(self):
        if self.thereIsADemon:
            if self.yVel < 0 and self.y <= self.demon.sizeY:
                self.yVel *= -1
                return True
            return False

        if self.yVel < 0 and self.screen.bricks[int(self.y - 1)][int(self.x)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y - 1)][int(self.x)].strength
            self.screen.bricks[int(self.y - 1)][int(self.x)].weaken()
            if self.isFireball:
                self.screen.bricks[int(self.y - 1)][int(self.x)].destroyed()  
            if self.thru != True:
                self.yVel *= -1
            else:
                os.system('afplay brickbreak.mp3 &')
            self.worthReflecting = True
        elif self.isFireball and self.yVel < 0 and self.x - self.brickSize >= 0 and self.screen.bricks[int(self.y - 1)][int(self.x - self.brickSize)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y - 1)][int(self.x - self.brickSize)].strength
            self.screen.bricks[int(self.y - 1)][int(self.x - self.brickSize)].destroyed()
            os.system('afplay explosion.mp3 &')

        elif self.isFireball and self.yVel < 0 and self.x + self.brickSize <= self.screen.maxWidth and self.screen.bricks[int(self.y - 1)][int(self.x + self.brickSize)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y - 1)][int(self.x + self.brickSize)].strength
            self.screen.bricks[int(self.y - 1)][int(self.x + self.brickSize)].destroyed()
            os.system('afplay explosion.mp3 &')

        elif self.y < self.screen.maxHeight and self.yVel > 0 and self.screen.bricks[int(self.y + 1)][int(self.x)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y + 1)][int(self.x)].strength
            self.screen.bricks[int(self.y + 1)][int(self.x)].weaken()
            if self.isFireball:
                self.screen.bricks[int(self.y + 1)][int(self.x)].destroyed()
            if self.thru != True:
                self.yVel *= -1
            else:
                os.system('afplay brickbreak.mp3 &')
            self.worthReflecting = True
        elif self.isFireball and self.yVel > 0 and self.x - self.brickSize >= 0 and self.screen.bricks[int(self.y + 1)][int(self.x - self.brickSize)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y + 1)][int(self.x - self.brickSize)].strength
            self.screen.bricks[int(self.y + 1)][int(self.x - self.brickSize)].destroyed()
            os.system('afplay explosion.mp3 &')
        elif self.isFireball and self.yVel < 0 and self.x + self.brickSize <= self.screen.maxWidth and self.screen.bricks[int(self.y + 1)][int(self.x + self.brickSize)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y + 1)][int(self.x + self.brickSize)].strength
            self.screen.bricks[int(self.y + 1)][int(self.x + self.brickSize)].destroyed()
            os.system('afplay explosion.mp3 &')

        elif self.xVel > 0 and self.screen.bricks[int(self.y)][int(self.x + 1)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y)][int(self.x + 1)].strength
            self.screen.bricks[int(self.y)][int(self.x + 1)].weaken()
            if self.isFireball:
                self.screen.bricks[int(self.y)][int(self.x + 1)].destroyed()
            if self.thru != True:
                self.xVel *= -1
            else:
                os.system('afplay brickbreak.mp3 &')
            self.worthReflecting = True
        elif self.isFireball and self.xVel > 0 and self.y - self.brickSize >= 0 and self.screen.bricks[int(self.y - self.brickSize)][int(self.x + 1)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y - self.brickSize)][int(self.x + 1)].strength
            self.screen.bricks[int(self.y - self.brickSize)][int(self.x + 1)].destroyed()
            os.system('afplay explosion.mp3 &')
        elif self.isFireball and self.xVel > 0 and self.y + self.brickSize <= self.screen.maxHeight and self.screen.bricks[int(self.y + self.brickSize)][int(self.x + 1)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y + self.brickSize)][int(self.x + 1)].strength
            self.screen.bricks[int(self.y + self.brickSize)][int(self.x + 1)].destroyed()    
            os.system('afplay explosion.mp3 &')

        elif self.xVel < 0 and self.screen.bricks[int(self.y)][int(self.x - 1)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y)][int(self.x-1)].strength
            self.screen.bricks[int(self.y)][int(self.x - 1)].weaken()
            if self.isFireball:
                self.screen.bricks[int(self.y)][int(self.x - 1)].destroyed()
            if self.thru != True:
                self.xVel *= -1
            else:
                os.system('afplay brickbreak.mp3 &')
            self.worthReflecting = True
        elif self.isFireball and self.xVel < 0 and self.y - self.brickSize >= 0 and self.screen.bricks[int(self.y - self.brickSize)][int(self.x - 1)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y - self.brickSize)][int(self.x - 1)].strength
            self.screen.bricks[int(self.y - self.brickSize)][int(self.x - 1)].destroyed()
            os.system('afplay explosion.mp3 &')
        elif self.isFireball and self.xVel < 0 and self.y + self.brickSize <= self.screen.maxHeight and self.screen.bricks[int(self.y + self.brickSize)][int(self.x - 1)].strength > 0:
            self.screen.score += self.screen.bricks[int(self.y + self.brickSize)][int(self.x - 1)].strength
            self.screen.bricks[int(self.y + self.brickSize)][int(self.x - 1)].destroyed()
            os.system('afplay explosion.mp3 &')
        else:
            return False    
        if self.worthReflecting:
            self.worthReflecting = False
            return True
        return False
    
    def demon(self, demon):
        self.demon = demon
        self.thereIsADemon = True

    def move(self):
        if self.thru == True and self.thruTime + 10 < self.screen.time:
            self.thru = False
            self.thruTime = 0
        if self.alive == False:
            return

        if self.isFireball and self.fireballTime + 10 < self.screen.time:
            self.isFireball = False

        if self.isFast == True and self.fastTime + self.screen.powerUpTime < self.screen.time:
            self.isFast = False
            self.xVel = self.originalVelX
            self.yVel = self.originalVelY
        self.prevXVel = self.xVel
        self.prevYVel = self.yVel
        if self.thru == True and self.isColliding == False:
            if self.brickollision() == True:
                self.isColliding = True
        elif self.thru == True and self.isColliding == True:
            if self.brickollision() == False:
                self.isColliding = False
        elif self.thru == False and self.brickollision() == True:
            if self.isFireball == False:
                os.system('afplay brickbreak.mp3 &')
            else:
                os.system('afplay explosion.mp3 &')
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
                os.system('afplay bounce.mp3 &')
            # colliding with the paddle
            elif self.y >= self.screen.maxHeight:
                if self.paddle.paddleX <= self.x and self.paddle.paddleX + self.paddle.size > self.x:
                    # if there is a paddle grab power up in action
                    if self.paddle.isGrabbing == True:
                        self.launched = False
                        self.x = self.paddle.paddleX + (self.paddle.size) / 2
                        self.y = self.screen.maxHeight - 1
                        self.place()
                        os.system('afplay bounce.mp3 &')
                        return
                    if self.bricksFallAfter + self.lastTimeBricksFell <= self.screen.time:
                        self.fallingBricks()
                        self.lastTimeBricksFell = self.screen.time
                    self.y = self.prevY
                    self.xVel += (self.paddle.paddleX + int(self.paddle.size/2)) - self.x
                    self.yVel *= -1
                    os.system('afplay bounce.mp3 &')
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
                os.system('afplay bounce.mp3 &')
        self.place()
    
    def place(self):
        self.screen.pixels[int(self.prevY)][int(self.prevX)] = ' '
        self.screen.pixels[int(self.y)][int(self.x)] = '@'
        if self.isFireball :
            self.screen.pixels[int(self.y)][int(self.x)] = '^'

    def launch(self):
        self.launched = True
        self.real = True
        self.xVel = random.randint(-10, 10)
        self.yVel = -10
        self.originalVelX = self.xVel
        self.originalVelY = self.yVel

    def fast(self):
        self.isFast = True
        self.xVel *= 1.5
        self.yVel *= 1.5
        self.fastTime = self.screen.time
        for i in range(len(self.daughters)):
            self.daughters[i].fast()
        self.move()

    def tempBall(self, x, y):
        self.launched = True
        self.x = x
        self.y = y
        self.xVel = 0
        self.yVel = 0
        while self.xVel * self.yVel == 0:
            self.xVel = random.randint(-10, 10)
            self.yVel = random.randint(-10, 10)
        self.move()
    
    def thruBall(self):
        self.thru = True
        self.thruTime = self.screen.time
        for i in range(len(self.daughters)):
            self.daughters[i].thruBall()

    def fallingBricks(self):
        # for i in range(self.screen.maxHeight + 2):
        #     print(i, end=' ')
        #     for j in range(self.screen.maxWidth + 2):
        #         print(self.screen.pixels[i][j], end = '')
        #     print(' ')
        
        for j in range(self.screen.maxWidth + 1):
            if self.screen.bricks[self.screen.maxHeight - 1][j].strength > 0:
                print("Game Over!!! :/")
                sys.exit()

        for i in range(self.screen.maxHeight - 2, -1, -1):
            still_brick = -1
            for j in range(self.screen.maxWidth + 1):
                self.screen.bricks[i + 1][j] = self.screen.bricks[i][j]
                if self.screen.bricks[i][j].strength > 0 :
                    if still_brick > j:
                        continue
                    else:
                        still_brick = self.screen.bricks[i][j].x + self.screen.bricks[i][j].size
                        self.screen.bricks[i][j].place(j, i + 1)
                        for k in range(3):
                            self.screen.pixels[i][j + k] = ' '
            
        # for j in range(self.screen.maxWidth + 1):
        #     self.screen.bricks[0][j] = TransparentB()
        
        for i in self.screen.powerUps:
            if i.y == i.prevY and i.life :
                i.y += 1
                i.prevY += 1

        # for i in range(self.screen.maxHeight + 2):
        #     print(i, end=' ')
        #     for j in range(self.screen.maxWidth + 2):
        #         print(self.screen.pixels[i][j], end = '')
        #     print(' ')

    def fireball(self):
        self.isFireball = True
        self.fireballTime = self.screen.time                    
