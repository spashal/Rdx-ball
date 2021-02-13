from colorama import init, Fore, Back, Style
from screen import Screen
from paddle import Paddle
import os, numpy, sys, time

try:
	import tty, termios
except ImportError:
	try:
		import msvcrt
	except ImportError:
		raise ImportError('getch not available')
	else:
		getch = msvcrt.getch
else:
	def getch():
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch


screen = Screen(10, 10)
paddle = Paddle(5, screen)
screen.display()


while True:
	# os.system("clear")
	time.sleep(0.5)

	input = getch()
	if input == 'q':
		break
	else:
		paddle.move(input)
	
	screen.display()