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
        self.time = 0

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
        
        


    def display(self):
        for i in range(self.maxHeight + 2):
            for j in range(self.maxWidth + 2):
                if self.pixels[i][j] == '|':
                    print(Back.BLUE, " ", end = '')
                elif self.pixels[i][j] == '=':
                    print(Back.BLUE, ' ', end = '')
                elif self.pixels[i][j] == '4':
                    print(Back.CYAN, ' ', end='')
                elif self.pixels[i][j] == '3':
                    print(Back.MAGENTA, ' ', end = '')
                elif self.pixels[i][j] == '2':
                    print(Back.GREEN, ' ', end = '')
                elif self.pixels[i][j] == '1':
                    print(Back.RED, ' ', end = '')    
                elif self.pixels[i][j] == ' ':
                    print(Back.RESET, self.pixels[i][j], end = '')
                elif self.pixels[i][j] == '*':
                    print(Back.YELLOW, " ", end = '')
                else:
                    print(Back.RESET, self.pixels[i][j], end = '')
            print(Back.RESET)
        print("Score:", self.score, "  ", "Time elapsed:", int(self.time))
    
