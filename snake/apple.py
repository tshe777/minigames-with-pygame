import random 
from config import Config
#		maybe can also use sprites (auto have a hitbox and just set == CELLSIZE) to animate apple
# 		inherit from Sprite parent class
		#		Sprite.__init__(self)
		#		self.image = image.load("filename")
		#		self.rect = self.image.get_rect()


class Apple():
	def __init__(self):
		self.setNewLocation()

	def setNewLocation(self):
		self.x = random.randint(0, Config.CELL_WIDTH - 3)
		self.y = random.randint(0, Config.CELL_HEIGHT - 3)
	