from brick import RedB, BlueB, UnbreakableB, GreenB, BomberB, ChainReactionB, RainbowB
from screen import Screen
from paddle import Paddle
from ball import Ball
from demon import Demon
import sys, os, random


class Level1():
    def __init__(self):
        self.screen = Screen(10, 10)
        self.paddle = Paddle(5, self.screen)
        self.ball = Ball(self.screen, self.paddle, False)
        self.paddle.place(self.paddle.size)
        self.ball.move()

        self.rb = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.gb = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.bb = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.kk = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.rb.place(1, 2)
        self.gb.place(4, 2)
        self.bb.place(7, 2)
        self.kk.place(5, 3)
        for i in range(3):
            self.screen.bricks[2][i + 1] = self.rb
            self.screen.bricks[2][i + 4] = self.gb
            self.screen.bricks[2][i + 7] = self.bb
            self.screen.bricks[3][i + 5] = self.kk

class Moderate():
    def __init__(self):
        self.screen = Screen(45, 20)
        self.paddle = Paddle(7, self.screen)
        self.ball = Ball(self.screen, self.paddle, False)
        self.paddle.place(self.paddle.size)
        self.ball.move()
    
    def putMark(self, brick, x, y):
        brick.place(x, y)
        for i in range(brick.size):
            self.screen.bricks[y][i + x] = brick

    def placeBricks(self):
        # the design of the this level
        for i in range(3):
            for j in range(3):
                if i + j < 3:
                    temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
                    self.putMark(temp, 4+i*3, 4 + j)
                if i >= j:
                    temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
                    self.putMark(temp, 34+i*3, 4 + j)
        for i in range(7):
            n = random.randint(0, 4)
            temp = RedB(3, self.screen, self.paddle, self.ball)
            if n == 1:
                temp = GreenB(3, self.screen, self.paddle, self.ball)
            elif n == 2:
                temp = BlueB(3, self.screen, self.paddle, self.ball)
            elif n == 3:
                temp = RainbowB(3, self.screen, self.paddle, self.ball)
            self.putMark(temp, 13 + i*3, 4)
        
        temp = BomberB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 22, 7)
        temp = BomberB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 19, 6)
        temp = BomberB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 19, 8)
        temp = BomberB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 25, 6)
        temp = BomberB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 25, 8)

        temp = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 22, 8)
        temp = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 19, 9)
        temp = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 16, 10)
        temp = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 13, 11)
        temp = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 25, 9)
        temp = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 28, 10)
        temp = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 31, 11)

        # for i in range(self.screen.maxHeight + 2):
        #     for j in range(self.screen.maxWidth + 2):
        #         print(self.screen.bricks[i][j].strength, end='')
        #     print()
        # sys.exit()

class Easy():
    def __init__(self):
        self.screen = Screen(45, 20)
        self.paddle = Paddle(7, self.screen)
        self.ball = Ball(self.screen, self.paddle, False)
        self.paddle.place(self.paddle.size)
        self.ball.move()
    
    def putMark(self, brick, x, y):
        brick.place(x, y)
        for i in range(brick.size):
            self.screen.bricks[y][i + x] = brick

    def placeBricks(self):
        # the design of the this level
        
        # top corners
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1, 1)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1 + 3, 1)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1 + 3 * 2, 1)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1 + 3 * 3, 1)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1, 2)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1 + 3, 2)    
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1 + 3 * 2, 2)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1, 3)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1 + 3, 3)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1, 4)

        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 33 + 1, 1)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 33 + 1 + 3, 1)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 33 + 1 + 3 * 2, 1)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 33 + 1 + 3 * 3, 1)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 33 + 1 + 3, 2)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 33 + 1 + 3 * 2, 2)    
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 33 + 1 + 3 * 3, 2)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 33 + 1 + 3 * 2, 3)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 33 + 1 + 3 * 3, 3)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 33 + 1 + 3 * 3, 4)

        # central thing
        for i in range(8, 3, -1):
            j = (11 - i) * 3 + 1
            n = random.randint(0, 5)
            temp = RedB(3, self.screen, self.paddle, self.ball)
            if n == 1:
                temp = GreenB(3, self.screen, self.paddle, self.ball)
            elif n == 2:
                temp = BlueB(3, self.screen, self.paddle, self.ball)
            elif n == 3:
                temp = BomberB(3, self.screen, self.paddle, self.ball)
            elif n == 4:
                temp = RainbowB(3, self.screen, self.paddle, self.ball)
            self.putMark(temp, j, i)
        
        for i in range(5, 9):
            j = (i + 3) * 3 + 1
            n = random.randint(0, 5)
            temp = RedB(3, self.screen, self.paddle, self.ball)
            if n == 1:
                temp = GreenB(3, self.screen, self.paddle, self.ball)
            elif n == 2:
                temp = BlueB(3, self.screen, self.paddle, self.ball)
            elif n == 3:
                temp = BomberB(3, self.screen, self.paddle, self.ball)
            elif n == 4:
                temp = RainbowB(3, self.screen, self.paddle, self.ball)
            self.putMark(temp, j, i)
        
        for i in range(12, 7, -1):
            j = (19 - i) * 3 + 1
            n = random.randint(0, 5)
            temp = RedB(3, self.screen, self.paddle, self.ball)
            if n == 1:
                temp = GreenB(3, self.screen, self.paddle, self.ball)
            elif n == 2:
                temp = BlueB(3, self.screen, self.paddle, self.ball)
            elif n == 3:
                temp = BomberB(3, self.screen, self.paddle, self.ball)
            elif n == 4:
                temp = RainbowB(3, self.screen, self.paddle, self.ball)
            self.putMark(temp, j, i)
        
        for i in range(9, 13):
            j = (i - 5) * 3 + 1
            n = random.randint(0, 5)
            temp = RedB(3, self.screen, self.paddle, self.ball)
            if n == 1:
                temp = GreenB(3, self.screen, self.paddle, self.ball)
            elif n == 2:
                temp = BlueB(3, self.screen, self.paddle, self.ball)
            elif n == 3:
                temp = BomberB(3, self.screen, self.paddle, self.ball)
            elif n == 4:
                temp = RainbowB(3, self.screen, self.paddle, self.ball)
            self.putMark(temp, j, i)
        
        temp = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 3 * 6 + 1, 7)
        temp = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 3 * 8 + 1, 7)
        temp = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 3 * 7 + 1, 8)
        temp = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 3 * 6 + 1, 10)
        temp = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 3 * 7 + 1, 10)
        temp = ChainReactionB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 3 * 8 + 1, 10)
    

