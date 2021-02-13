import os

# paddle is the stick like structure at the bottom you hit your ball with
class Paddle():

    def __init__(self, size, screen):
        self.size = size
        self.screenHeight = screen.maxHeight
        self.screenWidth = screen.maxWidth
        self.paddleX = int((self.screenWidth - size) / 2)
        self.screen = screen

    def place(self):
        for i in range(1, self.screenWidth + 1):
            if i >= self.paddleX and i < self.paddleX + self.size:
                self.screen.pixels[self.screenHeight][i] = '@'
            else:
                self.screen.pixels[self.screenHeight][i] = ' '
    
    def move(self, input):
        if input == 'a' and self.paddleX > 1:
            self.paddleX -= 1
        elif input == 'd' and self.paddleX + self.size <= self.screenWidth:
            self.paddleX += 1
        self.place()
    
    # below function shall place the paddle into the appropriate string in pixels
        
        
