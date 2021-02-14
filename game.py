from colorama import init, Fore, Back, Style
from screen import Screen
from paddle import Paddle
from kbhit import KBHit
from ball import Ball
import os, numpy, sys, time, signal

screen = Screen(50, 30)
paddle = Paddle(9, screen)
ball = Ball(screen, paddle)
paddle.place()
ball.move()
screen.display()

def alarmHandler(signum, frame):
	raise AlarmException

class AlarmException(Exception):
	pass

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
