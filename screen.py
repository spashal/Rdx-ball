from colorama import init
from paddle import Paddle
import os

# this class lays out the screen where the game will run
class Screen():
    def __init__(self, screenWidth, screenHeight):
        self.maxWidth = screenWidth
        self.maxHeight = screenHeight

        # making borders
        pixels = [[' ' for j in range(screenWidth + 2)] for i in range(screenHeight + 2)]
        pixels[0] = ['='] * (screenWidth + 2)
        pixels[screenHeight + 1] = ['='] * (screenWidth + 2)
        for i in range(1, screenHeight + 1):
            pixels[i][0] = '|'
            pixels[i][screenWidth + 1] = '|'
        self.pixels = pixels


    def display(self):
        for i in range(self.maxHeight + 2):
            listToString = ' '.join([str(elem) for elem in self.pixels[i]])
            print(listToString)
    
