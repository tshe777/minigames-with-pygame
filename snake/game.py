from config import Config
from apple import Apple
from snake import Snake
import pygame, sys

class Game():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
		self.clock = pygame.time.Clock()
		self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
		self.BASICFONTTITLE = pygame.font.Font('freesansbold.ttf', 35)
		self.BASICFONTMENU = pygame.font.Font('freesansbold.ttf', 65)
		pygame.display.set_caption('SNAKEGAME')
		self.apple = Apple()
		self.snake = Snake()

	def drawGrid(self):
		for x in range (0, Config.WINDOW_WIDTH, Config.CELLSIZE):
			pygame.draw.line(self.screen, Config.GRIDCOLOR, (x,0), (x, Config.WINDOW_HEIGHT))
		for y in range (0, Config.WINDOW_HEIGHT, Config.CELLSIZE):
			pygame.draw.line(self.screen, Config.GRIDCOLOR, (0,y), (Config.WINDOW_WIDTH, y))

	def drawSnake(self):
		for coord in self.snake.snakeCoords:
			x = coord["x"] * Config.CELLSIZE
			y = coord["y"] * Config.CELLSIZE
			snakeSegmentRect = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)
			pygame.draw.rect(self.screen, Config.DARKGREEN, snakeSegmentRect)
			snakeInnerSegmentRect = pygame.Rect(x + 4, y + 4, Config.CELLSIZE-8, Config.CELLSIZE-8)
			pygame.draw.rect(self.screen, Config.GREEN, snakeInnerSegmentRect)

	def drawApple(self):
		x = self.apple.x * Config.CELLSIZE
		y = self.apple.y * Config.CELLSIZE
		appleRect = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)
		pygame.draw.rect(self.screen, Config.RED, appleRect)

	def drawScoreboard(self, score):
		scorex = Config.WINDOW_WIDTH-120
		scorey = 10
		scoreboard = self.BASICFONT.render("Score: " + str(score), True, Config.WHITE)
		self.screen.blit(scoreboard, (scorex, scorey))

	def isGameOver(self):
		if (self.snake.snakeCoords[self.snake.HEAD]['x'] == -1 or 
			self.snake.snakeCoords[self.snake.HEAD]['x'] == Config.CELL_WIDTH or 
			self.snake.snakeCoords[self.snake.HEAD]['y'] == -1 or 
			self.snake.snakeCoords[self.snake.HEAD]['y'] == Config.CELL_HEIGHT):
			return self.resetGame()
		for snakeBody in self.snake.snakeCoords[1:]:
			if (snakeBody["x"] == self.snake.snakeCoords[self.snake.HEAD]["x"] and
				snakeBody["y"] == self.snake.snakeCoords[self.snake.HEAD]["y"]):
				return self.resetGame()

	def resetGame(self):
		#clears the board 
		del self.snake
		del self.apple
		self.snake = Snake()
		self.apple = Apple()
		return True

	def checkForKeyPress(self):
		keyInput = pygame.event.get(pygame.KEYUP)
		if len(keyInput) != 0:
			if keyInput[0].key == pygame.K_ESCAPE:
				pygame.quit()
				quit()
			else:
				return keyInput[0].key

	def drawPressAnyKeyMsg(self):
		press_key_messagex = Config.CELLSIZE / 2
		press_key_messagey = Config.CELLSIZE / 2
		msg = self.BASICFONT.render("PRESS ANY KEY TO CONTINUE", True, Config.WHITE)
		self.screen.blit(msg, (press_key_messagex, press_key_messagey))

	def displayGameOver(self):
		gameOverScreenx = Config.WINDOW_WIDTH / 2
		gameOverScreeny = Config.WINDOW_HEIGHT / 2
		gameOverMsg = self.BASICFONTTITLE.render("GAME OVER", True, Config.WHITE)
		self.screen.blit(gameOverMsg, (gameOverScreenx, gameOverScreeny))
		self.drawPressAnyKeyMsg()
		pygame.display.update()
		pygame.time.wait(200)
		self.checkForKeyPress()
		while True:
			if self.checkForKeyPress():
				pygame.event.get()
				return

	def handleKeyEvents(self, event):
		if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.snake.direction != self.snake.DOWN:
			self.snake.direction = self.snake.UP
		if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self.snake.direction != self.snake.RIGHT:
			self.snake.direction = self.snake.LEFT
		if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.snake.direction != self.snake.UP:
			self.snake.direction = self.snake.DOWN
		if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self.snake.direction != self.snake.LEFT:
			self.snake.direction = self.snake.RIGHT
		elif event.key == pygame.K_ESCAPE:
			pygame.quit()

	def showMenu(self):
		menuSurf1 = self.BASICFONTMENU.render('SNAKE GAME LOOOOL', True, Config.WHITE, Config.RED)
		menuSurf2 = self.BASICFONTMENU.render('SNAKE GAME LOOOOL', True, Config.GREY)
		degrees1, degrees2 = 0, 0

		while True:
			for event in pygame.event.get(): #do I even need this
				if event.type == pygame.KEYDOWN:
					return
			self.screen.fill(Config.BACKGROUND_COLOR)
			rotSurf1 = pygame.transform.rotate(menuSurf1, degrees1)
			rotRect1 = rotSurf1.get_rect()
			rotRect1.center = (Config.WINDOW_WIDTH / 2, Config.WINDOW_HEIGHT / 2)
			self.screen.blit(rotSurf1, rotRect1)

			rotSurf2 = pygame.transform.rotate(menuSurf2, degrees2)
			rotRect2 = rotSurf2.get_rect()
			rotRect2.center = (Config.WINDOW_WIDTH / 2, Config.WINDOW_HEIGHT / 2)
			self.screen.blit(rotSurf2, rotRect2)
			
			self.drawPressAnyKeyMsg()
			pygame.display.update()
			self.clock.tick(Config.MENU_FPS)
			degrees1 += 1
			degrees2 += 3

	def draw(self):
		self.screen.fill(Config.BACKGROUND_COLOR)
		self.drawGrid()
		self.drawSnake()
		self.drawApple()
		self.drawScoreboard(len(self.snake.snakeCoords)-3)
		pygame.display.update()
		self.clock.tick(Config.FPS)


	def run(self):
		self.showMenu()
		while True:
			self.gameLoop()
			self.displayGameOver()

	def gameLoop(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self.handleKeyEvents(event)
			self.draw()
			self.snake.update(self.apple)
			if self.isGameOver():
				break
