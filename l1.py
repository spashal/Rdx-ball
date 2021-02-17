from brick import RedB, BlueB, UnbreakableB, GreenB
from screen import Screen
from paddle import Paddle
from ball import Ball
import sys, os


class Level1():
    def __init__(self):
        self.screen = Screen(10, 10)
        self.paddle = Paddle(5, self.screen)
        self.ball = Ball(self.screen, self.paddle, False)
        self.paddle.place(self.paddle.size)
        self.ball.move()

        self.rb = UnbreakableB(3, self.screen, self.paddle, self.ball)
        self.gb = GreenB(3, self.screen, self.paddle, self.ball)
        self.bb = RedB(3, self.screen, self.paddle, self.ball)
        self.rb.place(1, 2)
        self.gb.place(4, 2)
        self.bb.place(7, 2)
        for i in range(3):
            self.screen.bricks[2][i + 1] = self.rb
            self.screen.bricks[2][i + 4] = self.gb
            self.screen.bricks[2][i + 7] = self.bb
