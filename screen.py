from colorama import init, Fore, Back, Style
from paddle import Paddle
from brick import Brick, RedB, BlueB, GreenB, TransparentB
import os
init()
# this class lays out the screen where the game will run
class Screen():
    def __init__(self, screenWidth, screenHeight):
        self.maxWidth = screenWidth
        self.maxHeight = screenHeight
        self.score = 0
        self.time = 0.00
        self.powerUps = []
        self.balls = 0
        self.powerUpTime = 10
        self.levelIsDemon = False
        # remember to change this with change in interval in ball.py
        self.interval = 0.05

        # making borders
        pixels = [[' ' for j in range(screenWidth + 2)] for i in range(screenHeight + 2)]
        pixels[0] = ['='] * (screenWidth + 2)
        pixels[screenHeight + 1] = ['='] * (screenWidth + 2)
        for i in range(1, screenHeight + 1):
            pixels[i][0] = '|'
            pixels[i][screenWidth + 1] = '|'
        self.pixels = pixels

        # tracking the bricks
        self.bricks = ([[] for i in range(self.maxHeight + 4)])
        # print(len(self.bricks[0]))
        for i in range(self.maxHeight + 4):
            for j in range(self.maxWidth + 4):
                temp = TransparentB()
                self.bricks[i].append(temp)
        
    def setDemon(self, demon, paddle):
        self.demon = demon
        self.paddle = paddle

    def display(self):
        if self.levelIsDemon:
            self.demon.place()
            for i in range(self.maxHeight + 2):
                for j in range(self.maxWidth + 2):
                    print(self.pixels[i][j], end='')
                print(' ')
            print("Demon's Health: ", end='')
            for i in range(int(self.demon.life / 10)):
                print(Back.RED, ' ', end='')
            print(Back.RESET)
            print("Paddle Health: ", end='')
            for i in range(int(self.paddle.life / 10)):
                print(Back.BLUE, ' ', end='')
            print(Back.RESET)
            return


        for i in range(self.maxHeight + 2):
            for j in range(self.maxWidth + 2):
                if self.bricks[i][j].strength > 0:
                    self.bricks[i][j].place(self.bricks[i][j].x, self.bricks[i][j].y)
        for i in range(len(self.powerUps)):
            self.powerUps[i].move()
        for i in range(self.maxHeight + 2):
            for j in range(self.maxWidth + 2):
                if self.pixels[i][j] == '|':
                    print(Back.BLUE, " ", end = '')
                elif self.pixels[i][j] == '=':
                    print(Back.BLUE, ' ', end = '')
                elif self.pixels[i][j] == ' ':
                    print(Back.RESET, self.pixels[i][j], end = '')
                elif self.pixels[i][j] == '*':
                    print(Back.YELLOW, " ", end = '')
                elif self.pixels[i][j] == '&':
                    print(Back.LIGHTYELLOW_EX, " ", end='')
                elif self.pixels[i][j] == "@":
                    print(Back.RESET, "@", end='')
                elif self.pixels[i][j] == '^':
                    print(Fore.RED, '@', end='')
                elif self.pixels[i][j] == 'T' or self.pixels[i][j] == 'E' or self.pixels[i][j] == 'S' or self.pixels[i][j] == 'F' or self.pixels[i][j] == 'M' or self.pixels[i][j] == 'G' or self.pixels[i][j] == 'B':
                    print(Back.LIGHTBLUE_EX, self.pixels[i][j], end = '')
                elif self.bricks[i][j].strength == 0:
                    print(Back.RESET, ' ', end='')
                elif self.pixels[i][j] == '6':
                    print(Back.LIGHTYELLOW_EX, ' ', end='')
                elif self.pixels[i][j] == '5':
                    print(Back.LIGHTRED_EX, ' ', end='')
                elif self.pixels[i][j] == '4':
                    print(Back.CYAN, ' ', end='')
                elif self.pixels[i][j] == '3':
                    print(Back.MAGENTA, ' ', end = '')
                elif self.pixels[i][j] == '2':
                    print(Back.GREEN, ' ', end = '')
                elif self.pixels[i][j] == '1':
                    print(Back.RED, ' ', end = '')    
                
            print(Back.RESET, Fore.RESET)
    