class Difficult():
    def __init__(self):
        self.screen = Screen(45, 20)
        self.paddle = Paddle(7, self.screen)
        self.ball = Ball(self.screen, self.paddle, False)
        self.paddle.place(self.paddle.size)
        self.ball.move()
    
    def randBrick(self):
        n = random.randint(0, 5)
        temp = RedB(3, self.screen, self.paddle, self.ball)
        if n == 1:
            temp = GreenB(3, self.screen, self.paddle, self.ball)
        elif n == 2:
            temp = BlueB(3, self.screen, self.paddle, self.ball)
        elif n == 3:
            temp = BomberB(3, self.screen, self.paddle, self.ball)
        elif n == 4:
                temp = RainbowB(3, self.screen, self.paddle, self.ball)
        return temp

    def putMark(self, brick, x, y):
        brick.place(x, y)
        for i in range(brick.size):
            self.screen.bricks[y][i + x] = brick

    def placeBricks(self):
        # the design of the this level
        
        # top centre
        temp = self.randBrick()
        self.putMark(temp, 5 * 3 + 1, 1)
        temp = self.randBrick()
        self.putMark(temp, 1 + 3 * 7, 1)
        temp = self.randBrick()
        self.putMark(temp, 1 + 3 * 6, 1)
        temp = self.randBrick()
        self.putMark(temp, 1 + 3 * 9, 1)
        temp = self.randBrick()
        self.putMark(temp, 1 + 3 * 8, 1)
        temp = self.randBrick()
        self.putMark(temp, 7 * 3 + 1, 2)
        temp = self.randBrick()
        self.putMark(temp, 1 + 3 * 6, 2)
        temp = self.randBrick()
        self.putMark(temp, 1 + 3 * 8, 2)
        temp = self.randBrick()
        self.putMark(temp, 1 + 3 * 7, 3)

        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 3 * 6 + 1, 3)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1 + 3 * 8, 3)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1 + 3 * 7, 4)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1 + 3 * 8, 5)
        temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1 + 3 * 6, 5)

        # Middle portion
        for i in range(7, 12):
            j = (i - 4) * 3 + 1
            temp = self.randBrick()
            self.putMark(temp, j, i)
            temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
            self.putMark(temp, j, i + 3)
            
        for i in range(7, 12):
            j = (18 - i) * 3 + 1
            temp = self.randBrick()
            self.putMark(temp, j, i)
            temp = UnbreakableB(3, self.screen, self.paddle, self.ball)
            self.putMark(temp, j, i + 3)
        
        temp = BomberB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 2 * 3 + 1, 6)
        temp = BomberB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 2 * 3 + 1, 5)
        temp = BomberB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1 * 3 + 1, 6)
        temp = BomberB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 1 * 3 + 1, 5)

        temp = BomberB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 12 * 3 + 1, 5)
        temp = BomberB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 12 * 3 + 1, 6)
        temp = BomberB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 13 * 3 + 1, 6)
        temp = BomberB(3, self.screen, self.paddle, self.ball)
        self.putMark(temp, 13 * 3 + 1, 5)
    
class FinalLevel():
    def __init__(self):
        self.screen = Screen(100, 30)
        self.paddle = Paddle(15, self.screen)
        self.ball = Ball(self.screen, self.paddle, False)
        self.paddle.place(self.paddle.size)
        self.ball.move()
    
    def placeDemon(self):
        self.demon = Demon(self.screen, self.paddle, self.ball)
        self.screen.setDemon(self.demon, self.paddle)
        self.ball.demon(self.demon)
        self.demon.place()
