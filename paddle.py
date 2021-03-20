import os, sys

# paddle is the stick like structure at the bottom you hit your ball with
class Paddle():

    def __init__(self, size, screen):
        self.size = size
        self.screenHeight = screen.maxHeight
        self.screenWidth = screen.maxWidth
        self.paddleX = int((self.screenWidth - size + 1) / 2)
        self.screen = screen
        self.isExpanded = False
        self.originalSize = size
        self.expandedTime = 0.00
        self.shrunkTime = 0
        self.grabTime = 0
        self.isShrunk = False
        self.isGrabbing = False
        self.life = 100

    def place(self, size):
        for i in range(1, self.screenWidth + 1):
            if i >= self.paddleX and i < self.paddleX + size:
                if i != self.paddleX + int(self.size/2):
                    self.screen.pixels[self.screenHeight][i] = '*'
                else:
                    self.screen.pixels[self.screenHeight][i] = '&'
            else:
                self.screen.pixels[self.screenHeight][i] = ' '
    
    def move(self, input):

        if self.isGrabbing == True:
            if self.grabTime + self.screen.powerUpTime < self.screen.time:
                self.grabTime = 0
                self.isGrabbing = False

        if self.isExpanded == True:
            if self.expandedTime + 100 < self.screen.time:
                self.expandedTime = 0
                self.size = self.originalSize
                self.isExpanded = False
        
        if self.isShrunk == True and self.shrunkTime + self.screen.powerUpTime < self.screen.time:
            self.shrunkTime = 0
            self.size = self.originalSize
            self.isShrunk = False
            
        if input == 'a' and self.paddleX > 1:
            self.paddleX -= 1
        elif input == 'd' and self.paddleX + self.size <= self.screenWidth:
            self.paddleX += 1
        self.place(self.size)

    def expand(self):
        self.isExpanded = True
        self.size = int(self.size * 1.5)
        self.expandedTime = self.screen.time
        self.move('c')
    
    def shrink(self):
        self.isShrunk = True
        self.size = int(self.size * 0.66)
        self.shrunkTime = self.screen.time
        self.move('c')
    
    def grab(self):
        self.isGrabbing = True
        self.grabTime = self.screen.time
        self.move('c')
