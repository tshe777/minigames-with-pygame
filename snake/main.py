#snake game by tao
"""
implementation for google play:
1. watch ad to add life?
2. store high score?
3. fun power ups like slow down time (lower FPS), randomly put another apple or 2 or 3, 

"""



"""
------PLANNING-----

procedure:
	1. draw window | clear screen
	2. keep updating window | update game 
	3. handle inputs | update game
	4. handle data -> draw graphics | draw game 

properties:

1. game behavior

	game over:
		if snake hits edge of screen or hits itself
		make new game upon any keydown
	snake movement:
		body trails its head
	powerups:
		eating an apple grows body by length one
	score:
		length of snake
	menu screen:
		shows time 
		disappears upon any keydown
	input:
		arrow keys and wasd change snake direction

2. constants
	- Colors
	- Apple size
	- Game board size
	- Window dimensions
	- Frame rate


3. data definitions

	apple
	- has an x and y which is random -> interation with snake makes it reposition 

	snake
	- each block has an x and y
	- entire snake is sum of blocks -> maybe a list or dictionary 
	[{"x": 1, "y": 2}, {"x": snake[0].x - 1}]	 
	- moves by deleting last block and moving to new location based on direction


4. functions
	- snake movement, snake eating and growing, apple repositioning, game ending
"""

import sys
from game import Game

def main():
	game = Game()
	game.run()
	sys.exit()

if __name__ == '__main__':
	main()
