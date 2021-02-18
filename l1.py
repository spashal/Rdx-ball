from brick import RedB, BlueB, UnbreakableB, GreenB, BomberB, ChainReactionB
from screen import Screen
from paddle import Paddle
from ball import Ball
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

class Evals():
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
            n = random.randint(0, 2)
            temp = RedB(3, self.screen, self.paddle, self.ball)
            if n == 1:
                temp = GreenB(3, self.screen, self.paddle, self.ball)
            elif n == 2:
                temp = BlueB(3, self.screen, self.paddle, self.ball)
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