from colorama import init, Fore, Back, Style
from paddle import Paddle
from kbhit import KBHit
from brick import Brick, RedB, GreenB, TransparentB, BlueB, UnbreakableB
import os, numpy, sys, time
from l1 import Level1, Evals
# os.system('afplay ' + 'barbie.mp3 &')


keyboard = KBHit()
lives = 5
score = 0
while lives > 0:
	level = Evals()
	level.placeBricks()
	while True:
		level.screen.time += level.ball.waitTime
		time.sleep(level.ball.waitTime)
		if keyboard.kbhit():
			inp = keyboard.getch()
			if inp == 'q':
				sys.exit()
			elif inp == 'a' or inp == 'd':
				level.paddle.move(inp)
			elif inp == ' ':
				level.ball.launch()
			keyboard.flush()
		level.ball.move()
		
		if level.ball.gameOver == True:
			break
		os.system("clear")
		level.screen.display()
		print("Score:", level.screen.score + score, "  ", "Time elapsed:", int(level.screen.time))
		print("Lives left:", lives - 1)
	lives -= 1
	score += level.screen.score

print("Game over!")
os.system('afplay gameoverclaps.mp3 &')
