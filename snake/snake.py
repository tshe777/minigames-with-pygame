from config import Config
from apple import Apple
import random

class Snake():
	UP = 'up'
	DOWN = 'down'
	LEFT = 'left'
	RIGHT = 'right'
	HEAD = 0
	def __init__(self):
		self.x = random.randint(Config.CELL_WIDTH * (1/4), Config.CELL_WIDTH * (3/4))
		self.y = random.randint(Config.CELL_HEIGHT * (1/4), Config.CELL_WIDTH * (3/4))
		self.direction = self.RIGHT
		self.snakeCoords = [{"x": self.x, "y": self.y},
							{"x": self.x-1, "y": self.y},
							{"x": self.x-2, "y": self.y}]
	def update(self, apple):
		# 1. check if snake head is at same coords as apple position (eating)
		# 2. move worm by adding very last segment into new position depending on keypress (UP, DOWN, LEFT, RIGHT)

		if self.snakeCoords[self.HEAD]["x"] == apple.x and self.snakeCoords[self.HEAD]["y"] == apple.y:
			apple.setNewLocation()
		else:
			del self.snakeCoords[-1]

		if self.direction == self.UP:
			newHead = {"x": self.snakeCoords[self.HEAD]["x"], "y": self.snakeCoords[self.HEAD]["y"] - 1}

		elif self.direction == self.DOWN:
			newHead = {"x": self.snakeCoords[self.HEAD]["x"], "y": self.snakeCoords[self.HEAD]["y"] + 1}

		elif self.direction == self.LEFT:
			newHead = {"x": self.snakeCoords[self.HEAD]["x"] - 1, "y": self.snakeCoords[self.HEAD]["y"]}

		elif self.direction == self.RIGHT:
			newHead = {"x": self.snakeCoords[self.HEAD]["x"] + 1, "y": self.snakeCoords[self.HEAD]["y"]}
		self.snakeCoords.insert(0, newHead)