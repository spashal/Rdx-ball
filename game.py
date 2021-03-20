from colorama import init, Fore, Back, Style
from paddle import Paddle
from kbhit import KBHit
from brick import Brick, RedB, GreenB, TransparentB, BlueB, UnbreakableB
import os, numpy, sys, time
from levels import Level1, Moderate, Easy, Difficult, FinalLevel
# os.system('afplay ' + 'barbie.mp3 &')


keyboard = KBHit()
lives = 5
score = 0
while lives > 0:

	# level 1
	level = Easy()
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
			elif inp == 't':
				break
			keyboard.flush()
		level.ball.move()
		
		if level.ball.gameOver == True:
			break
		os.system("clear")
		level.screen.display()
		print("Level 1")
		print("Score:", level.screen.score + score, "  ", "Time elapsed:", int(level.screen.time))
		print("Lives left:", lives - 1)
	score += level.screen.score

	# level 2
	level = Moderate()
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
			elif inp == 't':
				break
			keyboard.flush()
		level.ball.move()
		
		if level.ball.gameOver == True:
			break
		os.system("clear")
		level.screen.display()
		print("Level 2")
		print("Score:", level.screen.score + score, "  ", "Time elapsed:", int(level.screen.time))
		print("Lives left:", lives - 1)
	score += level.screen.score

	# level 3
	level = Difficult()
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
			elif inp == 't':
				break
			keyboard.flush()
		level.ball.move()
		
		if level.ball.gameOver == True:
			break
		os.system("clear")
		level.screen.display()
		print("Level 3")
		print("Score:", level.screen.score + score, "  ", "Time elapsed:", int(level.screen.time))
		print("Lives left:", lives - 1)
	score += level.screen.score

	# Last level of this life
	level = FinalLevel()
	level.placeDemon()
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
			elif inp == 't':
				break
			keyboard.flush()
		level.ball.move()
		
		if level.ball.gameOver == True:
			break
		os.system("clear")
		level.screen.display()
		print("Level 4")
		print("Score:", level.screen.score + score, "  ", "Time elapsed:", int(level.screen.time))
		print("Lives left:", lives - 1)
	lives -= 1
	score += level.screen.score

print("Game over!")
os.system('afplay gameoverclaps.mp3 &')
