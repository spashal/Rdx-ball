from colorama import init, Fore, Back, Style
from screen import Screen
from paddle import Paddle
from kbhit import KBHit
from brick import Brick, RedB, GreenB, TransparentB, BlueB
from ball import Ball
import os, numpy, sys, time


screen = Screen(10, 10)
paddle = Paddle(5, screen)
ball = Ball(screen, paddle)
paddle.place()
ball.move()

rb = RedB(3, screen)
gb = GreenB(3, screen)
bb = BlueB(3, screen)
rb.place(1, 2)
gb.place(4, 2)
bb.place(7, 2)
for i in range(3):
	screen.bricks[2][i + 1] = rb
	screen.bricks[2][i + 4] = gb
	screen.bricks[2][i + 7] = bb


keyboard = KBHit()

while True:
	# os.system("clear")

	time.sleep(ball.waitTime)
	if keyboard.kbhit():
		inp = keyboard.getch()
		if inp == 'q':
			sys.exit()
		elif inp == 'a' or inp == 'd':
			paddle.move(inp)
		elif inp == ' ':
			ball.launch()
		keyboard.flush()
	ball.move()
	
	if ball.gameOver == True:
		print("Game over!")
		break
	os.system("clear")
	screen.display()
