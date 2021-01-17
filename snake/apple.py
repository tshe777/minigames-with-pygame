import random 
from config import Config

class Apple():
	def __init__(self):
		self.setNewLocation()

	def setNewLocation(self):
		self.x = random.randint(0, Config.CELL_WIDTH - 3)
		self.y = random.randint(0, Config.CELL_HEIGHT - 3)
	